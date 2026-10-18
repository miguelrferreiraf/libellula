"""Executa o notebook e verifica execução, contabilização e isolamento temporal."""
import json
import os
from pathlib import Path

os.environ['MPLBACKEND'] = 'Agg'
path = Path(__file__).with_name('modeloRLgestaobanca.ipynb')
notebook = json.loads(path.read_text(encoding='utf-8'))
scope = {}
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        print(f'Executando célula {i}', flush=True)
        exec(compile(''.join(cell['source']), f'{path.name}:cell-{i}', 'exec'), scope)

np = scope['np']
execute = scope['execute_trade']
settle = scope['settle_trade']
for direction in (1, -1):
    outputs = np.array([direction, .5, .01, .01])
    cases = [(102, 98, 'SL_AMBOS'),
             (102, 99.5, 'TP' if direction == 1 else 'SL'),
             (100.5, 98, 'SL' if direction == 1 else 'TP'),
             (100.5, 99.5, 'CLOSE')]
    for high, low, expected in cases:
        execution = execute(outputs, dict(Open=100., High=high, Low=low, Close=100.2))
        assert execution['reason'] == expected
        result = settle(100., outputs, execution)
        np.testing.assert_allclose(result['net_pnl'], direction * .5 * (execution['exit'] - 100))
        np.testing.assert_allclose(result['capital_after'], 100 + result['net_pnl'])
    touch = execute(outputs, dict(Open=100., High=101., Low=99., Close=100.))
    assert touch['reason'] == 'SL_AMBOS'
flat = execute(np.zeros(4), dict(Open=100., High=102., Low=98., Close=101.))
assert settle(100., np.zeros(4), flat)['capital_after'] == 100.
assert (scope['market'].loc[scope['train_idx'], 'execution_time'] < scope['val_idx'][0]).all()
assert (scope['market'].loc[scope['val_idx'], 'execution_time'] < scope['test_idx'][0]).all()
np.testing.assert_allclose(scope['mean'], scope['state'].loc[scope['train_idx']].mean())
env = scope['test_evaluation']
assert len(env.history) == len(scope['test_idx'])
np.testing.assert_allclose(env.equity, scope['INITIAL_CAPITAL'] + sum(r['net_pnl'] for r in env.history))
try:
    env.step(np.zeros(3))
except RuntimeError:
    pass
else:
    raise AssertionError('O ambiente aceitou ação após término.')
assert env.reset().shape == (33,)
assert env.equity == scope['INITIAL_CAPITAL'] and not env.history

# Ações contínuas: valores intermediários distintos, sem grade nem teto de risco.
convert = scope['sacred_outputs']
grid = np.linspace(-9, 9, 1001)
outputs = np.array([convert([x, x, x], .01) for x in grid])
assert len(np.unique(outputs[:, 1])) == len(grid)
assert len(np.unique(outputs[:, 2])) == len(grid)
assert (outputs[:, 1] >= 0).all() and (outputs[:, 1] <= 1).all()
assert outputs[-1, 1] * outputs[-1, 3] > .01
for direction in (1, -1):
    for x in (-1000., -7.123, 0., 4.567, 1000.):
        out = convert([0., x, x], direction)
        trade = execute(out, dict(Open=100., High=101., Low=99., Close=100.))
        assert trade['tp'] > 0 and trade['sl'] > 0
        assert direction * (trade['tp'] - 100.) > 0
        assert direction * (trade['sl'] - 100.) < 0
        assert 0 <= 100 * out[1] <= 100
assert convert([0, 4, 0], 1)[2] > 1  # TP comprado sem teto artificial
assert convert([0, 0, 4], -1)[3] > 1  # SL vendido sem teto artificial
torch = scope['torch']
model = scope['model']
assert model.log_std.grad is not None and torch.isfinite(model.log_std.grad).all()
expected = ['timestamp', 'Position_size', 'Take_profit', 'Stop_loss', 'Result', 'Capital_atualizado']
for history in scope['training_histories']:
    table = scope['operations_table'](history)
    assert list(table.columns) == expected and len(table) == len(history)
    np.testing.assert_allclose(table.Capital_atualizado, scope['INITIAL_CAPITAL'] + table.Result.cumsum())
    assert (table.Position_size <= history.capital_before).all()
assert len(scope['training_histories']) == scope['EPISODES']
assert len(scope['all_operations']) == sum(map(len, scope['training_histories']))
print('PASS: espaço contínuo, gradientes, preços positivos, exposição, tabelas completas, saldo, execução e blocos temporais.')

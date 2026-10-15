"""Reorganização visual sem modificar instruções Python do notebook."""
import ast
import copy
import json
from pathlib import Path


def format_notebook(path):
    notebook = json.loads(path.read_text(encoding='utf-8'))
    original = copy.deepcopy(notebook)
    if notebook['metadata'].get('libellula_layout') == 'readable-v1':
        return
    details = {
        1: '''### Fontes de dados e referência temporal

- **Estado do RL:** features de risco e previsões disponíveis em *t*.
- **Dataset ambiente:** OHLC importado do histórico original, usado na execução em *t+1*.
- **Próximo período:** próxima vela do histórico, inclusive após fins de semana.

### Integridade e separação das informações

**O OHLC real futuro não entra na observação do agente.** A validação confere valores finitos, timestamps e correspondência do fechamento em *t*. Transições com OHLC inconsistente são excluídas e registradas, sem alterar preços ou substituir a vela seguinte.
''',
        2: '''### Contrato dos outputs sagrados

O vetor segue a ordem **[direção, fração de exposição, distância TP, distância SL]**.

1. **Direção:** sinal da previsão do TFT.
2. **Exposição:** parcela da banca destinada à operação.
3. **TP e SL:** distâncias relativas ao preço de entrada.

### Observação e parâmetros do protótipo

- **33 elementos:** 29 features e quatro variáveis do estado da banca.
- **9 ações:** ficar fora ou escolher uma das oito combinações operacionais.
- **Custos zero**, exposição sem alavancagem e risco nominal limitado ao SL.

*Os valores numéricos são configuráveis; a padronização usa somente o treino.*
''',
        3: '''### Reinicialização de cada episódio

- **Capital e pico:** começam no valor inicial configurado.
- **Posições abertas:** nenhuma.
- **Histórico:** novo registro para cada episódio.

*Os saldos de episódios diferentes não são somados.*
''',
        4: '''### Informação disponível no instante da decisão

- Features da linha corrente em *t*, padronizadas com estatísticas do treino.
- Patrimônio relativo ao capital inicial e drawdown atual.
- Exposição e posição aberta iguais a zero entre as operações.

**A observação não consulta a tabela OHLC futura.**
''',
        5: '''### Da política à operação

1. A rede estima **probabilidades de ação** e **valor esperado**.
2. O treino sorteia ações para explorar; a avaliação escolhe a maior probabilidade.
3. A conversão aplica limites de exposição e risco ao SL.

*A decisão precede o conhecimento do Open real seguinte; preços e quantidade são definidos pelo executor.*
''',
        6: '''### Regras de saída na vela real de t+1

1. **Somente TP atingido:** saída no TP.
2. **Somente SL atingido:** saída no SL.
3. **Ambos atingidos:** SL primeiro, pela convenção conservadora.
4. **Nenhum atingido:** saída no **Close real de t+1**.

*Toque exato no nível conta como execução. Compras e vendas têm níveis em sentidos opostos.*
''',
        7: '''### Calculadora interna da banca

- **Quantidade:** capital anterior × exposição ÷ entrada.
- **Resultado:** direção × quantidade × (saída − entrada).
- **Novo capital:** capital anterior + resultado líquido.

**Custos são zero no protótipo.** O patrimônio é atualizado após liquidar a operação.
''',
        8: '''### Recompensa e trilha de auditoria

- **Recompensa básica:** resultado líquido ÷ capital anterior.
- **Penalização opcional:** aumento do drawdown; coeficiente inicialmente zero.
- **Registro:** timestamps, ação, níveis, execução, quantidade, resultado e banca.

*Ficar fora produz recompensa zero; cada transição permanece disponível para inspeção.*
''',
        9: '''### Encerrar a operação e avançar

1. Converter a ação e executar a operação.
2. Liquidar o resultado e registrar a transição.
3. Avançar **uma linha** ou encerrar o episódio.

**Nenhuma posição é carregada.** Após o término, uma nova ação exige reinicialização.
''',
        10: '''### Organização do treinamento

1. Separar **treino, validação e teste** em ordem temporal.
2. Ajustar a padronização exclusivamente no treino.
3. Treinar a política ator-crítico com episódios completos.
4. Selecionar pesos pelo capital final da validação.
5. Avaliar a política selecionada e destacar os capitais.

**Cada episódio começa com a banca inicial.** Repetir o histórico não cria novos cenários.
''',
        11: '''### Leitura dos resultados

- **Evolução:** capital por episódio e perda ator-crítico.
- **Gestão da banca:** patrimônio e drawdown no teste.
- **Operações:** quantidade, taxa de acerto e motivos de saída.
- **Comparação:** política RL, exposição fixa na direção do TFT e permanecer fora.

### Rastreabilidade

Pesos, normalizador, configurações, hashes e registros ficam em **`resultados`**.

*Perda menor não garante política melhor; modificar parâmetros após examinar o teste transforma esse bloco em validação.*
''',
    }
    splits = {
        2: [
            ('from pathlib import Path', '### 1.1 Bibliotecas e recursos locais', 'As bibliotecas são carregadas uma vez; toda a lógica operacional permanece no notebook.'),
            ('ROOT = next', '### 1.2 Caminhos e reprodutibilidade', 'Localizamos o projeto e fixamos a **semente aleatória**.'),
            ('state = pd.read_parquet', '### 1.3 Importação e validação do estado', 'Conferimos o contrato das **29 features** e a integridade do índice.'),
            ('raw = pd.read_csv', '### 1.4 Importação do dataset ambiente', 'Interpretamos as datas originais e identificamos as velas com OHLC inconsistente.'),
            ('future = ohlc.shift', '### 1.5 Alinhamento do período real seguinte', 'O deslocamento ocorre **antes da exclusão** de transições inválidas.'),
            ("print(f'Estado:", '### 1.6 Conferência visual do alinhamento', 'Mostramos o tamanho utilizável e exemplos dos pares *t → t+1*.'),
        ],
        4: [
            ('INITIAL_CAPITAL =', '### 2.1 Parâmetros configuráveis', 'Aqui ficam **banca inicial**, limites, distâncias de saída e parâmetros de treinamento.'),
            ('assert INITIAL_CAPITAL', '### 2.2 Validação e catálogo de ações', 'Verificamos os limites e enumeramos as combinações que o agente poderá escolher.'),
        ],
        10: [
            ('class ActorCritic', '### 5.1 Rede de política e valor', 'As duas cabeças compartilham uma representação das observações.'),
            ('def sacred_outputs', '### 5.2 Conversão para os outputs sagrados', 'Aplicamos a direção prevista e os **limites operacionais** antes da execução.'),
        ],
        20: [
            ('n = len(state)', '### 10.1 Separação temporal e normalização', '**As operações das bordas não atravessam o bloco seguinte.** As estatísticas são ajustadas apenas no treino.'),
            ('def make_env', '### 10.2 Ambientes e avaliação determinística', 'Construímos ambientes independentes e uma rotina de avaliação sem atualização de pesos.'),
            ('model = ActorCritic', '### 10.3 Inicialização do agente e acompanhamento', 'Criamos a rede, o otimizador e os registros de seleção na validação.'),
            ('for episode in range', '### 10.4 Ciclo de aprendizado ator-crítico', 'O ciclo é mantido inteiro: coleta → retornos descontados → atualização dos pesos → validação. **Treino e avaliação usam bancas separadas.**'),
            ('model.load_state_dict', '### 10.5 Avaliação dos pesos selecionados', 'Carregamos a política escolhida na validação e executamos os três blocos.'),
            ('def capital_banner', '### 10.6 Capital inicial e final em destaque', '**O capital do último episódio de treino e o capital do teste aparecem separadamente.**'),
        ],
        22: [
            ('def metrics', '### 11.1 Métricas da banca e das operações', 'A taxa de acerto considera somente operações efetivas; o retorno usa a banca inicial.'),
            ('fixed_test =', '### 11.2 Comparadores no mesmo bloco de teste', 'Comparamos estratégias com **o mesmo executor e a mesma banca inicial**.'),
            ('fig, axes =', '### 11.3 Gráficos de evolução', 'Os gráficos mostram capital por episódio, perda, patrimônio e drawdown.'),
            ('display(test_log.reason', '### 11.4 Inspeção dos motivos e registros', 'As tabelas permitem conferir as saídas e as primeiras transições do teste.'),
            ('OUTPUT_DIR.mkdir', '### 11.5 Salvamento dos artefatos', 'Salvamos os pesos, a padronização, os históricos e a figura de monitoramento.'),
            ('manifest =', '### 11.6 Manifesto de reprodutibilidade', 'O manifesto registra configurações, divisão temporal, **exclusões e hashes dos datasets**.'),
        ],
    }
    def markdown(text):
        return dict(cell_type='markdown', metadata={}, source=text.splitlines(True))
    cells = []
    for index, cell in enumerate(original['cells']):
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            if source.startswith('## '):
                number = int(source.split('.')[0].replace('## ', ''))
                title, body = source.split('\n', 1)
                cell = copy.deepcopy(cell)
                cell['source'] = (title + '\n\n' + details[number] +
                                  '\n### Detalhes e convenções\n\n' + body).splitlines(True)
            cells.append(cell)
        elif index in splits:
            source = ''.join(cell['source'])
            positions = [source.index(anchor) for anchor, _, _ in splits[index]] + [len(source)]
            assert positions == sorted(positions) and positions[0] == 0
            # Não atribuir resultados antigos a fragmentos novos.
            for j, (_, title, explanation) in enumerate(splits[index]):
                cells.append(markdown(title + '\n\n' + explanation + '\n'))
                fragment = source[positions[j]:positions[j+1]]
                ast.parse(fragment)
                cells.append(dict(cell_type='code', metadata=copy.deepcopy(cell['metadata']),
                                  execution_count=None, outputs=[], source=fragment.splitlines(True)))
        else:
            cells.append(cell)
    for i, cell in enumerate(cells):
        cell['id'] = f'rl-readable-{i:03d}'
    before = ''.join(''.join(c['source']) for c in original['cells'] if c['cell_type'] == 'code')
    after = ''.join(''.join(c['source']) for c in cells if c['cell_type'] == 'code')
    assert before == after, 'As instruções Python foram modificadas.'
    assert ast.dump(ast.parse(before)) == ast.dump(ast.parse(after))
    headings = [c['source'][0].strip() for c in cells if c['cell_type'] == 'markdown' and c['source'][0].startswith('## ')]
    expected = [c['source'][0].strip() for c in original['cells'] if c['cell_type'] == 'markdown' and c['source'][0].startswith('## ')]
    assert headings == expected and len(headings) == 11
    notebook['cells'] = cells
    notebook['metadata']['libellula_layout'] = 'readable-v1'
    path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False), encoding='utf-8')
    print(f'Layout atualizado: {len(cells)} células; código idêntico; 11 etapas preservadas.')


if __name__ == '__main__':
    format_notebook(Path(__file__).with_name('modeloRLgestaobanca.ipynb'))

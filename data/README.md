# Catálogo de dados e reprodutibilidade

Este catálogo descreve o estado verificável dos datasets presentes no repositório em 2026-09-07. Um identificador de versão é o SHA-256 integral do arquivo: qualquer alteração no conteúdo produz uma versão diferente. Não substitui a identificação de versão do fornecedor, que ainda não foi registrada.

## Convenções

- Ativo: `EUR/USD`.
- Periodicidade observada: diária; não há registro de calendário, horário de fechamento ou convenção de barra do fornecedor.
- Fuso horário: desconhecido. A coluna `Date` não contém horário nem offset.
- Provedor, método de coleta, data de extração, licença e parâmetros de exportação: não documentados nos arquivos recebidos.
- Datas são tratadas como calendário sem fuso. `EUR_USD.csv` chega em ordem decrescente e é ordenado crescentemente antes do cálculo de indicadores.
- As transformações removem linhas sem indicadores ou alvo futuro; o `setup()` converte `Change %` para fração, cria `target_return` e `target_direction`, e separa 70%/15%/15% em ordem temporal.

## Datasets ativos

| Dataset | Papel e linhagem | Linhas x colunas / período | Versão SHA-256 |
| --- | --- | --- | --- |
| `raw/EUR_USD.csv` | Entrada OHLC de EUR/USD; fonte externa não identificada. | 1.568 x 7; 2020-02-11 a 2026-02-11 | `2fdeed033f3cdbe13218f0368dc81498d315e8beffe74769573f7187c016309d` |
| `processed/financial_tools_datset.csv` | `raw/EUR_USD.csv` processado por `notebooks/financial_tools/financial_tools.ipynb`; OHLC mais indicadores técnicos. | 1.568 x 25; 2020-02-11 a 2026-02-11 | `0d1c38791539b86d18378818368aafb76e1f519c17390ce698fee7d084455430` |
| `processed/dataset_processed.csv` | Saída de `src/setup.py`; dataset técnico limpo com alvo futuro. | 1.366 x 27; 2020-11-18 a 2026-02-10 | `99be595c8ff0ccdf4cf6dd38b839cc260f41175b1035da489f73ee8dfc0f189a` |
| `processed/cvar/cvar_features.parquet` | Features CVaR do dataset técnico. | 205 x 3; 2024-07-18 a 2025-04-30 | `cf74fef5340c0a3a5043e47fa823ebec9a7255a007705c5f378de01acc6f422f` |
| `processed/epf/epf_features.parquet` | Features EPF do dataset técnico. | 205 x 4; 2024-07-18 a 2025-04-30 | `a876d12c462d6879afc6883d18cbcf83dc2a65d61612831106faf56dc6a1d094` |
| `processed/evt/evt_features.parquet` | Features EVT ancoradas no índice EPF. | 205 x 4; 2024-07-18 a 2025-04-30 | `19924d93e025d39e9e8a107d69bebcdb1e301ae80c78e13e86b120eb2a7d6e0c` |
| `processed/pdfd/pdfd_features.parquet` | Features de distribuição de perdas. | 205 x 6; 2024-07-18 a 2025-04-30 | `2cf0ad9217e5198e2c363dede89664f7f4f44749c3ed8fd7bde794c684fd3eb6` |
| `processed/qf/qf_features.parquet` | Features de previsão por quantis. | 205 x 8; 2024-07-18 a 2025-04-30 | `118e0f799f0b7648596cfded5c7b1a77366323f935e027984dfd0e63b7aa18fd` |
| `processed/combined/risk_features.parquet` | Concatenação das cinco saídas do envelope de risco. | 205 x 25; 2024-07-18 a 2025-04-30 | `c76bd517d988b4e88253659defd7fd3229c7ed148697d7dafaf18b68d77a4189` |

## Arquivos fora do pipeline ativo

- `raw/EUR_USD_1.csv`: exportação em esquema localizado (`Data`, `Último`, `Var%`), sem notebook consumidor; não deve ser confundida com a entrada ativa.
- `processed/pdfd_dataset.csv`: artefato legado, sem notebook consumidor atual.
- `notebooks/Predictive_TFT_model/risk_with_predictions.parquet`: artefato legado da concatenação entre TFT e risco; não é mais produzido pelo notebook TFT.

## Saídas do pipeline de estado para RL

- `processed/predictions/tft_predictions.parquet`: previsões da validação produzidas exclusivamente pelo notebook TFT.
- `processed/rl_state/rl_state.parquet`: concatenação estrita de `risk_features.parquet` e `tft_predictions.parquet`, produzida por `src/pipelines/rl_state.py` para o futuro agente de RL.
- `processed/rl_state/rl_state.metadata.json`: manifesta os hashes dos dois insumos e da saída. Seus hashes, período e dimensões devem ser incluídos na tabela de datasets ativos após a primeira execução.

## Procedimento de reprodução

1. Registrar fornecedor, URL/API, data e hora de coleta com fuso, ativo, granularidade, convenção de preço e parâmetros de exportação antes de substituir `raw/EUR_USD.csv`.
2. Registrar o SHA-256 do novo arquivo bruto neste catálogo.
3. Executar `financial_tools`, as cinco ferramentas de risco, `Concatenation` e o TFT, nessa ordem.
4. Atualizar as dimensões, período e SHA-256 de cada saída alterada neste catálogo.

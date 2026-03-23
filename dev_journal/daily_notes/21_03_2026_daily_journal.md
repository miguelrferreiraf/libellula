# :calendar: 21-03-2026 (saturday)
***by: Miguel Ferreira***

> **As atividades deste daily log são relativas ao 'week plan' da semana de 16/03/26 - segunda-feira - até 23/03/26 - segunda feira seguinte**

## :rocket: Objetivo
***(Objetivos são programados no planejamento semanal, disponível na na pasta ```week_pln/```).***
- Criar o CVaR
- O CVaR (e todas as outras ferramentas e modelo do envelope de risco) deverão ser criadas de forma padronizada para evitar que não possam ser conogregadas num mesmo output geral.
- Esta padronização segue o seguinte protocolo:
> 1. Importação dos dados financeiros (OHLC + indicadores econômicos) ep ré-processamento via método (```setup()```)
> 2. Criação do modelo/ferramenta do envelope
> 3. Aplicação do dataset ao modelo ferramenta recém-criado
> 4. Testes de eficiência para detecção de viéses, vazamentos ou quaisquer anomalias estatísticas
> 5. Geração de output
> 6. Salvamento da ferramenta/modelo  
## :wrench: Atividades
- CVaR criado
## :open_file_folder: Arquivos/notebooks trabalhados
- ```notebooks/risk_envelope/CVaR.ipynb``` *(criado)*
## :white_check_mark: Resultados
- Testes e outputs satisfatórios
## :bookmark_tabs: Observações
- **HOJE FIZEMOS ALTERAÇÕES ESTRUTURAS NA PIPELINE!**
- Antes, a ideia central do envelope de risco era analisar milhares de cotações e devolver uma array de dados probabilíticos a serem analisados pelo modele de reinforcement learning de gestão de banca.
- Mas isso não parecia muito eficiente: teríamos que analisar millhares de dados e deles decantar uma minúscula array de dados probabilísiticos de risco a ser analisado pelo modelo de RL de gestão de banca.
- Agora, graças a um breve experimento que fizemos com o CVaR, descobri que podemos gerar uma array de dados probabilísticos de risco para cada linha de dados financeiros do dataset original.
- Mas isso implica mudanças estruturais no funcionamento de nossa pipeline. Ao menos teremos dados suficientes para treinar o RL de gestão de risco...
## :thought_balloon: Próximos passos
- **PADRONIZAR O EPF E O QF EM SEGUNDO O PROTOCOLO ACIMA DESCRITO.... EM REGIME DE URGÊNCIA**
- Continuar criando mais ferramentas e modelos para o envelope de risco.
## versionamento
| Commits | Descrição | Notas | Início/fim | Versão |
| :--- | :---: | :--- | :--- | :--- |
| ```creating CVaR``` | Criando CVaR | CVaR pronto, testado e funcional | 19h23-00h00 | ? |


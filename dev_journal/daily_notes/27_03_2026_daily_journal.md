# :calendar: 28-03-2026 (friday)
***by: Miguel Ferreira***

> O trabalho dentro deste daily log é baseado no week plan criado para os dias desde de 28/03/2026 até 04/04/2026 (```week_plan/04_week_pln```), criado no dia 27/03/2026. Ele pode ser encontrado na pasta ```/Libellula/dev_journal/week_plan/```.  Apenas a título de curiosidade, estes são os objetivos:
>> 1. O envelope de risco já possui EPF, QF e CVaR. Criar o PDFD
>> 2. PADRONIZAR O NOTEBOOK E O CÓDIGO DE CADA UM DOS SUPRACITADOS
>> 3. Transformar os outputs (pacotes de decisão) num único dataset
>> 4. Iniciar um protótipo do TFT preditivo para datasets multivariados
>> 5. Aplicar o TFT num dataset com rolling window de pelo menos 5% e dataset de pelo menos 5 mil períodos.

> Este é o registro das atividades feitas em cima deste planejamento semanal supracitado.

## :rocket: Objetivo
***(Objetivos são programados no planejamento semanal, disponível na na pasta ```week_pln/```).***
- Criar PDFD
- Gerar output com dataset usável
## :wrench: Atividades
- PDFD criado
- Output com coluna de dados também criado
## :open_file_folder: Arquivos/notebooks trabalhados
- ```notebooks/financial_tools/PDFD.ipynb``` *(criado)*
## :white_check_mark: Resultados
- PDFD com parâmetros variados, todos bem executados 
- Janela de risco utilizada:
```
risk_window = 252
```
- Testes com resultados satisfatórios
## :bookmark_tabs: Observações
- Teste de PDFD (*sannity checks*) executado sob os seguintes parâmetros de drawndown:
```
drawdown_levels = [
    -0.005,
    -0.01,
    -0.02,
    -0.03
]
```
## :thought_balloon: Próximos passos
- Padronização geral de todas as ferramentas financeiras dentro do protocolo! **URGENTE!**
## versionamento
| Commits | Descrição | Notas | Início/fim | Versão |
| :--- | :---: | :--- | :--- | :--- |
| ```creating PDFD!!!``` | Criação do PDFD | none | 22h00-00h00 | ? |


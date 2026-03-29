# :calendar: 29-03-2026 (sunday)
***by: Miguel Ferreira***

> O trabalho dentro deste daily log é baseado no week plan criado para os dias desde de 28/03/2026 até 04/04/2026 (```week_plan/04_week_pln```), criado no dia 27/03/2026. Ele pode ser encontrado na pasta ```/Libellula/dev_journal/week_plan/```.

## :rocket: Objetivo
***(Objetivos são programados no planejamento semanal, disponível na na pasta ```week_pln/```).***
- O objetivo hoje era padronizar todas as ferramentas do envelope para seguirem o protocolo de ordenamento dos notebooks:
> 1. Data preparation
> 2. Model construction
> 3. Sanity checks
> 4. Generation of risk features
> 5. Output standardization
> 6. Saving the feature
## :wrench: Atividades
- Isto foi feito com ajuda do Codex (ChatGPT) conectado ao diretório do projeto
## :open_file_folder: Arquivos/notebooks trabalhados
- ```/notebooks/risk-envelop/epf.ipynb``` (manualmente)
- ```/notebooks/risk-envelop/PDFD.ipynb``` (usando o Códex)
- ```/notebooks/risk-envelop/quantile_forecasting.ipynb``` (usando o Códex)
- ```/notebooks/risk-envelop/PDFD.ipynb``` (usando o Códex)
## :white_check_mark: Resultados
- **Satisfatórios**
## :bookmark_tabs: Observações
- Após o prompt ser executado no Códex, devemos iniciar um PR (*Pull Request*)
- O PR gera um branch nova no projeto
- Então devemos verificá-la. A descrição da branch é redigida pelo próprio Codex
- Após a verificação comparativa da nova branch com o modelo atual, executamos o 'merge', para tornar a branch em 'main'
- Depois, podemos excluir a branch colateral
- Para permitir o trabalho no repositório local, executamos um ```git pull orgin main```
 imediato
 ## :thought_balloon: Próximos passos
- Verificar a eficiência da padronização
- Testar as colunas de features e ver e estão trabalháveis
- Criar o esboço do TFT multivariado
## versionamento
| Commits | Descrição | Notas | Início/fim | Versão |
| :--- | :---: | :--- | :--- | :--- |
| ```adding epf standardized and daily logs``` | EPF padronizado segundo novo protocolo | none | 0h00-1h38 | 11h30-00h00 |
| ```Align quantile forecasting notebook with risk-envelope protocol``` | QF padronizado segundo novo protocolo | none | 11h30-00h00 | ? |
| ```Merge pull request #1 from miguelrferreiraf/codex/adapt-jupyter-notebook-to-libelula-protocol``` | Merge da branch criada pelo Codex para QF | none | 11h30-00h00 | ? |
| ```Standardize CVaR and PDFD notebook structure``` | CVaR e PDFD padronizado pelo Codex segundo novo protocolo | none | 11h30-00h00 | ? |
| ```Merge pull request #2 from miguelrferreiraf/codex/standardize-risk-envelope-notebooks-structure``` | merge da branch criada pelo Codex para padronizar CVaR e PDFD | none | 11h30-00h00 | ? |


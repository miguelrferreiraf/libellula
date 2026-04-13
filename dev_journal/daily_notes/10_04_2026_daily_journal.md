# :calendar: 10-03-2026 (friday)
***by: Miguel Ferreira***

> O trabalho dentro deste daily log é baseado no week plan criado para os dias desde de 28/03/2026 até 04/04/2026 (```week_plan/04_week_pln```), criado no dia 27/03/2026. Ele pode ser encontrado na pasta ```/Libellula/dev_journal/week_plan/```.

## :rocket: Objetivo
***(Objetivos são programados no planejamento semanal, disponível na na pasta ```week_pln/```).***
- O objetivo hoje era fazer com que cada ferramenta do envelope de risco fornecesse outputs como features que pudessem ser concatenados no dataset que será usado pelo modelo de RL de gestão de banca! Estas sao as features que estamos pleiteando: 
1. EPF
```
epf_upper
epf_lower
epf_width
epf_asymmetry
```
### **:bangbang:THATS THE SINGLE ONE WHICH IS ACTUALLY DONE!**
2. Quantile forecasting:
```
q5
q25
q50
q75
q95
```
3. CVaR:
**Esse tá difícil, eu vejo isso depois!**
4. PDFD:
```
pdfd_005
pdfd_01
pdfd_02
pdfd_03
```
## :wrench: Atividades
- **SÓ CONSEGUIR GERAR AS FEATURES PARA UMA FERRAMENTA!: O EPF.** Mas já é um começo...
- Escrevi no notebook sobre a necessidade de se padronizar o restante do trabalho de geração de features nas outras ferramentas do envelope.
## :open_file_folder: Arquivos/notebooks trabalhados
- ```/notebooks/risk-envelop/epf_FINAL.ipynb``` *(criado)*
## :white_check_mark: Resultados
- **Satisfatórios**
## :bookmark_tabs: Observações
- **Precisamos criar uma pasta para armazenar os datasets gerados pelas ferramentas do envelope de risco!**
- Isso tem que ser bem organizado! É muito fácil fazer bagunça entre os datasets, já que eles serão gerados em grande número, e o ideal é que haja uma pasta para cada tipo de dataset.
- **Ou não!** Já que a cada rodagemdo kernel, o dataset gerado será sempre gerado com o mesmo nome, o que significa que o novo dataset substituirá o que já existe!  
 ## :thought_balloon: Próximos passos
- **REFAZER O MESMO PROCESSO COM TODAS AS OUTRAS FERRAMENTAS DO ENVELOPE DE RISCO!!!**:
> 1. Quantile Forecasting
> 2. CVaR
> 3. PDFD
- O *Quantile Forecasting* parece o mais complicado de se aplicar este protocolo de trabalho (o mesmo que aplicamos no EPF)
- Então talvez o próximo deva ser o **CVaR**
## versionamento
| Commits | Descrição | Notas | Início/fim | Versão |
| :--- | :---: | :--- | :--- | :--- |
| ```commiting final EPF model with dataset``` | Adicionamos scripts para geração de features de dados estatísticos trabalháveis pelo modelo de RL de gestão de banca | Temos que fazer isso com todas as outras ferramentas do envelope | 11h00 - 00h00 | none |


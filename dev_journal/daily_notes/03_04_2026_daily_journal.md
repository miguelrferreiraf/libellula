# :calendar: 03-04-2026 (friday)
***by: Miguel Ferreira***
> DIAZINHO COMPLICADO!!!
>> **Problemas de infraestrutura relativos às versões conflitantes de bibliotecas e dependências (PyTorch, Scikit-Learn, etc.)**
> Este daily log trata de algumas tarefas feitas com base no planejamento semanal dsponível em ```/dev_journal/week_pln/```, mais especificamente no planejamento ```/04_week_pln```.

> Este é o registro das atividades feitas em cima deste planejamento semanal supracitado.

## :rocket: Objetivo
***(Objetivos são programados no planejamento semanal, disponível na na pasta ```week_pln/```).***
- Iniciar um protótipo do TFT preditivo para datasets multivariados
## :wrench: Atividades
- Protótipo iniciado!
## :open_file_folder: Arquivos/notebooks trabalhados
- ```notebooks/Predictive_TFT_model/``` *(criado)*
- ```notebooks/Predictive_TFT_model/predictive_tft_model.ipynb``` *(criado)*
```notebooks/Predictive_TFT_model/tft_env``` *(criado)*
## :white_check_mark: Resultados
- Ainda estamos em testes de versionamento de linguagem, bibliotecas e dependências
- **Temos alguns resultados quanto à eficiência do modelo TFT (é apenas um protótipo) mas são minguados e não resolvemos questões estruturais!**
## :bookmark_tabs: Observações
- **Tivemos que baixar uma versão defasada, mas mais robusta, do Python: o Python 3.11!**
- **Fizemos isso porque algumas bibliotecas e dependências não estavam atualizadas para serem executadas em versões mais recentes do Python (como a que eu usava: 3.14)**
- Baixamos estas versão e criamos um ambiente virtual (```virtual env```) **DENTRO DA PASTA RECÉM CRIADA PARA ACOMODAR OS ARQUIVOS DO TFT** (```/Predictive_TFT_model/```), para que o ambiente virtual fosse específico para este arquivo e modelo
- Criamos o ambiente virtual, acionamos ele e usamos o ```ipykernel``` para gerar um kernel específico para este arquivo, assim evitando problemas de versões antagônicas de bibliotecas e dependências coexistindo nos mesmos ambientes:
```
python -m ipykernel install --user --name tft_env
```
- **Executamos o kernel recém-criado no JupyterLab e trabalhamos dentro deste kernel, executando nele todas as células do notebook**
- Alguns probleminhas de versão continuam atrapalhando nosso progresso. 
- Salvamos uma descrição do passo-a-passo acima descrito **DENTRO DO PRÓPRIO NOTEBOOK DO TFT PREDITIVO!** (eu julguei que as informações eram muito importantes então as deixei num lugar manifesto). Portanto, mas detalhes podem ser encontrados em ```/notebooks/Predictive_TFT_model/predictive_tft_model.ipynb```.
## :thought_balloon: Próximos passos
- **RESOLVER OS PROBLEMAS INFRAESTRUTURASI RELATIVOS ÀS VERSÕES DAS BIBLIOTECAS E DEPENDÊNCIAS DENTRO DO AMBIENTE ```tft_env```!**
## versionamento
| Commits | Descrição | Notas | Início/fim | Versão |
| :--- | :---: | :--- | :--- | :--- |
| ```creating TFT prototype``` | Criação do protótipo do TFT | **ainda não finalizado! Problemas estruturais de versionamento de bibliotecas e dependências** | 13h00-20h00 | ? |


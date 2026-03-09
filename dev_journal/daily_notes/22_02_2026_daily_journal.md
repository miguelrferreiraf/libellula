# :calendar: 22-02-2026 (sunday)
***by: Miguel Ferreira***

### ***(Esta ```daily note``` foi feita post facto com base nas notas que eu escrevi em um documento pregresso já não mais existente. Ele, portanto, pode conter algumas faltas.)***

> **Não encontrei um 'week plan' referente a data desta daily note! As atividades aqui descritas constam num arquivo excel (que funcionava como uma 'daily notes' prévia, mas que já não existe mais), mas não há um planejamento semanal referente a esta data**

## :rocket: Objetivo
***(Objetivos são programados no planejamento semanal, disponível na na pasta ```week_pln/```).***
- Criar ferramentas do envelope de risco
## :wrench: Atividades
- O método ```setup()``` está pronto e o EPF também! Tudo feito em tempo recorde e com eficiência máxima
## :open_file_folder: Arquivos/notebooks trabalhados
- ```notebooks/risk_envelope/setup_n_epf_sketch.ipynb```
- ```notebooks/risk_envelope/epf.ipynb``` *(criado)*
## :white_check_mark: Resultados
- **EXPLÊNDIDOS!**
- O EPF foi tão extraordinariamente bem sucedido que tive que submetê-lo a uma bateria de testes para saber se não havia um vazamento de dados de alguma coluna do dataset para o modelo de EPF. Os resultados foram negativos! 
## :bookmark_tabs: Observações
- AUC: 0.93 (muito alto! Evidência de estrutura preditiva forte ou de data leaking)
- Executei um script para verificar se há uma única feature no meu dataset que manifesta alta correlação com os resultados da EPF: **NENHUMA!**. Correlação máxima encontrada: 0.559.
- Exacutamos um ```np.mean(y_train_bin)``` para identificarmos um caso de inflação (=0.9) ou deflação (=0.1) do AUC. Resultado: 0.4958. Exatamente na média que queríamos, indicando targets balanceados: 49,58% de retornos positivos e 50,42% de retornos negativos. Perfeitamente equilibrado
- Não há correlação individual alta
- Não há desbalanceamento
- Fizemos um teste final: ```np.random.shuffle(y_train_bin)```
- O comando acima embaralha os targets previstos pelo modelo e retreina o modelo em cima dos targets embaralhados, para anular correlações entre as features e o target, aniquilando padrões reais. Espera-se o resultado mais próximo possível de 0.5
- Nosso resultado foi 0.53
- Dentro da variação esperada para ruído
- Compatível com aleatório
- **SÓ PODE SER NATAL!**, é bom demais pra ser verdade!
## :thought_balloon: Próximos passos
- Finalização do método ```setup()``` de pré-processamento
- Criação do EPF
## versionamento
| Commits | Descrição | Notas | Início/fim | Versão |
| :--- | :---: | :--- | :--- | :--- |
| ? | Iniciação da criação do método ```setup()``` | none | 21h55-indeterminado | ? |


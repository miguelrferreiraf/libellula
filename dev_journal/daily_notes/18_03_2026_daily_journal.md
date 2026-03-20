# :calendar: 22-02-2026 (sunday)
***by: Miguel Ferreira***

> **As atividades deste daily log são relativas ao 'week plan' da semana de 16/03/26 - segunda-feira - até 23/03/26 - segunda feira seguinte**

## :rocket: Objetivo
***(Objetivos são programados no planejamento semanal, disponível na na pasta ```week_pln/```).***
- Criar mais ferramentas do envelope de risco
- Criar um quantile forecasting
## :wrench: Atividades
- O método foi criado mas ainda é necessário algumas calibragens
## :open_file_folder: Arquivos/notebooks trabalhados
- ```notebooks/risk_envelope/quantile_forecasting.ipynb``` *(criado)*
## :white_check_mark: Resultados
- **Ainda não muito animadores**
- Eu separei os quantis em diferentes escalas para mensuração de subestimação e superestimação.
- Os resultados dos quantis foram:
```
Quantile 0.1: 0.000693
Quantile 0.5: 0.001240
Quantile 0.9: 0.000862
```
- Os valores se motraram baixos e consistentes, o que é bom!
- Por causa dos intervalos entre as variáveis, pode-se dizer que o modelo capturou heterocedasticidade.
## :bookmark_tabs: Observações
- Ainda tem muito trabalho pela frente no quantile forecasting
- Usamos um algoritmo de calibração que retornou 0.782 (resultado esperado ~ 0.8)
- Nosso resultado, portanto, foi bastante satisfatório.
## :thought_balloon: Próximos passos
- Terminar de parametrizar o QF! 
- Ou não...
## versionamento
| Commits | Descrição | Notas | Início/fim | Versão |
| :--- | :---: | :--- | :--- | :--- |
| ```creating quantile forecasting``` | Quantile forecasting | Restam apenas algumas parametrizações, mas estou pensando em deixa-las para depois | 22h10-00h00 | ? |


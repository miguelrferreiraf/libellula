# :calendar: 23-04-2026 (thursday)
***by: Miguel Ferreira***

> **Ultimamente não tenho feito planejamentos semanais! Contudo, as coisas tem progredido bem, então não vo me preocupar com isso por agora!**

## :rocket: Objetivo
- Criar finalmente o código de concatenação para todos os datasets (formato '.parquet') criados pelas ferramentas do envelope de risco. 
- Mas, antes de fazer isso, precisamos ter certeza absoluta de que:
1. Os notebooks das ferramentas do envelope estão padronizados
2. Os datasets resultantes estao sincronizados! 
## :wrench: Atividades
- **Nós padronizamos (pela última vez, se Deus quiser) TODOS OS NOTEBOOKS COM AS FERRAMENTAS DO ENVELOPE DE RISCO. Eles não podem ficar mais padronizados (pelo menos no que concerne ao corpo de texto) do que já estão!**
- Uma vez padronizados, eu iniciei a criação do **'código de concatenação'**, e isso é muito importante.
- O **'código de concatenação'** é um script que concatena os datesets em formato '.parquet' gerados pelas *ferramentas do envelope de risco + dataset gerado pelo modelo TFT preditivo*, com o propósito de transformar tudo num só dataset a ser analisado pelo **modelo RL (Reinforcement Learning) de gestão de banca**
- Não sei se a esta altura do campeonato está claro a importância deste fluxo de trabalho, mas:
```
Fluxo:
1. As ferramentas do envelope de risco geram outputs que são features com dados de risco estocástico/probabilístico extraídos do dataset original (cotações OHLC)
2. O modelo TFT preditivo também gera um dataset com previsões
3. Cada uma das ferramentas gera um dataset contendo essas features
4. Um código externo, o **código de concatenação**, junta todos estes datasets (do envelope de risco e do TFT preditivo) num só
5. Este dataset final será usado para treinar o modelo RL de gestão de banca, que é responsável por gerenciar o tamanho das posições no trade e os stops
``` 
## :open_file_folder: Arquivos/notebooks trabalhados
- Olhe o qur fizemos!:
```
├───combined # Datasets concatenados
├───cvar # Contém as features geradas pelo notebook do CVaR
│       cvar_features.parquet # O dataset em questão
│
├───epf # Contém as features geradas pelo notebook do EPF
│       epf_features.parquet
│
├───evt # Contém as features geradas pelo notebook do EVT
│       evt_features.parquet
│
├───pdfd # Contém as features geradas pelo notebook do PDFD
│       pdfd_features.parquet
│
├───predictions # Contém o dataset com as previsões geradas pelo modelo TFT preditivo
└───qf # Contém as features geradas pelo notebook do Quantile Forecasting
        qf_features.parquet
```
- ```C:\projects\Libellula\data\processed\combined\``` *(criado)*
- ```C:\projects\Libellula\data\processed\cvar\``` *(criado)*
- ```C:\projects\Libellula\data\processed\epf\``` *(criado)*
- ```C:\projects\Libellula\data\processed\evt\``` *(criado)*
- ```C:\projects\Libellula\data\processed\pdfd\``` *(criado)*
- ```C:\projects\Libellula\data\processed\predictions\``` *(criado)*
- ```C:\projects\Libellula\data\processed\qf\``` *(criado)*
## :white_check_mark: Resultados
- **Satisfatórios**
## :bookmark_tabs: Observações
- **OS NOTEBOOKS DAS FERRAMENTAS DO ENVELOPE DE RISCO ESTÃO PADRONIZADOS, MAS OS DATASETS CONTENDO AS FEATURES DE RISCO NÃO ESTÃO SINCRONIZADOS!**
 ## :thought_balloon: Próximos passos
- **Para fazer um script de concatenação funcional, precisamos fazer com que os datasets gerados pelas ferramentas do envelope estejam sincronizados**
- Este, portanto, **FICA SENDO O PRÓXIMO PASSO**
- **EU JÁ O COMECEI E JÁ DETECTEI O PRIMIRO ERRO DE SINCRONIZAÇÃO!**
## versionamento
| Commits | Descrição | Notas | Início/fim | Versão |
| :--- | :---: | :--- | :--- | :--- |
| ```adding first parquet datasets to /data/processed/``` | Simplesmente rodei as células de código que transformavam os datasets gerados pelas ferramentas do envelope em arquivos '.parquet' salvos no diretório recém criado | Os arquivos com os datasets foram criados automaticamente | 11h00 - 18h00 | none |
| ```creating concatenation``` | Comecei a criar o código de concatenação, mas ele ainda está testando a sincronização dos datasets gerados pelo envelope | Encontrei um erro de sincronização. Corrijo depois | 11h00 - 18h00 | none |


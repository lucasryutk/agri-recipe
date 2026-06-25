# Objetivo principal
Este repositório tem como objetivo simular um sistema onde ele gera dados não estruturados de informações de receitas agronômicas e organiza em uma arquitetura Medallion - camadas bronze, silver e gold

# Fonte de dados
AgroApi - Api disponibilizada pela Embrapa - https://www.portal.agroapi.cnptia.embrapa.br/

# Estrutura de pastas

```text
agri-recipe/
├── src/
│   ├── main.py              ← orquestrador
│   ├── bronze_pipeline.py
│   ├── silver_pipeline.py
│   └── gold_pipeline.py
├── logs/
│   └── pipeline.log
├── raw/                     ← arquivos brutos
├── medallion/
│   ├── bronze/
│   │   └── .gitkeep
│   ├── silver/
│   │   └── .gitkeep
│   └── gold/
│       └── .gitkeep
├── .gitignore
├── .gitattributes
└── README.md
```

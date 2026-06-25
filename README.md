# Objetivo principal
Este repositório tem como objetivo simular um sistema onde ele gera dados não estruturados de informações de receitas agronômicas e organiza em uma arquitetura Medallion - camadas bronze, silver e gold


# Fonte de dados
AgroApi - Api disponibilizada pela Embrapa - https://www.portal.agroapi.cnptia.embrapa.br/


# Arquitetura Medallion

| 🥉 Bronze | Cópia bruta dos arquivos JSON da API, sem transformação |

| 🥈 Silver | Dados limpos, tipados e validados |

| 🥇 Gold   | Dados agregados e prontos para consumo analítico 


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


# Como executar 
1. Entrar no site  da AgroApi e criar uma chave de acesso

2. Clone o repositório

    git clone git@github.com:lucasryutk/agri-recipe.git

3. Entra na pasta do projeto

    cd agri-recipe

4. Crie um arquivo .env na pasta e salve a chave na variável 

    EMBRAPA_API_KEY = "sua_chave"

5. Crie registros fictícios

    python src/app.py

6. Execute os pipelines de ETL

    python src/main.py


## Autor: Lucas Ryu Takabayashi

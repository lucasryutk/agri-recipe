import logging
from pathlib import Path
from bronze_pipeline import salvar_bronze
from silver_pipeline import salvar_silver
from gold_pipeline import salvar_gold

Path('logs').mkdir(exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('logs/pipelines.logs', encoding='utf-8')
    ]
)

logging.getLogger(__name__)

def executar_pipeline():
    logging.info('='*50)
    logging.info('EXECUTANDO PIPELINE')
    logging.info('='*50)

    try:
        logging.info('ETAPA 1: BRONZE')
        salvar_bronze()

        logging.info('ETAPA 2: SILVER')
        salvar_silver()

        logging.info('ETAPA 3: GOLD')
        salvar_gold()

        logging.info('='*50)
        logging.info('PIPELINE CONCLUÍDO')
        logging.info('='*50)

    except Exception as e:
        logging.error(f'PIPELINE COM ERRO NA ETAPA {e}')
        raise

if __name__ == 'main.py':
    executar_pipeline()
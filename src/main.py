import logging
import time
from pathlib import Path

Path('logs').mkdir(exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format= '%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('logs/main', encoding='utf-8')
    ]
)
logging.getLogger("numexpr").setLevel(logging.WARNING)

from bronze_pipeline import salvar_bronze
from silver_pipeline import salvar_silver
from gold_pipeline import salvar_gold

logger = logging.getLogger(__name__)

def executar_pipeline():
    logging.info('='*50)
    logging.info('EXECUTANDO PIPELINE'.center(50))
    logging.info('='*50)
    time.sleep(2.5)

    try:
        logging.info('ETAPA 1: BRONZE')
        time.sleep(2.5)
        salvar_bronze()

        logging.info('ETAPA 2: SILVER')
        time.sleep(2.5)
        salvar_silver()

        logging.info('ETAPA 3: GOLD')
        time.sleep(2.5)
        salvar_gold()

        time.sleep(2.5)
        logging.info('='*50)
        logging.info('PIPELINE CONCLUÍDO'.center(50))
        logging.info('='*50)

    except Exception as e:
        logging.error(f'PIPELINE COM ERRO NA ETAPA {e}')
        raise

if __name__ == '__main__':
    executar_pipeline()
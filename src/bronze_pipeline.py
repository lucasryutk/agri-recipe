import shutil
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),                        
        logging.FileHandler(f'logs/bronze_stage_logs.logs', encoding='utf-8')  
    ]
)

logger = logging.getLogger(__name__)


def copiar_colar(origem, destino):
    origem = Path(origem)
    destino = Path(destino)

    logger.info(f'Iniciando cópía de arquivos de {origem} para {destino}')
    try:
        arquivos = list(origem.rglob('*'))
        contagem = len(arquivos)
        logger.info(f'{contagem} arquivos encontrados')
        destino.mkdir(parents=True, exist_ok=True)
        shutil.copytree(str(origem), str(destino), dirs_exist_ok=True)
        logger.info(f'Concluído: {contagem} arquivos copiados para {destino}')

    except Exception as e:
        logger.info(f'Erro ao copiar dados de {origem} para {destino}', exc_info=True)
        raise

copiar_colar('raw', 'medallion/bronze')

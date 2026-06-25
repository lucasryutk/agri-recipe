import shutil
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent 

logger = logging.getLogger(__name__)


def salvar_bronze():
    origem = BASE_DIR / 'raw'
    destino = BASE_DIR / 'medallion' / 'bronze'

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
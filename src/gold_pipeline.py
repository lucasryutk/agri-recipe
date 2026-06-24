from pathlib import Path
import pandas as pd
import logging
import json

BASE_DIR = Path(__file__).resolve().parent.parent  
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_DIR / 'gold_stage.log', encoding='utf-8')
    ]
)

logger = logging.getLogger(__name__)

def ler_silver(path):
    data = []
    p = Path(str(path))
    files = [i for i in p.glob('*.json')]
    for i in files:
        with open(i, encoding='utf-8') as file:
            data_json = json.load(file)
            data.extend(data_json)
    return data

def transformar_em_df(path):
    data = ler_silver(path)
    df = pd.json_normalize(
        data,
        record_path='recipe',
        meta=['data', 'id_cliente']
    )
    return df

def aplicacao_por_cultura():
    p_origem = BASE_DIR / 'medallion' / 'silver'
    df = transformar_em_df(p_origem)
    p_destino = BASE_DIR / 'medallion' / 'gold'
    path_json = p_destino / 'dosagem_por_marca.json'
    df_cultura = df.groupby('cultura')['dosagem'].agg('sum').sort_values(ascending=False)
    df_cultura.to_json(path_json, force_ascii=False ,indent=2)
    logging.info('Gerado relatório de cultura com sucesso!')

def aplicacao_por_marca():
    p_origem = BASE_DIR / 'medallion' / 'silver'
    df = transformar_em_df(p_origem)
    p_destino = BASE_DIR / 'medallion' / 'gold'
    path_json = p_destino / 'dosagem_por_marca.json'
    df_cultura = df.groupby('marca_comercial')['dosagem'].agg('sum').sort_values(ascending=False)
    df_cultura.to_json(path_json, force_ascii=False ,indent=2)
    logging.info('Gerado relatório de marca com sucesso!')

def salvar_gold():
    aplicacao_por_cultura()
    aplicacao_por_marca()
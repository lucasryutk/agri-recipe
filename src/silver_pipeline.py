import logging
import json
import re
from datetime import datetime 
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),                        
        logging.FileHandler(f'logs/silver_stage_logs.logs', encoding='utf-8')  
    ]
)

logger = logging.getLogger(__name__)


def limpeza(data: dict): 
    tratado = {
        'id': data['id'],
        'data': data['date'][:10],
        'id_cliente': data['client_id'],
        'recipe':
            [{
                'marca_comercial': i['marca_comercial'].capitalize(),
                'ingrediente_ativo': i['ingrediente_ativo'].capitalize(),
                'formulacao': i['formulacao'].strip(),
                'tecnica': i['tecnica'].capitalize(),
                'cultura': i['cultura'].capitalize(),
                'praga': re.sub(r'\s+', ' ',i['praga'].strip().replace('-', ' ')).capitalize(),
                'dosagem': i['dosagem']
            } for i in data['recipe']
            ]
    }
    return tratado


def ler_bronze():
    data = []
    p = Path('medallion/bronze')
    files = [f for f in p.glob('*') if f.name != '.gitkeep']
    for i in files:
        with open(i, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            data_clean = limpeza(json_data)
            data.append(data_clean)
    return data

def salvar_silver():
    data = ler_bronze('medallion/bronze')
    p = Path('medallion/silver')
    p.mkdir(parents=True, exist_ok=True)

    file_path = p / f'{datetime.today().strftime('%Y-%m-%d')}.json'
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

salvar_silver()
import numpy as np
import os
import requests
import uuid
import json
import logging
from time import sleep
from datetime import datetime, timezone
from dotenv import load_dotenv  
from pathlib import Path 

path = Path(__file__).parent.parent
interval = 5

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),                        
        logging.FileHandler(f'{path}/logs/generating.logs', encoding='utf-8')  
    ]
)

logger = logging.getLogger(__name__)

load_dotenv()

api_key = os.getenv('EMBRAPA_API_KEY')
url = 'https://api.cnptia.embrapa.br/agrofit/v1'
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
}

registros = ['culturas','tecnicas-aplicacoes','formulacoes','marcas-comerciais','pragas-nomes-comuns', 'ingredientes-ativos']

resultados = {endpoint: [] for endpoint in registros}

for endpoint in registros:
    count = 1
    while True:
        response = requests.get(
            url + f'/{endpoint}?page={count}',
            headers=headers
        )

        data = response.json()

        if not data:
            break

        resultados[endpoint].extend(data)
        count += 1

culturas = [i['nome'] for i in resultados['culturas']]
tecnicas = [i['nome'] for i in resultados['tecnicas-aplicacoes']]
formulacoes = [i['nome'] for i in resultados['formulacoes']]
marcas = [i['nome'] for i in resultados['marcas-comerciais']]
pragas = [i['nome'] for i in resultados['pragas-nomes-comuns']]
ingredientes_ativos = [i['nome_comum'] for i in resultados['ingredientes-ativos']]

def generate_recipe():
    num = np.random.randint(1, 5)
    
    return {
        'id': str(uuid.uuid4()),
        'date': datetime.now(timezone.utc).isoformat(),
        'client_id': np.random.randint(1, 999),
        'recipe':[
            {
                'marca_comercial': str(np.random.choice(marcas)),
                'ingrediente_ativo': str(np.random.choice(ingredientes_ativos)),
                'formulacao': str(np.random.choice(formulacoes)),
                'tecnica': str(np.random.choice(tecnicas)),
                'cultura': str(np.random.choice(culturas)),
                'praga': str(np.random.choice(pragas)),
                'dosagem': int(np.random.choice(range(5, 201, 5)))
            }

            for _ in range(num)
        ]

    }

def export_recipe(recipe):
    recipe_id = recipe['id']
    file_name = f'recipe_{recipe_id}'
    json_content = json.dumps(recipe, indent=2, ensure_ascii=False)
    (path/'raw').mkdir(exist_ok=True)
    (path/'raw'/file_name).write_text(json_content, encoding="utf-8")

    return file_name

def main():
    logger.info(f'Criando registros de receitas agronômicas a cada {interval} segundos - Use Ctrl + C para interromper os registros')
    sleep(3)
    while True:
        recipe = generate_recipe()
        recipe_name = export_recipe(recipe)
        logger.info(f'Gerando a receita de id: {recipe_name}')

        sleep(interval)

if __name__ == '__main__':
    main()
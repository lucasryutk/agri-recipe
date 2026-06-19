import shutil
import logging
import json
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

p = Path('medallion/bronze')

files = list(p.glob('*'))

print(files[0])

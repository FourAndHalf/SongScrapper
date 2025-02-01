import yaml
import logging
import os

logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("song_scrapper.log"),
        logging.StreamHandler()
    ]
)

def load_admin_config(key):
    """
    Load admin configuration from the YAML file.
    """

    file_name = 'admin_config.yaml'

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CONFIG_PATH = os.path.join(BASE_DIR, 'config', file_name)
    
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Configuration file not found: {CONFIG_PATH}")
    
    with open(CONFIG_PATH, 'r') as file:
        file = yaml.safe_load(file)
    
    value = file['settings'][key]
    
    
import yaml
import os
from SpotifyDownloader.logging_config import logger

def load_admin_config(key):
    """
    Load admin configuration from the YAML file.
    """

    logger.info(f"Looking to load configuration value for key: {key}")

    file_name = 'admin_config.yaml'

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CONFIG_PATH = os.path.join(BASE_DIR, file_name)

    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Configuration file not found: {CONFIG_PATH}")

    with open(CONFIG_PATH, 'r') as file:
        file = yaml.safe_load(file)

    if value := file['settings'][key]:
        return value
    else:
        raise ValueError(f"Configuration value not found for: {key}")
    
    
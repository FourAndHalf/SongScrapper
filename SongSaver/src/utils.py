import yaml
import os

def load_config(file_name = 'admin_config.yaml'):
    """
    Load admin configuration from the YAML file.
    """
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CONFIG_PATH = os.path.join(BASE_DIR, 'config', file_name)
    
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Configuration file not found: {CONFIG_PATH}")
    
    with open(CONFIG_PATH, 'r') as file:
        return yaml.safe_load(file)
    
def check_environment(config):
    """
    Validate the environment in the configuration.
    """

    environment = config['settings']['environment']
    return environment    
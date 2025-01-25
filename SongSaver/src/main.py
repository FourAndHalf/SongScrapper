from src.utils import load_config

config = load_config()

api_key = config['api']['api-key']
rate_limit = config['settings']['rate_limit']
environment = config['settings']['environment']

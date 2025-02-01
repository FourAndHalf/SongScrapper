import asyncpg
import asyncio
import logging
import pyyaml
from .src.utils import load_admin_config

logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("song_scrapper.log"),
        logging.StreamHandler()
    ]
)

async def connect_db():
    try:
        logging.info("Attempting to connect to the Neon.Tech Database....")

        conn = await asyncpg.connect(
            database = "",
            user = "",
            password = "",
            host = "",
            port = "5432"
        )
        
    except Exception as ex:
        logging.error(msg= 'Error occured on db connection :{ex}')
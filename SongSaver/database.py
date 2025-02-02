import asyncpg
import asyncio
import logging
import os
import dj_database_url
from urllib.parse import urlparse

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

        database_url = dj_database_url.config(default = os.getenv("DATABASE_URL"))

        if not database_url:
            logging.error("Database url is missing in environment file")
            raise ValueError("Database url is missing in environment file")
        
        parsed_url = urlparse(database_url)
                        
        conn = await asyncpg.connect(
            database = parsed_url.path.lstrip("/"),
            user = parsed_url.username,
            password = parsed_url.password,
            host = parsed_url.hostname,
            port = parsed_url.port,
        )
        
        logging.info("Successfully connected to database")
        
    except Exception as ex:
        logging.error(f'Error occurred on db connection :{ex}')
        return None
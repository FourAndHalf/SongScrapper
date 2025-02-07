import asyncpg
import asyncio
import os
import dj_database_url
from urllib.parse import urlparse
from SpotifyDownloader.logging_config import logger

async def connect_db():
    try:
        logger.info("Attempting to connect to the Neon.Tech Database....")

        database_url = dj_database_url.config(default = os.getenv("DATABASE_URL"))

        if not database_url:
            logger.error("Database url is missing in environment file")
            raise ValueError("Database url is missing in environment file")
        
        parsed_url = urlparse(database_url)
                        
        conn = await asyncpg.connect(
            database = parsed_url.path.lstrip("/"),
            user = parsed_url.username,
            password = parsed_url.password,
            host = parsed_url.hostname,
            port = parsed_url.port,
        )
        
        logger.info("Successfully connected to database")
        
    except Exception as ex:
        logger.error(f'Error occurred on db connection :{ex}')
        return None
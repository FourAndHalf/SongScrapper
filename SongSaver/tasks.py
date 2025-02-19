from celery import shared_task
from .src.utils.validators import is_spotify_url, is_youtube_url
from .src.youtube.youtube import download_song_from_youtube
from .src.spotify.spotify import get_spotify_data
from SpotifyDownloader.logging_config import logger

@shared_task(bind=True)
def process_playlist(self, data):
    """ Process the link provided without storing it in a database """

    try:
        link = data.get('link')

        if is_youtube_url(link):
            logger.info(f"Processing youtube link: {link}")
            download_song_from_youtube.delay(link)
            return {"status": "processing", "error": "YouTube"}
        elif is_spotify_url(link):
            logger.info(f"Processing spotify link: {link}")
            print('boom')
            return {"status": "processing", "error": "Spotify"}
        else:
            logger.warning(f"Invalid link provided: {link}")
            return {"status": "failed", "error": "Invalid URL"}

    except Exception as ex:
        logger.error(f"Error processing playlist: {str(ex)}", exc_info=True)
        return {"status": "failed", "error": str(ex)}

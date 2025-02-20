import re
from celery import shared_task
from .src.utils.validators import is_spotify_url, is_youtube_url
from .src.youtube.youtube import download_song_from_youtube_link, download_song_from_youtube_search
from .src.spotify.spotify import get_spotify_data
from SpotifyDownloader.logging_config import logger

@shared_task(bind=True)
def process_playlist(self, data):
    """ Process the link provided without storing it in a database """

    try:
        link = data

        if is_youtube_url(link):
            logger.info(f"Processing youtube link: {link}")
            download_song_from_youtube_link.delay(link)
            return {"status": "processing", "source": "YouTube"}
        elif is_spotify_url(link):
            logger.info(f"Processing spotify link: {link}")
            tracks = get_spotify_data(link)

            if not tracks:
                logger.warning(f"No tracks found for spotify link: {link}")
                return {"status": "failed", "error": "No tracks found"}

            if tracks[0]["type"] == "track":
                song_name = tracks["title"]
                song_name = re.sub(r'[^\w\s]', '', song_name).strip()
                artist = tracks["artist"]

                download_song_from_youtube_search.delay(song_name, artist)
            elif tracks[0]["type"] in ["playlist", "album"]:
                for track in tracks:
                    song_name = track["title"]
                    song_name = re.sub(r'[^\w\s]', '', song_name).strip()
                    artist = track["artist"]

                    download_song_from_youtube_search.delay(song_name, artist)
            return {"status": "processing", "source": "Spotify"}

        else:
            logger.warning(f"Invalid link provided: {link}")
            return {"status": "failed", "error": "Invalid URL"}

    except Exception as ex:
        logger.error(f"Error processing playlist: {str(ex)}", exc_info=True)
        return {"status": "failed", "error": str(ex)}

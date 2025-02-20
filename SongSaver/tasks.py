import re
from celery import shared_task
from .src.utils.validators import is_spotify_url, is_youtube_url
from .src.youtube.youtube import download_song_from_youtube_link, download_song_from_youtube_search
from .src.spotify.spotify import get_spotify_track_data, get_spotify_playlist_data, get_spotify_album_data
from SpotifyDownloader.logging_config import logger

@shared_task(bind=True)
def process_playlist(self, data):
    """ Process the link provided without storing it in a database """

    try:
        SPOTIFY_URL_PATTERN = re.compile(r"https?://open\.spotify\.com/(track|playlist|album)/([a-zA-Z0-9]+)")

        if is_youtube_url(data):
            logger.info(f"Processing youtube link: {data}")
            download_song_from_youtube_link.delay(data)
            return {"status": "processing", "source": "YouTube"}
        elif is_spotify_url(data):
            logger.info(f"Processing spotify link: {data}")
            match = SPOTIFY_URL_PATTERN.match(data)
            item_type, item_id = match.groups()
            
            if item_type == "track":
                track = get_spotify_track_data(item_id)

                if not track:
                    logger.warning(f"No tracks found for spotify link: {data}")
                    return {"status": "failed", "error": "No tracks found"}

                song_name = track["title"]
                song_name = re.sub(r'[^\w\s]', '', song_name).strip()
                artist = track["artist"]

                download_song_from_youtube_search.delay(song_name, artist)

            elif item_type == "playlist":
                tracks = get_spotify_playlist_data(item_id)
                for track in tracks:
                    song_name = track["title"]
                    song_name = re.sub(r'[^\w\s]', '', song_name).strip()
                    artist = track["artist"]

                    download_song_from_youtube_search.delay(song_name, artist)

            elif item_type == "album":
                tracks = get_spotify_album_data(item_id)
                for track in tracks:
                    song_name = track["title"]
                    song_name = re.sub(r'[^\w\s]', '', song_name).strip()
                    artist = track["artist"]
                    download_song_from_youtube_search.delay(song_name, artist)

            return {"status": "processing", "source": "Spotify"}

        else:
            logger.warning(f"Invalid link provided: {data}")
            return {"status": "failed", "error": "Invalid URL"}

    except Exception as ex:
        logger.error(f"Error processing playlist: {str(ex)}", exc_info=True)
        return {"status": "failed", "error": str(ex)}

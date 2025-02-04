from SpotifyDownloader.logging_config import logger
from src.utils.utils import load_admin_config
from src.spotify.spotify import get_spotify_data
from src.youtube.youtube import download_song_from_youtube

api_key = load_admin_config('api_key')
rate_limit = load_admin_config('rate_limit')
environment = load_admin_config('environment')

url = ""

logger.info("Before Processing Spotify Url")

tracks = get_spotify_data(url)

logger.info("After Processing Spotify Url")

if tracks is None:
    logger.error("No data returned. Check if Spotify API credentials are correct.")
elif "error" in tracks:
    logger.error(f"Error occurred: {tracks['error']}")
else:
    logger.info("Successfully fetched Spotify data.")

    for track in tracks:
        song_name = track.get("title")
        artist = track.get("artist")

        if song_name and artist:
            logger.info(f"Downloading: {song_name} - {artist}")
            if file_name := download_song_from_youtube(song_name, artist):
                logger.info(f"Downloaded Successfully: {file_name}")
            else:
                logger.error(f"Failed to download: {song_name} - {artist}")

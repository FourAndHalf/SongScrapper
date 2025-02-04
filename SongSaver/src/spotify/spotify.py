import spotipy
import re
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
from SpotifyDownloader.logging_config import logger
from utils.validators import is_spotify_url

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
    )
)

SPOTIFY_URL_PATTERN = re.compile(r"https?://open\.spotify\.com/(track|playlist)/([a-zA-Z0-9]+)")

def get_spotify_data(url):
    """     Determine url is a playlist / track and behave accordingly      """

    tracks = []
    song_count = 0    

    if not is_spotify_url(url):
        logger.warning(f"Invalid spotify url provided: {url}")
        return {"error": "Invalid Spotify URL. Only track and playlist URLs are supported."}
    
    try:
        logger.info(f"Before starting matching url data: {url}")

        match = SPOTIFY_URL_PATTERN.match(url)
        item_type, item_id = match.groups()
        
        if item_type == "track":
            try:
                logger.info("Before fetching track data...")

                tracks = get_track_info(item_id)

            except Exception as ex:
                logger.error(f"Failed to fetch track details: {ex}")
                return {"error": "Failed to fetch track details"}

        elif item_type == "playlist":
            try: 
                logger.info("Before fetching playlist track data...")

                playlist = sp.playlist_tracks(item_id)

                for item in playlist["items"]:
                    track = item["track"]
                    tracks.append(get_track_info(track))

            except Exception as ex:
                logger.error(f"Failed to fetch track details: {ex}")
                return {"error": "Failed to fetch track details"}

        return tracks
    
    except Exception as ex:
        logger.error(f"Error occurred while fetching spotify details: {ex}")
        return None

def get_track_info(track_id):
    """     Fetch track details from spotify url      """

    logger.info(f"Before starting fetching track details from spotify track id: {track_id}")

    try:
        track = sp.track(track_id)

        return {
            "type": "track",
            "title": track["name"],
            "artist": track["artists"][0]["name"],
            "album": track["album"]["name"],
            "release_date": track["album"]["release_date"],
            "spotify_url": track["external_urls"]["spotify"]
        }
    except Exception as ex:
        logger.error(f"Error occurred while fetching track id ({track_id}) details: {ex}")
        return None


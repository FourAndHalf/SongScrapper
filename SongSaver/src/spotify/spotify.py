import os
import re
import spotipy
from celery import shared_task
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from SpotifyDownloader.logging_config import logger
from ..utils.validators import is_spotify_url

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
    )
)

SPOTIFY_URL_PATTERN = re.compile(r"https?://open\.spotify\.com/(track|playlist|album)/([a-zA-Z0-9]+)")

@shared_task
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

                track_dtl = sp.track(item_id)

                track = {
                    "type": "track",
                    "title": track_dtl["name"],
                    "artist": track_dtl["artists"][0]["name"],
                    "album": track_dtl["album"]["name"],
                    "release_date": track_dtl["album"]["release_date"],
                    "spotify_url": track_dtl["external_urls"]["spotify"]
                }

                tracks.append(track)

            except Exception as ex:
                logger.error(f"Failed to fetch track details: {ex}")
                return {"error": "Failed to fetch track details"}

        elif item_type == "playlist":
            try: 
                logger.info("Before fetching playlist track data...")

                playlist = sp.playlist_tracks(item_id)

                for item in playlist["items"]:
                    track = item["track"]
                    track_dtl = sp.track(track["id"])

                    track = {
                        "type": "playlist",
                        "title": track_dtl["name"],
                        "artist": track_dtl["artists"][0]["name"],
                        "album": track_dtl["album"]["name"],
                        "release_date": track_dtl["album"]["release_date"],
                        "spotify_url": track_dtl["external_urls"]["spotify"]
                    }

                    tracks.append(track)

            except Exception as ex:
                logger.error(f"Failed to fetch playlist details: {ex}")
                return {"error": "Failed to fetch playlist details"}

        elif item_type == "album":
            try: 
                logger.info("Before fetching album track data...")

                album = sp.album_tracks(item_id)

                for item in album["items"]:
                    track = item["track"]
                    track_dtl = sp.track(track["id"])

                    track = {
                        "type": "album",
                        "title": track_dtl["name"],
                        "artist": track_dtl["artists"][0]["name"],
                        "album": track_dtl["album"]["name"],
                        "release_date": track_dtl["album"]["release_date"],
                        "spotify_url": track_dtl["external_urls"]["spotify"]
                    }

                    tracks.append(track)

            except Exception as ex:
                logger.error(f"Failed to fetch album details: {ex}")
                return {"error": "Failed to fetch album details"}

        return tracks
    
    except Exception as ex:
        logger.error(f"Error occurred while fetching spotify details: {ex}")
        return None


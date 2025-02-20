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


@shared_task
def get_spotify_track_data(track_id):
    """     Get Track Data      """

    try:
        logger.info("Before fetching track data...")

        track_dtl = sp.track(track_id)

        return {
            "type": "track",
            "title": track_dtl["name"],
            "artist": track_dtl["artists"][0]["name"],
            "album": track_dtl["album"]["name"],
            "release_date": track_dtl["album"]["release_date"],
            "spotify_url": track_dtl["external_urls"]["spotify"]
        }

    except Exception as ex:
        logger.error(f"Failed to fetch track details: {ex}")
        return {"error": "Failed to fetch track details"}

@shared_task
def get_spotify_playlist_data(playlist_id):
    try: 
        logger.info("Before fetching playlist track data...")

        tracks = []
        playlist = sp.playlist_tracks(playlist_id)

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
        
        return tracks

    except Exception as ex:
        logger.error(f"Failed to fetch playlist details: {ex}")
        return {"error": "Failed to fetch playlist details"}

@shared_task
def get_spotify_album_data(album_id):
    try: 
        logger.info("Before fetching album track data...")

        tracks = []
        album = sp.album_tracks(album_id)

        for item in album["items"]:
            track_id = item["id"]
            track_dtl = sp.track(track_id)

            track = {
                "type": "playlist",
                "title": track_dtl["name"],
                "artist": track_dtl["artists"][0]["name"],
                "album": track_dtl["album"]["name"],
                "release_date": track_dtl["album"]["release_date"],
                "spotify_url": track_dtl["external_urls"]["spotify"]
            }

            tracks.append(track)

        return tracks

    except Exception as ex:
        logger.error(f"Failed to fetch album details: {ex}")
        return {"error": "Failed to fetch album details"}


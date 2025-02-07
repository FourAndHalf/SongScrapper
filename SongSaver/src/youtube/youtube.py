import yt_dlp
import sys
import os
from pathlib import Path
from SpotifyDownloader.logging_config import logger

def get_download_folder():
    """Determine the appropriate Downloads folder path based on the OS."""
    
    if sys.platform.startswith("win"):  # Windows
        download_path = Path.home() / "Downloads"
    
    elif sys.platform.startswith("darwin"):  # macOS
        download_path = Path.home() / "Downloads"
    
    elif sys.platform.startswith("linux"):  # Linux / Android
        if "ANDROID_ROOT" in os.environ:
            download_path = Path("/storage/emulated/0/Download")  # Android downloads folder
        else:
            download_path = Path.home() / "Downloads"
    
    else:
        raise Exception("Unsupported OS")
    
    music_path = download_path / "Music"
    music_path.mkdir(parents=True, exist_ok=True)
    
    return music_path

def download_song_from_youtube(song_name, artist):
    """      Download an MP3 file of the song from YouTube.      """

    logger.info(f"Before setting search query for track: {song_name} - {artist}")

    try:
        return download_song_from_youtube_snippet(song_name, artist)
    except Exception as ex:
        logger.error(f"Error downloading from YouTube: {ex}")
        return None


def download_song_from_youtube_snippet(song_name, artist):
    search_query = f"{song_name} {artist} official audio"
    download_folder = get_download_folder()
    
    output_path = download_folder/f"{song_name} - {artist}.%(ext)s"

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': str(output_path),
    }

    logger.info(f"Before starting downloading track: {search_query}")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{search_query}"])

    logger.info(f"After downloading track: {output_path.with_suffix('.mp3')}")

    return str(output_path.with_suffix('.mp3'))

import yt_dlp
import sys
import os
from celery import shared_task
from pathlib import Path
from SpotifyDownloader.logging_config import logger

@shared_task
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

@shared_task
def download_song_from_youtube_link(link):
    """      Download an MP3 file of the song using YouTube Link      """

    logger.info(f"Before downloading track with youtube link: {link}")

    try:
        return download_song_from_youtube_link(link)
    except Exception as ex:
        logger.error(f"Error downloading from YouTube: {ex}")
        return None

@shared_task
def download_song_from_youtube_search(song_name, artist):
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
        'quiet': True,
        'no_warnings': True,
        'extract_flat': 'in_playlist',
        'socket_timeout': 30,
        'retries': 3,
        'nocheckcertificate': True,
        'extractor_args': {
            'youtube': {
                'skip': ['dash', 'hls'],
                'player_client': ['android', 'web'],
            }
        },
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate',
        }
    }

    logger.info(f"Before starting downloading track: {search_query}")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{search_query}"])

    logger.info(f"After downloading track: {output_path.with_suffix('.mp3')}")

    return str(output_path.with_suffix('.mp3'))

@shared_task
def download_song_from_youtube_link(link):
    download_folder = get_download_folder()
    
    output_path = download_folder/"%(title)s.%(ext)s"

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': str(output_path),
        'quiet': True,
        'no_warnings': True,
        'extract_flat': 'in_playlist',
        'socket_timeout': 30,
        'retries': 3,
        'nocheckcertificate': True,
        'extractor_args': {
            'youtube': {
                'skip': ['dash', 'hls'],
                'player_client': ['android', 'web'],
            }
        },
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate',
        }
    }

    logger.info(f"Before starting downloading track: {link}")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    info = ydl.extract_info(link, download=False)
    downloaded_file = download_folder / f"{info['title']}.mp3"


    logger.info(f"After downloading track: {downloaded_file}")

    return str(downloaded_file)
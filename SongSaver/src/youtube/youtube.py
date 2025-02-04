import yt_dlp
from SpotifyDownloader.logging_config import logger

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
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': f"downloads/music/{song_name} - {artist}.%(ext)s",
    }

    logger.info(f"Before starting downloading track: {search_query}")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{search_query}"])

    logger.info(f"After downloading track: {song_name} - {artist}.mp3")

    return f"{song_name} - {artist}.mp3"

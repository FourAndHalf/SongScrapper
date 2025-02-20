import re

def is_spotify_url(url):
    return bool(re.match(r'https?://open\.spotify\.com/(track|playlist|album)/[a-zA-Z0-9]+', url))

def is_youtube_url(url):
    return bool(re.match(r'https?://(www\.)?(youtube\.com|youtu\.be)/', url))

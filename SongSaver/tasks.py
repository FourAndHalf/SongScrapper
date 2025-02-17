from celery import shared_task
from .src.utils.validators import is_spotify_url, is_youtube_url

@shared_task
def process_playlist(data):
    """ Process the link provided without storing it in a database """

    link = data.get('link')

    if is_youtube_url(link):
        print('lmao') 
    elif is_spotify_url(link):
        print('boom')
    else:
        print('hurray')
        
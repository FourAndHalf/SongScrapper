from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import re

def startup_page(request):
    return render(request, 'SongSaver/link.html')

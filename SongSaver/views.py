import pretty_errors

from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from .forms import SpotifyLinkForm
from .models import Playlist

pretty_errors.configure(
    filename_display=pretty_errors.FILENAME_EXTENDED,
    line_number_first=True,
    display_link=True,
    lines_before=2,
    lines_after=2,
    code_color='yellow',
)

def startup_page(request):
    return render(request, 'SongSaver/link.html')

def create_playlist(request):
    if request.method == 'POST':
        form = SpotifyLinkForm(request.POST)
        if form.is_valid():
            post_data(form)
            return redirect('LinkListing')
    else:
        form = SpotifyLinkForm()

    return render(request, "SongSaver/link.html", {'form': form})


def post_data(form):
    playlist = form.save(commit=True)
    playlist.created_by = "JINSON"
    playlist.created_at = now()
    playlist.save()
    form.save_m2m()

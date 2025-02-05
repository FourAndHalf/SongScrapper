import pretty_errors

from django.db import connection
from django import forms
from .models import Playlist, Artist, Genre
from src.database.queries.codes_manager import fetch_artists, fetch_genres
from .src.utils.utils import load_admin_config

environment = load_admin_config('environment')

if environment == "TEST":
    pretty_errors.configure(
        filename_display=pretty_errors.FILENAME_EXTENDED,
        line_number_first=True,
        display_link=True,
        lines_before=2,
        lines_after=2,
        code_color='yellow',
    )

artists = fetch_artists()
genres = fetch_genres()



class SpotifyLinkForm(forms.ModelForm):
    curated_artists = forms.ChoiceField(
        choices=list(artists),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=True,
    )
    genre = forms.ChoiceField(
        choices=list(genres),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=True,
    )


class Meta:
    model = Playlist
    fields = [ 'link', 'playlist_name', 'curated_artists', 'genre', 'songs_count' ]

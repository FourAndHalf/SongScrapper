import pretty_errors

from django import forms
from .models import Playlist, Artist, Genre
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

class SpotifyLinkForm(forms.ModelForm):
    curated_artists = forms.ModelMultipleChoiceField(
        queryset=Artist.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

class Meta:
    model = Playlist
    fields = [ 'link', 'playlist_name', 'curated_artists', 'genre', 'songs_count' ]

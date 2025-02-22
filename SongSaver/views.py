#region Declarations

import pretty_errors

from django.shortcuts import render
from .forms import SpotifyLinkForm
from .src.utils.utils import load_admin_config
from .tasks import process_playlist

#endregion

#region Configuration

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

#endregion

#region Define Pages

def startup_page(request):
    return render(request, 'loader.html')

def dashboard_page(request):
    return render(request, 'dashboard.html')

def listing_page(request):
    return render(request, 'listing.html')

def fav_listing_page(request):
    return render(request, 'fav_listing.html')

def create_link_page(request):
    return render_create_link(request)

#endregion

def render_create_link(request):
    if request.method == 'POST':
        form = SpotifyLinkForm(request.POST)

        if form.is_valid():
            link = form.cleaned_data["link"]
            playlist_post(form)

    else:
        form = SpotifyLinkForm()

    return render(request, 'link.html', {'form': form})


def playlist_post(form):
    data = form.cleaned_data['link']

    process_playlist(data)
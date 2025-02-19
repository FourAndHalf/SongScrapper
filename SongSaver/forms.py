#region Declaration

import pretty_errors

from django import forms
from .src.utils.utils import load_admin_config

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

class SpotifyLinkForm(forms.Form):
    link = forms.URLField(label="Spotify Link", required=True)

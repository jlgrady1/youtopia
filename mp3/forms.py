import logging
from django import forms


LOGGER = logging.getLogger(__name__)


class YouTubeURLForm(forms.Form):
    url_attrs = {
        'placeholder': 'https://www.youtube.com/watch?v=<videoid>',
        'class': 'form-control'
    }

    youtube_url = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs=url_attrs),
        error_messages={'required': 'URL is required'}
    )

    def clean_youtube_url(self):
        url = self.data['youtube_url']
        LOGGER.debug("cleaned data", url)
        # https://www.youtube.com/watch?v=<videoid>
        if 'youtube.com/watch?v=' not in url:
            raise forms.ValidationError("Unknown youtube url.")

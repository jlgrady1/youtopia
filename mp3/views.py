import logging
import os
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils.encoding import smart_str
from django.views.static import serve
from wsgiref.util import FileWrapper

from mp3.forms import YouTubeURLForm
from mp3.youtube import YouTubeDownloader

LOGGER = logging.getLogger(__name__)


def index(request):
    context = {}
    LOGGER.debug("index")
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        LOGGER.debug("Submitted")
        # create a form instance and populate it with data from the request:
        form = YouTubeURLForm(request.POST)
        LOGGER.debug("Submitted form {}".format(form))
        # check whether it's valid:
        if form.is_valid():
            f = form.cleaned_data
            LOGGER.debug("form {}".format(f))
            url = f['youtube_url']
            LOGGER.debug("is_valid: {}".format(url))
            ydl = YouTubeDownloader(url)
            filename = ydl.fetch()
            static_path = '/youtube/{}'.format(filename)

            response = HttpResponseRedirect(static_path, content_type='application/force-download')
            return response
        else:
            LOGGER.debug("Invalid form")

    # if a GET (or any other method) we'll create a blank form
    form = YouTubeURLForm()
    context['form'] = form

    return render(request, 'mp3/index.j2', context)

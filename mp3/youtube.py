import logging
from subprocess import getoutput

DOWNLOADER = 'fake_serve'
LOGGER = logging.getLogger(__name__)


class YouTubeDownloader(object):
    def __init__(self, url):
        self.url = url
        # self.validate_url()

    def fetch(self):
        fullpath = getoutput(DOWNLOADER)
        filename = fullpath.split('/')[-1]
        LOGGER.debug('filename', filename, 'fullpath', fullpath)
        return filename, fullpath

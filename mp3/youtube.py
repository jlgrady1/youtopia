import logging
import os
import re
from subprocess import getoutput


LOGGER = logging.getLogger(__name__)

EXISTS = re.compile('\[download\] (.*?) has already been downloaded')
NEW = re.compile('\[ffmpeg\] Destination: (.*)')
MEDIA_HOME = os.environ.get("MEDIA_HOME", '/youtube')


class YouTubeDownloader(object):
    def __init__(self, url):
        self.url = url

    def fetch(self):
        cmd = 'youtube-dl --extract-audio --audio-format mp3 -o "/{}/%(title)s.tmp" {}'.format(
            MEDIA_HOME,
            self.url
        )
        output = getoutput(cmd)
        lines = output.split('\n')
        if len(lines) < 3:
            LOGGER.error("Error downloading file")
            return None, None
        fullpath = ''
        for line in lines:
            LOGGER.debug("youtube-dl: {}".format(line))
            if EXISTS.match(line):
                fullpath = EXISTS.match(line).groups()[0]
            elif NEW.match(line):
                fullpath = NEW.match(line).groups()[0]
        filename = fullpath.split('/')[-1]
        LOGGER.debug("Sending file: {}".format(filename))
        return filename

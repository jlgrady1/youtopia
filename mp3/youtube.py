import logging
import re
from subprocess import getoutput

DOWNLOADER = 'fake_serve'
# DOWNLOADER = 'youtube-dl'
LOGGER = logging.getLogger(__name__)

EXISTS = re.compile('\[download\] (.*?) has already been downloaded')
NEW = re.compile('\[ffmpeg\] Destination: (.*)')


class YouTubeDownloader(object):
    def __init__(self, url):
        self.url = url
        # self.validate_url()

    def fetch(self):
        cmd = 'youtube-dl --extract-audio --audio-format mp3 -o "/youtube/%(title)s.tmp" {}'.format(
            self.url
        )
        output = getoutput(cmd)
        lines = output.split('\n')
        if len(lines) < 3:
            LOGGER.error("Got no lines!")
            return None, None
        fullpath = ''
        LOGGER.debug("output was {}".format(output))
        for line in lines:
            LOGGER.debug("LINE!!!! - {}".format(line))
            if EXISTS.match(line):
                fullpath = EXISTS.match(line).groups()[0]
            elif NEW.match(line):
                fullpath = NEW.match(line).groups()[0]
        LOGGER.debug("returned {}".format(fullpath))
        filename = fullpath.split('/')[-1]
        LOGGER.debug('filename', filename, 'fullpath', fullpath)
        return filename, fullpath


# youtube-dl -x --audio-format mp3 -o %(title).mp3 "https://www.youtube.com/watch\?v\=vU0fYzuypXg"

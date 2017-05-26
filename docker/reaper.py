import logging
import os
import time

log = logging.getLogger(__name__)
HOME = os.environ.get("MEDIA_HOME")
DEBUG = os.environ.get("DEBUG", "False")
INTERVAL = 5 * 60  # 5 Minutes
REAP_AGE_MIN = 30  # Files created greater than REAP_AGE_MIN ago will be reaped


def validate():
    if not HOME:
        log.error("YOUTOPIA_HOME is not set!")
        exit(1)


def run():
    while True:
        time.sleep(INTERVAL)
        log.info("Reaper is waking up.")
        files = os.listdir(HOME)
        now = time.time()
        for f in files:
            log.debug("Examining {}".format(f))
            path = "{}/{}".format(HOME, f)
            if not os.path.isfile(path):
                log.info("Skipping dir {}".format(f))
            info = os.stat(path)
            created = info.st_ctime
            delta = (now - created) / 60.0  # Time delta in minutes
            if delta >= REAP_AGE_MIN:
                log.info("Reaping file {}".format(f))
                os.remove(path)
        log.info("Reaper is going to sleep.")


def main():
    # Configure logging
    dbg = DEBUG.lower() == 'true'
    if dbg:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    log.info("Reaper is starting up")
    validate()
    run()


if __name__ == '__main__':
    main()

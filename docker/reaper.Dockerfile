FROM alpine:3.4
MAINTAINER James Grady <jlgrady1@gmail.com>

ENV DEBUG=False \
    YOUTOPIA_HOME=/srv/youtopia \
    MEDIA_HOME=/youtube

RUN apk add --update python3

COPY reaper.py /

CMD python3 /reaper.py

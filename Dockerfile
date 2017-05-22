FROM alpine:3.4
MAINTAINER James Grady <jlgrady1@gmail.com>

ENV FFMPEG_VERSION=3.3.1 \
    FFMPEG_TMP=/tmp/ffmpeg

WORKDIR /srv/youtopia

RUN apk add --update curl python3 tar xz && \
    ln -s /usr/bin/python3 /usr/local/bin/python && \
    ln -s /usr/bin/pip3 /usr/local/bin/pip && \
    mkdir ${FFMPEG_TMP} && cd ${FFMPEG_TMP} && \
    curl -Lo ffmpeg.tar.xz https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-64bit-static.tar.xz && \
    tar xvf ffmpeg.tar.xz && \
    cp ffmpeg-git-*-64bit-static/ffmpeg ffmpeg-git-*-64bit-static/ffprobe /usr/local/bin && \
    cd / && rm -rf /tmp/ffmpeg

COPY / ./
RUN pip3 install -r requirements.txt

EXPOSE 80

CMD python3 main.py

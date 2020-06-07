FROM alpine-3.7
MAINTAINER yaphetsglhf@gmail.com

RUN set -xe \
    && apk add --no-cache ca-certificates \
                          build-base \
                          git \
                          libffi-dev \
                          openssl \
                          openssl-dev \
                          python3-dev \
    && apk add --no-cache --update python3 \
    && pip3 install -U pip \
    && pip3 install errbot \
                    hypchat \
                    irc \
                    pyasn1 \
                    pyasn1-modules \
                    python-telegram-bot \
                    slackclient \
                    sleekxmpp \
                    requests \
    && adduser -s /bin/sh -D errbot \
    && apk del --purge build-base \
                       libffi-dev \
                       openssl-dev \
                       python3-dev

ARG WORKDIR=/home/errbot
WORKDIR ${WORKDIR}

RUN set -xe \
    && mkdir -p ~/.local/lib/python3.5/site-packages \
    && errbot --init

COPY . ${WORKDIR}/

USER errbot
VOLUME ${WORKDIR}

ENTRYPOINT ["errbot"]

FROM alpine:latest
MAINTAINER James Mills, prologic at shortcircuit dot net dot au

RUN apk -U add znc znc-modperl znc-modtcl znc-modpython znc-extra && \
    apk -U add ca-certificates && \
    rm -rf /var/cache/apk/*

RUN pip3 install requests
COPY mutter.py /usr/src/znc/modules/mutter.py

ADD entrypoint.sh /entrypoint.sh
ADD znc.conf /znc.conf

VOLUME /data

EXPOSE 7000

ENTRYPOINT ["/entrypoint.sh"]
CMD []

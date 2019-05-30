FROM debian:jessie-slim

RUN apt-get update && \
    apt-get install -y wget && \
    apt-get clean

RUN wget -O - https://github.com/writeas/writefreely/releases/download/v0.9.1/writefreely_0.9.1_linux_amd64.tar.gz | tar -C /tmp -zx && \ 
    mkdir /usr/share/writefreely && \
    mv /tmp/writefreely /usr/local/bin/writefreely &&  \
    mv /tmp/pages /tmp/static /tmp/templates  /usr/share/writefreely

COPY start.sh /start.sh

VOLUME /data

EXPOSE 8080/tcp

ENTRYPOINT ["/start.sh"]
CMD []

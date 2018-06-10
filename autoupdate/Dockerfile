FROM golang:alpine AS build

RUN apk add --update git && \
    rm -rf /var/cache/apk/* && \
    go get github.com/prologic/irccat && \
    go get github.com/prologic/msgbus/...

FROM alpine

ENV MSGBUS_URI https://msgbus.mills.io/
ENV MSGBUS_TOPIC ci.mills.io

ENV IRC_NICK autoupdate
ENV IRC_HOST irc.mills.io
ENV IRC_PORT 6667
ENV IRC_CHAN #alerts

RUN apk add --update ca-certificates jq docker && \
    rm -rf /var/cache/apk/*

COPY --from=build /go/bin/irccat /usr/local/bin/irccat
COPY --from=build /go/bin/msgbus /usr/local/bin/msgbus

COPY autoupdate.sh /usr/local/bin/autoupdate.sh
COPY start.sh /start.sh

ENTRYPOINT ["/start.sh"]
CMD ["prologic/autoupdate", "autoupdate_autoupdate"]

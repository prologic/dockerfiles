FROM gliderlabs/alpine:3.1
MAINTAINER James Mills, prologic at shortcircuit dot net dot au

CMD ["python"]

RUN \
    apk add --update ca-certificates wget python && \
    rm -rf /var/cache/apk/* && \
	wget -q -O - https://bootstrap.pypa.io/ez_setup.py | python - && \
	wget -q -O - https://bootstrap.pypa.io/get-pip.py | python - && \
	rm /*.zip && \
	rm -rf $(find /usr/lib/python2.7 -type d -name "test*") && \
	python -m compileall /usr/lib/python2.7 && \
	rm $(find /usr/lib/python2.7 -type f -name "*.py") && \
	rm $(find /usr/lib/python2.7 -type f -name "*.pyo")

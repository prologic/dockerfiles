# zerobin (0bin)

[![Image Layers](https://badge.imagelayers.io/prologic/zerobin:latest.svg)](https://imagelayers.io/?images=prologic/zerobin:latest)

A Alpine based image of [zerobin](https://pypi.python.org/pypi/zerobin)
a client side encrypted pastebin.

## Quick Start

```#!bash
docker run -d -p 80:80 prologic/zerobin
```

With [autodock-paas](https://github.com/prologic/autodock-paas):

```#!bash
docker run -d -e VIRTUALHOST=paste.mydomain.com prologic/zerobin
```

[Docker Compose](https://docs.docker.com/compose/):

```#!yml
zerobin:
  image: prologic/zerobin
  environment:
    - VIRTUALHOST=paste.mydomain.com
  restart: always
```

Production hipache with SSL
===========================

A production version of Hipache with SSL.

Usage
-----

docker-compose.yml:

``` sourceCode
hipache:
    image: prologic/hipache
        ports:
            - "80:80"
            - "443:443"
        volumes:
            - ./ssl:/ssl
        restart: always
```

Or in conjunction with \[prologic/mksslcrt\](<https://hub.docker.com/r/prologic/mksslcrt/>):

``` sourceCode
sslcerts:
    image: prologic/mksslcrt
    command: mydomain.com

hipache:
    image: prologic/hipache
        ports:
            - "80:80"
            - "443:443"
        volumes_from:
            - sslcerts
        restart: always
```

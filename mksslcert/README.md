mksslcrt
========

A simple image based on \[crux\](<https://hub.docker.com/_/crux/>) that allows you to easily create self-signed SSL certificates.

Usage
-----

``` sourceCode
$ docker run --rm -v $(pwd):ssl:/ssl mksslcrt mydomain.com
```

If you want to use the resulting certificates as a "Data Volume Container":

``` sourceCode
$ docker run --name sslcerts prologic/mksslcrt mydomain.com
$ docker run --volumes-from sslcerts prologic/hipache
```

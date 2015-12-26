mksslcrt
========

.. image:: https://badge.imagelayers.io/prologic/mksslcrt:latest.svg
   :target: https://imagelayers.io/?images=prologic/mksslcrt:latest
   :alt: Image Layers

A simple image based on [Alpine](https://hub.docker.com/_/alpine/)
that allows you to easily create self-signed SSL certificates.

Usage
-----

.. code-block:: bash
    
    $ docker run --rm -v $(pwd)/ssl:/ssl mksslcrt mydomain.com


If you want to use the resulting certificates as a "Data Volume Container":

.. code-block:: bash
    
    $ docker run --name sslcerts prologic/mksslcrt mydomain.com
    $ docker run --volumes-from sslcerts prologic/hipache

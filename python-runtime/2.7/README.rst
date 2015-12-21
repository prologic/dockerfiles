.. _Docker: https://www.docker.com/
.. _Alpine Linux: http://www.alpinelinux.org/
.. _Python: https://www.python.org/

Alpine based Python Runtime for Docker
======================================

.. image:: https://badge.imagelayers.io/prologic/python-runtime:latest.svg
   :target: https://imagelayers.io/?images=prologic%2Fpython-runtime:latest
   :alt: Image Layers

A full `Python`_ `Docker`_ image based on `Alpine Linux`_ that
provides a minimal but useful runtime environment at only 25MB!

Supported tags (*and Python version*):

- 2.7

.. note:: This image does not include any build tools so 3rd party
          C-extensions that do not have wheels will not install.

.. note:: Please also note to further optimize this image I removed
          lib2to3, lib-tk, ensurepip, tests, idle and libidle.

There is also an ``2.7-onbuild`` tag which sets up a typical Python
application by performing the following tasks:

.. code-block:: docker
    
    COPY requirements.txt /tmp/requirements.txt
    RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

    WORKDIR /app
    COPY . /app/
    RUN pip install .

To use the ``onbuild`` tag in  your image define your ``Dockerfile`` as::
    
    FROM prologic/python-runtime:2.7-onbuild

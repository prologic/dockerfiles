.. _Docker: https://www.docker.com/
.. _Alpine Linux: http://www.alpinelinux.org/
.. _Python: https://www.python.org/

Alpine based Python Runtime for Docker
======================================

A `Python`_ `Docker`_ image based on `Alpine Linux`_ that provides a minimal but useful
runtime environment.

Supported tags (*and Python version*):

- 2.7

.. note:: This image does not include any build tools so 3rd party C-extensions that do not have
          wheels will not install.

This image is optimized for size::
    
    $ docker images prologic/python-runtime
    REPOSITORY                TAG                 IMAGE ID            CREATED              VIRTUAL SIZE
    prologic/python-runtime   2.7-onbuild         0f52cadcc471        About a minute ago   29.73 MB
    prologic/python-runtime   2.7                 22f023d7f32b        29 minutes ago       29.73 MB
    prologic/python-runtime   latest              22f023d7f32b        29 minutes ago       29.73 MB

There is also an ``2.7-onbuild`` tag which sets up a typical Python application by performing the
following tasks:

.. code-block:: docker
    
    COPY requirements.txt /tmp/requirements.txt
    RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

    WORKDIR /app
    COPY . /app/
    RUN pip install .

To use the ``onbuild`` tag in  your image define your ``Dockerfile`` as::
    
    FROM prologic/python-runtime:2.7-onbuild

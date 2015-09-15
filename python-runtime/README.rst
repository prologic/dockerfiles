.. _Docker: https://www.docker.com/
.. _Alpine Linux: http://www.alpinelinux.org/
.. _Python: https://www.python.org/

Alpine based Python Runtime for Docker
======================================

Some `Docker`_ images for an `Alpine Linux`_ based `Python`_ runtime environment.

These images are optimized for size::
    
    $ docker images prologic/python-runtime
    REPOSITORY                TAG                 IMAGE ID            CREATED              VIRTUAL SIZE
    prologic/python-runtime   2.7-onbuild         0f52cadcc471        About a minute ago   29.73 MB
    prologic/python-runtime   2.7                 22f023d7f32b        29 minutes ago       29.73 MB
    prologic/python-runtime   latest              22f023d7f32b        29 minutes ago       29.73 MB

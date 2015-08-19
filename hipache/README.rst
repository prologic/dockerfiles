Production hipache with SSL
===========================

A production version of Hipache with SSL.

Usage
-----

docker-compose.yml:

.. code-block:: yaml
    
    hipache:
        image: prologic/hipache
            ports:
                - "80:80"
                - "443:443"
            volumes:
                - etc/hipache/ssl:/etc/ssl
            restart: always

#!/bin/sh

# Fix up redis configuration file
sed -i "s/^daemonize yes/daemonize no/g" /etc/redis/redis.conf

# Be sure to bind on all interfaces
sed -i "s/^bind 127.0.0.1/bind 0.0.0.0/g" /etc/redis/redis.conf

# Start services as the base image does.
supervisord -n

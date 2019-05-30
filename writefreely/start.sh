#!/bin/sh

if [ ! -f /config.ini ]; then
  cat > /etc/config.ini << EOF
[server]
hidden_host          = 
port                 = ${PORT:-8080}
bind                 = 0.0.0.0
tls_cert_path        = 
tls_key_path         = 
templates_parent_dir = /usr/share/writefreely
static_parent_dir    = /usr/share/writefreely
pages_parent_dir     = /usr/share/writefreely
keys_parent_dir      = /data

[database]
type     = sqlite3
filename = /data/writefreely.db
username = 
password = 
database = 
host     = localhost
port     = 3306

[app]
site_name         = ${SITE:-Demo}
site_description  = ${DESC:-Demo Writefreely Instance}
host              = ${URL:-http://localhost:8080}
theme             = write
disable_js        = false
webfonts          = true
single_user       = false
open_registration = false
min_username_len  = 3
max_blogs         = 1
federation        = true
public_stats      = true
private           = false
local_timeline    = true
user_invites      = true
EOF
fi

if [ ! -f /data/writefreely.db ]; then
  writefreely -c /etc/config.ini --init-db
  writefreely -c /etc/config.ini --create-admin "${USERNAME:-demo}:${PASSWORD:-demo}"
fi

if [ ! -d /data/keys ]; then
  writefreely -c /etc/config.ini --gen-keys
fi

exec writefreely -c /etc/config.ini "$@"

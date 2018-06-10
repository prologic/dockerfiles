#!/bin/bash

MSGBUS_URI="${MSGBUS_URI:-https://msgbus.mills.io}"
MSGBUS_TOPIC="${MSGBUS_TOPIC:-ci.mills.io}"

REGISTRY_HOSTNAME="${REGISTRY_HOSTNAME:-r.mills.io}"

function docker_login() {
  username="${REGISTRY_USERNAME}"
  if [[ -z "${username}" ]]; then
    if [ -f /run/secrets/registry_username ]; then
      username="$(cat /run/secrets/registry_username)"
    fi
  fi

  password="${REGISTRY_PASSWORD}"
  if [[ -z "${password}" ]]; then
    if [ -f /run/secrets/registry_password ]; then
      password="$(cat /run/secrets/registry_password)"
    fi
  fi

  if [[ ! -z "${username}" ]]; then
    echo "${password}" | docker login -u "${username}" --password-stdin "${REGISTRY_HOSTNAME}"
  fi
}

docker_login

exec msgbus -d sub "${MSGBUS_TOPIC}" /usr/local/bin/autoupdate.sh "${@}"

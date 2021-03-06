#!/bin/bash

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <image> <service> [<service> ...]"
  exit 1
fi

IRC_NICK="${IRC_NICK:-autoupdate}"
IRC_HOST="${IRC_HOST:-irc.mills.io}"
IRC_PORT="${IRC_PORT:-6667}"
IRC_CHAN="${IRC_CHAN:-#alerts}"

JQ_TEMPLATE="${JQ_TEMPLATE:-"\"\\(.repo .owner)/\\(.repo .name)\""}"

REPO="${1}"
shift

SERVICES=("${@}")

payload="$(cat - | jq -r '.payload' | base64 -d)"
repo="$(echo "${payload}" | jq -r "${JQ_TEMPLATE}")"

function update_service() {
  service="${1}"

  image="$(docker service inspect "${service}" | jq -r '.[0] | .Spec.TaskTemplate.ContainerSpec.Image' | cut -f 1 -d '@')"

  docker service update -d --image "${image}" --with-registry-auth "${service}"
}

if [[ "${repo}" == "${REPO}" ]]; then
  echo "incoming payload matches ${repo} == ${REPO}"
  for service in "${SERVICES[@]}"; do
    echo "updating services ${service} ..."
    update_service "${service}"
    echo "NOTICE: service updated ${service}" \
      | irccat -n "${IRC_NICK}" "${IRC_HOST}:${IRC_PORT}" "${IRC_CHAN}"
  done
else
  echo "payload mismatch ${repo} != ${REPO}"
fi

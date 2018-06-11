# autoupdate

A little tiny shell-script driven auto updater for docker services using
webhook payloads from drone.

This uses [msgbus](https://github.com/prologic/msgbus) to subscribe to a
topic setup for drone webhook payload delivery and automatically updates
the matching services.  [jq](https://stedolan.github.io/jq/) is used to
extract information from the payload and [docker](https://www.docker.com)
to perform the updates to the matching services. An announcement is also
sent to a configurable IRC server and channel using
[irccat](https://github.com/prologic/irccat).

By default the configuration parses Drone CI webhooks but can be configured.

Required positional arguments are:

- `<image>`
- `<service>`

You *may* optionally specify multiple services to be updated.

Configuration is via environment variables:

- `JQ_TEMPLATE` -- Filter the payload for the image being updated
- `MSGBUS_URI` -- The msgbus endpoint uri to connect to for pushed alerts
- `MSGBUS_TOPIC` -- The msgbus topic to subscribe to for alerts
- `REGISTRY_(HOSTNAME|USERNAME|PASSWORD)` -- Docker registry configuration and optional login
- `IRC_(HOST|PORT|CHAN|NICK)` - Various IRC configuration parameters

**Note:** You can also use Docker Secrets to manage registry credentials. Use names `registry_username` and `registry_password`.

## Example(s)

```#!bash
$ docker run -t prologic/autoupdate prologic/msgbus msgbus_msgbus
```

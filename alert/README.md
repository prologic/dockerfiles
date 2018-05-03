# alert

A little tiny shell-script driven Prometheus IRC notifications for alerts.

This uses [msgbus](https://github.com/prologic/msgbus) to subscribe to alerts
coming from Prometheus (*which has been configured to send alerts to msgbus*)
and [irccat](https://github.com/prologic/irccat) to connect to and post on IRC.

Configuration is via environment variables:

- `MSGBUS_URI` -- The msgbus endpoint uri to connect to for pushed alert# alert

A little tiny shell-script driven Prometheus IRC notifications for alerts.

This uses [msgbus](https://github.com/prologic/msgbus) to subscribe to alerts
coming from Prometheus (*which has been configured to send alerts to msgbus*)
and [irccat](https://github.com/prologic/irccat) to connect to and post on IRC.

Configuration is via environment variables:

- `MSGBUS_URI` -- The msgbus endpoint uri to connect to for pushed alerts
- `MSGBUS_TOPIC` -- The msgbus topic to subscribe to for alerts
- `IRC_(HOST|PORT|CHAN|NICK)` - Various IRC configuration parameters

# ircnotify

A little tiny shell-script driven generic IRC notifications tool.

This uses [msgbus](https://github.com/prologic/msgbus) to subscribe to generic
topics (*say from webhooks*), [jq](https://stedolan.github.io/jq/) to filter
and templateize the payload into an IRC message  and
[irccat](https://github.com/prologic/irccat) to connect to and post on IRC.

Configuration is via environment variables:

- `JQ_TEMPLATE` -- The jq template/expression to use (**Required**).
- `MSGBUS_URI` -- The msgbus endpoint uri to connect to for pushed alerts
- `MSGBUS_TOPIC` -- The msgbus topic to subscribe to for alerts
- `IRC_(HOST|PORT|CHAN|NICK)` - Various IRC configuration parameters

You can also provide the `JQ_TEMPLATE` via the first argument like this:

```#!yaml
ircnotify:
  image: prologic/ircnotify
  command: '. | "NOTICE: \(.repo.owner)/\(.repo.name) build \(.build.number) \(.build.status) (\(.build.link))"'
```

## Example(s)

Provide `JQ_TEMPLATE` via environment:
```#!bash
$ docker run -t -e JQ_TEMPLATE='"NOTICE: \( .message )"' prologic/ircnotify
```

Provide `JQ_TEMPLATE` via command-line argument:
```#!bash
$ docker run -t prologic/ircnotify '"NOTICE: \( .message )"'
```

Use the default `JQ_TEMPLATE` of `'"\(.)"'`:
```#!bash
$ docker run -t prologic/ircnotify
```

## Templte(s)

Some pre-defined templates to help get you started:

* Docker Hub: `'"NOTICE: \(.push_data.pusher) pushed image \(.repository.repo_name) with tag \(.push_data.tag)"'`
* Drone CI: `'"NOTICE: \(.repo.owner)/\(.repo.name) build \(.build.number) \(.build.status) (\(.build.link))"'`
* Prometheus AlertManager: `'.alerts[] | "ALERT: \(.labels.alertname) \(.status) - \(.annotations.summary)"'`

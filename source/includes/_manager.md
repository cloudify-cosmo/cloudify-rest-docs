# Manager

The following REST API calls provide information about Cloudify's manager.


## Status

`GET /api/v2/events`

Gets Cloudify manager status.

> Request Example

```shell
$ curl -XGET http://localhost/api/v2/status
```
> Response Example

```json
{
  "status": "running",
  "services": [
    {
      "instances": [
        {
          "LoadState": "loaded",
          "Description": "InfluxDB Service",
          "state": "running",
          "MainPID": 3609,
          "Id": "cloudify-influxdb.service",
          "ActiveState": "active",
          "SubState": "running"
        }
      ],
      "display_name": "InfluxDB"
    },
    {
      "instances": [
        {
          "LoadState": "loaded",
          "Description": "Cloudify Management Worker Service",
          "state": "running",
          "MainPID": 6565,
          "Id": "cloudify-mgmtworker.service",
          "ActiveState": "active",
          "SubState": "running"
        }
      ],
      "display_name": "Celery Management"
    },
    {
      "instances": [
        {
          "LoadState": "loaded",
          "Description": "LSB: Starts Logstash as a daemon.",
          "state": "running",
          "MainPID": 0,
          "Id": "logstash.service",
          "ActiveState": "active",
          "SubState": "running"
        }
      ],
      "display_name": "Logstash"
    },
    {
      "instances": [
        {
          "LoadState": "loaded",
          "Description": "RabbitMQ Service",
          "state": "running",
          "MainPID": 2697,
          "Id": "cloudify-rabbitmq.service",
          "ActiveState": "active",
          "SubState": "running"
        }
      ],
      "display_name": "RabbitMQ"
    },
    {
      "instances": [
        {
          "LoadState": "loaded",
          "Description": "Cloudify AMQP InfluxDB Broker Service",
          "state": "running",
          "MainPID": 4293,
          "Id": "cloudify-amqpinflux.service",
          "ActiveState": "active",
          "SubState": "running"
        }
      ],
      "display_name": "AMQP InfluxDB"
    },
    {
      "instances": [
        {
          "LoadState": "loaded",
          "Description": "Cloudify REST Service",
          "state": "running",
          "MainPID": 5021,
          "Id": "cloudify-restservice.service",
          "ActiveState": "active",
          "SubState": "running"
        }
      ],
      "display_name": "Manager Rest-Service"
    },
    {
      "instances": [
        {
          "LoadState": "loaded",
          "Description": "Cloudify WebUI Service",
          "state": "running",
          "MainPID": 5831,
          "Id": "cloudify-webui.service",
          "ActiveState": "active",
          "SubState": "running"
        }
      ],
      "display_name": "Cloudify UI"
    },
    {
      "instances": [
        {
          "LoadState": "loaded",
          "Description": "nginx - high performance web server",
          "state": "running",
          "MainPID": 5893,
          "Id": "nginx.service",
          "ActiveState": "active",
          "SubState": "running"
        }
      ],
      "display_name": "Webserver"
    },
    {
      "instances": [
        {
          "LoadState": "loaded",
          "Description": "Riemann Service",
          "state": "running",
          "MainPID": 6500,
          "Id": "cloudify-riemann.service",
          "ActiveState": "active",
          "SubState": "running"
        }
      ],
      "display_name": "Riemann"
    },
    {
      "instances": [
        {
          "LoadState": "loaded",
          "Description": "Elasticsearch",
          "state": "running",
          "MainPID": 4219,
          "Id": "elasticsearch.service",
          "ActiveState": "active",
          "SubState": "running"
        }
      ],
      "display_name": "Elasticsearch"
    }
  ]
}
```

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`status` | string | The status of the manager. Will always have a "running" value.
`services`| list | List of [Service](#the-service-object) resources each, representing a service running in the manager.

### The Service Object:

Attribute | Type | Description
--------- | ------- | -------
`instances` | list | List of [Instance](#the-instance-object) resources representing the instances of a service running in a manager in a DBus structure.
`display_name` | string | The service name.

### The Instance Object:

Attribute | Type | Description
--------- | ------- | -------
`LoadState` | string | Contains a state value that reflects whether the configuration file of this unit has been loaded.
`Description` | string | The description of the service instance.
`state` | string | The state of the service instance (unknown, down, up, finish).
`MainPID` | integer | The process id of the main service instance process.
`Id` | string | The id of the service instance.
`ActiveState` | string | Contains a state value that reflects whether the unit is currently active or not. The following states are currently defined: active, reloading, inactive, failed, activating, deactivating.
`SubState` | string | Encodes states of the same state machine that `ActiveState` covers, but knows more fine-grained states that are unit-type-specific.

Information about the instance fields can be found in the [DBus reference](http://www.freedesktop.org/wiki/Software/systemd/dbus/).


## Version

`GET /api/v2/version`

Gets Cloudify manager version information.


> Request Example

```shell
$ curl -XGET http://localhost/api/v2/version
```

> Response Example

```json
{
  "date": "",
  "commit": "",
  "version": "3.3.0",
  "build": "85"
}
```

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`date` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The date and time of the build the manager was built of.
`commit`| string | Git commit hash of the REST service code base used by the manager.
`version` | string | The version of Cloudify manager.
`build` | string | Build number.

# Manager

The following REST API calls provide information about Cloudify's manager.

## Status

> Request Example

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/status"
```

```python
# Python Client-
client.manager.get_status()

# Python Requests-
url = "http://<manager-ip>/api/v2.1/status"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
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
    }
    ...
  ]
}
```

`GET "{manager-ip}/api/v2.1/events"`

Gets Cloudify manager status.

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

> Request Example

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/version"
```

```python
# Python Client-
client.manager.get_version()

# Python Requests-
url = "http://<manager-ip>/api/v2.1/version"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
```

> Response Example

```json
{
  "date": "",
  "commit": "",
  "version": "3.4.0-m5",
  "build": "85"
}
```

`GET "{manager-ip}/api/v2.1/version"`

Gets Cloudify manager version information.

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`date` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The date and time of the build the manager was built of.
`commit`| string | Git commit hash of the REST service code base used by the manager.
`version` | string | The version of Cloudify manager.
`build` | string | Build number.

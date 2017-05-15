# Manager

The following REST API calls provide information about Cloudify's manager.

## Status

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3/status"
```

```python
# Using ClodifyManager
client.manager.get_status()

# Using requests
url = 'http://<manager-ip>/api/v3/status'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_include': 'status'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
response.json()
```

> Response Example

```json
{
  "status": "running"
}
```

`GET "{manager-ip}/api/v3/status"`

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
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3/version?_include=version"
```

```python
# Using CloudifyClient
client.manager.get_version()

# Using requests
url = 'http://<manager-ip>/api/v3/version'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_include': 'version'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
response.json()
```

> Response Example

```json
{
  "version": "4.0.1"
}
```

`GET "{manager-ip}/api/v3/version"`

Gets Cloudify manager version information.

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`date` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The date and time of the build the manager was built of.
`commit`| string | Git commit hash of the REST service code base used by the manager.
`version` | string | The version of Cloudify manager.
`build` | string | Build number.
`edition` | string | Software edition (either `community` or `premium`)

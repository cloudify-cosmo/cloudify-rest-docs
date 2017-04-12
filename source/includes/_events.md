# Events

## The Event Resource

### Attributes:

Attribute | Type | Description
--------- | ---- | -----------
`blueprint_id` | string | Blueprint id
`deployment_id` | string | Deployment id
`execution_id` | string | Execution id
`workflow_id` | string | Workflow id
`node_name` | string | Node name
`node_instance_id` | string | Node instance id
`operation` | string | Operation path (only available in operation events)
`timestamp` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The time at which the event was logged on the management machine
`reported_timestamp` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The time at which the event occurred on the executing machine
`message` | string | Message text
`type` | string | Indicates whether the resource is a `cloudify_event` or a `cloudify_log`
`event_type` | string | Event type name (only for `cloudify_event` items)
`logger` | string | Logger id (only for `cloudify_log` items)
`level` | string | Log level (only for `cloudify_log` items)


## List events

### Lists all events

> Request Example

```shell
$ curl -X GET --header "tenant: default_tenant" -u user:password "http://<manager_ip>/api/v3/events"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager-ip>',
    username='<manager-username>',
    password='<manager-password>',
    tenant='<manager-tenant>')
events = client.events.list()
for event in events:
    print event

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager-ip>/api/v3/events'
headers = {'Tenant': 'default_tenant'}
response = requests.get(url, auth=HTTPBasicAuth('user', 'password'), headers=headers)
response.json()
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/events",
  "method": "GET",
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> Response Example

```json
{
  "items": [
    {
      "node_instance_id": "vm_ke9e2d",
      "operation": "cloudify.interfaces.cloudify_agent.create",
      "blueprint_id": "linuxbp1",
      "timestamp": "2017-03-22T11:41:59.169Z",
      "message": "Successfully configured cfy-agent",
      "level": "info",
      "node_name": "vm",
      "workflow_id": "install",
      "reported_timestamp": "2017-03-22T11:41:59.169Z",
      "deployment_id": "linuxdp1",
      "type": "cloudify_log",
      "execution_id": "19ce78d6-babc-4a18-ba8e-74b853f2b387",
      "logger": "22e710c6-18b8-4e96-b8a3-2104b81c5bfc"
    },
    {
      "node_instance_id": "vm_ke9e2d",
      "event_type": "task_succeeded",
      "operation": "cloudify.interfaces.cloudify_agent.create",
      "blueprint_id": "linuxbp1",
      "timestamp": "2017-03-22T11:42:00.083Z",
      "message": "Task succeeded 'cloudify_agent.installer.operations.create'",
      "node_name": "vm",
      "workflow_id": "install",
      "reported_timestamp": "2017-03-22T11:42:00.083Z",
      "deployment_id": "linuxdp1",
      "type": "cloudify_event",
      "execution_id": "19ce78d6-babc-4a18-ba8e-74b853f2b387"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 2,
      "offset": 0,
      "size": 10000
    }
  }
}
```

`GET "{manager-ip}/api/v3/events"`

### List events within a time range

`GET "{manager-ip}/api/v3/events?_range=timestamp,[time_start],[time_end]"`

Parameter | Type | Description
--------- | ------- | -------
`time_start` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | optional value to begin range with.
`time_end` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | optional value to end range with.

all events within a  time range:

`GET "/api/v3/events?_range=timestamp,<time_start>,<time_end>"`

all events since a given time:

`GET "/api/v3/events?_range=timestamp,<time_start>,`

all events until a given time:

`GET "/api/v3/events?_range=timestamp,,<time_end>"`

<aside class="notice">
Always include the commas, even when the values are omitted
</aside>

### List events with filters

`GET "{manager-ip}/api/v3/events?<filter>"`

Allowed filters:

- `blueprint_id`
- `deployment_id`
- `execution_id`
- `event_type` (only returns `cloudify-event` items)
- `level` (only returns `cloudify-log` items)
- `message`([SQL's LIKE style pattern expected](https://www.postgresql.org/docs/9.5/static/functions-matching.html#FUNCTIONS-LIKE))

Multiple filters can be passed in the same request:

- Filters of the same type will be combined using a logical OR operator
- Filters of differnt type will be combined using a logical AND operator.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Event` resources.
`metadata` | object | Pagination metadata

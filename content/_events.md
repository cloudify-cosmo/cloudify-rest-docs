# Events

## The Event Resource

### Attributes:

Attribute | Type | Description
--------- | ---- | -----------
`blueprint_id` | string | Blueprint id
`deployment_id` | string | Deployment id
`error_causes` | [[ErrorCause](#the-errorcause-object)] | List of errors that happened while executing a given task (only for `cloudify_event` items)
`event_type` | string | Event type name (only for `cloudify_event` items)
`execution_id` | string | Execution id
`level` | string | Log level (only for `cloudify_log` items)
`logger` | string | Logger id (only for `cloudify_log` items)
`message` | string | Message text
`node_instance_id` | string | Node instance id
`node_name` | string | Node name
`operation` | string | Operation path (only available in operation events)
`reported_timestamp` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The time at which the event occurred on the executing machine
`timestamp` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The time at which the event was logged on the management machine
`type` | string | Indicates whether the resource is a `cloudify_event` or a `cloudify_log`
`workflow_id` | string | Workflow id

## The ErrorCause object

Attribute | Type | Description
--------- | ---- | -----------
`message` | string | Error message
`traceback` | string | Stack trace at the point where the exception was raised
`type` | string | Exception type


## List events

### Lists all events

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u user:<manager-password> \
    "http://<manager_ip>/api/v3.1/events"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager-ip>',
    username='<manager-username>',
    password='<manager-password>',
    tenant='<manager-tenant>')
events = client.events.list(include_logs=True)
for event in events:
    print event

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager-ip>/api/v3.1/events'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(url, auth=HTTPBasicAuth('user', '<manager-password>'), headers=headers)
response.json()
```

> Response Example

```json
{
  "items": [
    {
      "node_instance_id": "vm_ke9e2d",
      "operation": "cloudify.interfaces.cloudify_agent.create",
      "blueprint_id": "linuxbp1",
      "timestamp": "2017-03-22T11:42:00.484Z",
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
      "timestamp": "2017-03-22T11:42:00.788Z",
      "message": "Task succeeded 'cloudify_agent.installer.operations.create'",
      "node_name": "vm",
      "workflow_id": "install",
      "error_causes": null,
      "reported_timestamp": "2017-03-22T11:42:00.083Z",
      "deployment_id": "linuxdp1",
      "type": "cloudify_event",
      "execution_id": "19ce78d6-babc-4a18-ba8e-74b853f2b387"
    },
    {
      "node_instance_id": "vm_ke9e2d",
      "event_type": "task_failed",
      "operation": "cloudify.interfaces.cloudify_agent.create",
      "blueprint_id": "linuxbp1",
      "timestamp": "2017-03-22T11:43:02.132Z",
      "message": "Task failed 'cloudify_agent.installer.operations.create' -> ERROR_MESSAGE",
      "node_name": "vm",
      "workflow_id": "install",
      "error_causes": [
        {
          "message": "ERROR_MESSAGE",
          "traceback": "Traceback (most recent call last):\n  File \"/opt/mgmtworker/env/lib/python2.7/site-packages/cloudify/dispatch.py\", line 624, in main\n
  File \"/opt/mgmtworker/env/lib/python2.7/site-packages/cloudify/dispatch.py\", line 389, in handle\n  File \"/opt/mgmtworker/env/lib/python2.7/site-packages/t
estmockoperations/tasks.py\", line 476, in execution_logging\n    raise NonRecoverableError('ERROR_MESSAGE', causes=causes)\nNonRecoverableError: ERROR_MESSAGE\n",
          "type": "NonRecoverableError"
        }
      ],
      "reported_timestamp": "2017-03-22T11:43:01.823Z",
      "deployment_id": "linuxdp1",
      "type": "cloudify_event",
      "execution_id": "19ce78d6-babc-4a18-ba8e-74b853f2b387"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 3,
      "offset": 0,
      "size": 10000
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/events"`

### List events within a time range

`GET "{manager-ip}/api/v3.1/events?_range=timestamp,[time_start],[time_end]"`

Parameter | Type | Description
--------- | ------- | -------
`time_start` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | optional value to begin range with.
`time_end` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | optional value to end range with.

all events within a  time range:

`GET "/api/v3.1/events?_range=timestamp,<time_start>,<time_end>"`

all events since a given time:

`GET "/api/v3.1/events?_range=timestamp,<time_start>,`

all events until a given time:

`GET "/api/v3.1/events?_range=timestamp,,<time_end>"`

<aside class="notice">
Always include the commas, even when the values are omitted
</aside>

### List events with filters

`GET "{manager-ip}/api/v3.1/events?<filter>"`

Allowed filters:

- `blueprint_id`
- `deployment_id`
- `execution_id`
- `event_type` (only returns `cloudify-event` items)
- `level` (only returns `cloudify-log` items)
- `message`([SQL's LIKE style pattern expected](https://www.postgresql.org/docs/9.5/static/functions-matching.html#FUNCTIONS-LIKE))
- `include_logs`(Include also logs in the response, defaults to False)

Multiple filters can be passed in the same request:

- Filters of the same type will be combined using a logical OR operator
- Filters of differnt type will be combined using a logical AND operator.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Event` resources.
`metadata` | object | Pagination metadata

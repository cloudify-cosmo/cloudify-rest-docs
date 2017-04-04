# Events

## The Event Resource

> `Note`

```python
# include this code when using cloudify python client-
from cloudify_rest_client import CloudifyClient
client = CloudifyClient('<manager-ip>')

# include this code when using python requests-
import requests
```

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`event_type` | string | Event type name
`type` | string | Indicates whether the resource is an event or a log (`cloudify_event` or `cloudify_log`)
`tags` | list | List of tags
`timestamp` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The time at which the event occurred on the executing machine
`@timestamp` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The time at which the event was logged on the management machine
`message_code` | string | Reserved, currently unused
`context` | [Context](#the-context-object) | contains various identifiers related to the event
`message` | [Message](#the-message-object) | contains the event message
`level` | string | Log level (only available in log events)
`logger` | string | Logger name
`@version` | string | Internal log entry version (logstash)

### The Context object:

Attribute | Type | Description
--------- | ------- | -------
`task_id` | string | Task id (only available in operation events)
`task_name` | string | Task name (only available in operation events)
`task_queue` | string | Task queue (only available in operation events)
`task_target` | string | Task target (only available in operation events)
`operation` | string | Operation path (only available in operation events)
`task_total_retries` | integer | Number of max retries, -1 if infinite (only available in operation events)
`task_current_retries` | integer | Number of attempted retries (only available in operation events)
`plugin` | string | Plugin name
`blueprint_id` | string | Blueprint id
`node_name` | string | Node name
`node_id` | string | Node instance id
`workflow_id` | string | Workflow id
`deployment_id` | string | Deployment id
`execution_id` | string | Execution id

### The Message Object:
Attribute | Type | Description
--------- | ------- | -------
`text` | string | Message text


## List Events

> Request Example

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/events"
```

```python
# Python Client-
events = client.events.list()
for event in events:
    print event

# Python Requests-
url = "http://<manager-ip>/api/v2.1/events"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
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
      "level": "info",
      "timestamp": "2015-12-02 14:53:21.821+0000",
      "@timestamp": "2015-12-02T14:53:21.823Z",
      "tags": [
        "event"
      ],
      "message_code": null,
      "@version": "1",
      "context": {
        "task_id": "45f53924-af08-438c-88ac-34f5d76bb677",
        "blueprint_id": "hello-world",
        "plugin": "agent",
        "task_target": "hello1",
        "node_name": "vm",
        "workflow_id": "install",
        "node_id": "vm_6d480",
        "task_name": "cloudify_agent.installer.operations.create",
        "task_queue": "hello1",
        "operation": "cloudify.interfaces.cloudify_agent.create",
        "execution_id": "274d9cfb-42ae-4ba7-853d-bf0e990b5add",
        "deployment_id": "hello1"
      },
      "logger": "45f53924-af08-438c-88ac-34f5d76bb677",
      "type": "cloudify_log",
      "message": {
        "text": "Disabling requiretty directive in sudoers file"
      }
    },
    {
      "event_type": "task_started",
      "tags": [
        "event"
      ],
      "timestamp": "2015-12-02 14:53:23.593+0000",
      "@timestamp": "2015-12-02T14:53:23.664Z",
      "message_code": null,
      "@version": "1",
      "context": {
        "deployment_id": "hello1",
        "task_current_retries": 0,
        "task_id": "a0db8898-0fa1-4eae-ad1f-741f3253e6b2",
        "blueprint_id": "hello-world",
        "plugin": "agent",
        "task_target": "hello1",
        "node_name": "vm",
        "workflow_id": "install",
        "node_id": "vm_6d480",
        "task_name": "cloudify_agent.installer.operations.configure",
        "task_queue": "hello1",
        "operation": "cloudify.interfaces.cloudify_agent.configure",
        "task_total_retries": -1,
        "execution_id": "274d9cfb-42ae-4ba7-853d-bf0e990b5add"
      },
      "message": {
        "text": "Task started 'cloudify_agent.installer.operations.configure'",
        "arguments": null
      },
      "type": "cloudify_event"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 2,
      "size": 10000,
      "offset": 0
    }
  }
}
```

`GET "{manager-ip}/api/v2.1/events"`

Lists all events.

`GET "{manager-ip}/api/v2.1/events?_range=@timestamp,[time_start],[time_end]"`

Lists all events within a time range:

Parameter | Type | Description
--------- | ------- | -------
`time_start` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | optional value to begin range with.
`time_end` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | optional value to end range with.

time range: `/api/v2.1/events?_range=@timestamp,2015-12-01,2015-12-31T14:30:00Z`

all events since: `/api/v2.1/events?_range=@timestamp,2015-12-01,`

all events until: `/api/v2.1/events?_range=@timestamp,,2015-12-31`

<aside class="notice">
Always include the commas, even when the values are omitted
</aside>

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Event` resources.

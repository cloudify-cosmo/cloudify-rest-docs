# Events

## The Event Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`blueprint_id` | string | Blueprint id
`deployment_id` | string | Deployment id
`execution_id` | string | Execution id
`message` | string | Message text
`event_type` | string | Event type name
`node_instance_id` | string | Node instance id
`node_name` | string | Node name
`operation` | string | Operation path (only available in operation events)
`timestamp` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The time at which the event was logged on the management machine
`reported_timestamp` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The time at which the event occurred on the executing machine
`type` | string | Indicates whether the resource is a `cloudify_event` or a `cloudify_log`
`workflow_id` | string | Workflow id


## List events

### Lists all events

> Request Example

```shell
$ curl -X GET --header "tenant: default_tenant" -u user:password "http://<manager_ip>/api/v3/events"
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

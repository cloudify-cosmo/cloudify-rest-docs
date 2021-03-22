# Execution Schedules

## The Execution Schedule Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | The name of the execution schedule.
`deployment_id` | string | The id of the deployment to which the scheduled execution is related.
`workflow_id` | string | The id of the workflow which the scheduled execution runs.
`parameters` | object | A dict of the workflow parameters passed when starting the scheduled execution.
`created_at` | datetime | The time the execution schedule was created at.
`next_occurrence` | datetime | The calculated next time in which the scheduled workflow should be executed at.
`since` | datetime | The earliest time the scheduled workflow should be executed at.
`until` | datetime | The latest time the scheduled workflow may be executed at (optional).
`stop_on_fail` | boolean | Whether the scheduler should stop attempting to run the execution once it failed (**False** by default).
`enabled` | boolean | Whether this schedule is currently enabled (**True** by default).

## List Execution Schedules

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/execution-schedules?_include=id,deployment_id,workflow_id,next_occurrence"
```

```python
# Using CloudifyClient
execution_schedules = client.execution_schedules.list(_include=['id', 'deployment_id', 'workflow_id', 'next_occurrence'])
for schedule in execution_schedules:
  print(schedule)

# Using requests
url = 'http://<manager-ip>/api/v3.1/execution-schedules'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_include': 'id,deployment_id,workflow_id,next_occurrence'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
```

> Response Example

```json
{
  "items": [
    {
      "id": "dep_a",
      "next_occurrence": "2021-03-08T18:47:00.000Z",
      "workflow_id": "install",
      "deployment_id": "dep"
    },
    {
      "id": "dep_b",
      "next_occurrence": "2021-03-09T18:47:00.000Z",
      "workflow_id": "uninstall",
      "deployment_id": "dep"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 2,
      "offset": 0,
      "size": 0
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/execution-schedules"`

Lists all execution schedules.


## Get Execution Schedule

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/executions-schedules/<schedule-id>?
    deployment_id=<deployment-id>&
    _include=id,deployment_id,workflow_id,next_occurrence"
```

```python
# Using CloudifyClient
client.execution_schedules.get(
    schedule_id='<schedule_id>',
    deployment_id='<deployment_id>',
    _include=['id', 'deployment_id', 'workflow_id', 'next_occurrence']
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/executions-schedules/<schedule_id>'
headers = {'Tenant': '<manager-tenant>'}
querystring = {
    'deployment_id': '<deployment-id>',
    '_include': 'id,deployment_id,workflow_id,next_occurrence'
}
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
  "id": "dep_a",
  "next_occurrence": "2021-03-08T10:16:00.000Z",
  "workflow_id": "install",
  "deployment_id": "dep"
}
```

`GET "{manager-ip}/api/v3.1/execution-schedules/{schedule-id}?deployment_id={deployment-id}"`

Gets an execution schedule.

### URI Parameters
* `schedule-id`: The id of the execution schedule.
* `deployment-id`: The id of the deployment to which the schedule belongs.

### Response
An `ExecutionSchedule` resource.


## Create Execution Schedule

> Request Example

```shell
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"workflow_id": "install", "since": "2021-1-1 12:00:00",
    "until": "2022-1-1 12:00:00", "recurrence": "1 day"}' \
    "http://<manager-ip>/api/v3.1/execution-schedules/<schedule-id>?
    deployment_id=<deployment-id>&_include=id"
```

```python
# Using CloudifyClient
client.execution_schedules.create(
    schedule_id='<schedule-id>',
    deployment_id='<deployment-id>',
    workflow_id='install',
    since='2021-1-1 12:00:00',
    until='2022-1-1 12:00:00',
    recurrence='1 day',
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/execution-schedules/<schedule-id>'
headers = {
    'Content-Type': 'application/json',
    'Tenant': '<manager-tenant>',
}
querystring = {'deployment_id': '<deployment-id>', '_include': 'id'}
payload ={
    'workflow_id': 'install',
    'since': '2021-1-1 12:00:00',
    'until': '2022-1-1 12:00:00',
    'recurrence': '1 day',
}
response = requests.put(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
    json=payload,
)
response.json()
```

> Response Example

```json
{
  "id": "custom-sched"
}
```

`PUT -d '{"workflow_id": "install", ...}' "{manager-ip}/api/v3.1/execution-schedules/{schedule-id}?deployment_id={deployment-id}"`

Creates a new execution schedule.

### URI Parameters
* `schedule-id`: The id of the new execution schedule.
* `deployment-id`: The id of the deployment for which to schedule the workflow.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`workflow_id` | string | The workflow id/name that the schedule should execute.
`execution_arguments` | object | A dictionary of arguments passed directly to the workflow execution.
`parameters` | object | A dictionary containing parameters to be passed to the execution when starting it.
`since` | string | A string representing the earliest date and time this workflow should be executed at, of the format `%Y-%m-%d %H:%M:%S`. Must be provided if no `rrule` is given.
`until` | string | A string representing the latest date and time this workflow may be executed at, of the format `%Y-%m-%d %H:%M:%S` (optional).
`recurrence` | string | A string representing the frequency with which to run the execution, e.g. `2 weeks`. Must be provided if no `rrule` is given and `count` is other than 1.
`count` | integer | Maximum number of times to run the execution. If left empty, there's no limit on repetition.
`weekdays` | string | A list of strings representing the weekdays on which to run the execution, e.g. `['su', 'mo', 'tu']`. If left empty, the execution will run on any weekday.
`rrule` | string | A string representing a scheduling rule in the iCalendar format, e.g. `RRULE:FREQ=DAILY;INTERVAL=3`, which means "run every 3 days". Optional. Mutually exclusive with `recurrence`, `count` and `weekdays`.
`slip` | integer | Maximum time window after the target time has passed, in which the scheduled execution can run (in minutes). If not provided, defaults to 0.
`stop_on_fail` | boolean | If set to true, once the execution has failed, the scheduler won't make further attempts to run it. If not provided, defaults to `false`.

Valid execution arguments are:

* `allow_custom_parameters` (boolean): Specifies whether to allow custom parameters, which are not present in the parameters schema of the workflow.
* `force` (boolean): Specifies whether to force the workflow execution in case there is already a running execution.
* `dry_run` (boolean): If set to true, no actual actions will be performed.
* `wait_after_fail` (integer): When a task fails, wait this many seconds for already-running tasks to return.
* `queue` (boolean): Whether to queue the execution if it can't run. **Useless in schedules**: all executions which cannot run will be queued.
See Executions for more details on these.

Valid **recurrence** expressions are of the form `<integer> minutes|hours|days|weeks|months|years`. These can be also written without a space after the number, without the final `s`, or using the short forms `min|h|d|w|mo|y`.

Valid **weekdays** expressions are a list containing any of `su|mo|tu|we|th|fr|sa`.
These may be optionally prefixed by `1` to `4` or `l-` (for "last") signifying a "complex weekday", e.g. `2mo` for "the 2nd Monday of a month" or `l-fr` for "the last Friday of a month". Complex weekdays can only be used in tandem with a `months` or `years` recurrence.

### Response
An `ExecutionSchedule` resource.


## Update Execution Schedule

> Request Example

```shell
$ curl -X PATCH \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"since": "2021-1-1 12:00:00", "until": "2022-1-1 12:00:00", "recurrence": "1 day", "enabled": True}' \
    "http://<manager-ip>/api/v3.1/execution-schedules/<schedule-id>?
    deployment_id=<deployment-id>&_include=id"
```

```python
# Using CloudifyClient
client.execution_schedules.update(
    schedule_id='<schedule-id>',
    deployment_id='<deployment-id>',
    since='2021-1-1 12:00:00',
    until='2022-1-1 12:00:00',
    recurrence='1 day',
    enabled=True,
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/execution-schedules/<schedule-id>'
headers = {
    'Content-Type': 'application/json',
    'Tenant': '<manager-tenant>',
}
querystring = {'deployment_id': '<deployment-id>', '_include': 'id'}
payload ={
    'since': '2021-1-1 12:00:00',
    'until': '2022-1-1 12:00:00',
    'recurrence': '1 day',
    'enabled': True,
}
response = requests.patch(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
    json=payload,
)
response.json()
```

> Response Example

```json
{
  "id": "custom-sched"
}
```

`PATCH -d '{"since": "2021-1-1 12:00:00", "until": "2022-1-1 12:00:00", ...}' "{manager-ip}/api/v3.1/execution-schedules/{schedule-id}?deployment_id={deployment-id}"`

Updates an existing execution schedule.

### URI Parameters
* `schedule-id`: The id of the execution schedule to update.
* `deployment-id`: The id of the deployment to which the schedule belongs.

### Request Body
All fields below are optional.

Property | Type | Description
--------- | ------- | -----------
`since` | string | A string representing the earliest date and time this workflow should be executed at, of the format `%Y-%m-%d %H:%M:%S`.
`until` | string | A string representing the latest date and time this workflow may be executed at, of the format `%Y-%m-%d %H:%M:%S`.
`recurrence` | string | A string representing the frequency with which to run the execution, e.g. `2 weeks`.
`count` | integer | Maximum number of times to run the execution.
`weekdays` | string | A list of strings representing the weekdays on which to run the execution, e.g. `['su', 'mo', 'tu']`.
`rrule` | string | A string representing a scheduling rule in the iCalendar format, e.g. `RRULE:FREQ=DAILY;INTERVAL=3`, which means "run every 3 days". Mutually exclusive with `recurrence`, `count` and `weekdays`.
`slip` | integer | Maximum time window after the target time has passed, in which the scheduled execution can run (in minutes).
`stop_on_fail` | boolean | If set to true, once the execution has failed, the scheduler won't make further attempts to run it.
`enabled` | boolean | Set to false to make the scheduler ignore this schedule, until set to true again.

Valid **recurrence** expressions are of the form `<integer> minutes|hours|days|weeks|months|years`. These can be also written without a space after the number, without the final `s`, or using the short forms `min|h|d|w|mo|y`.

Valid **weekdays** expressions are a list containing any of `su|mo|tu|we|th|fr|sa`.
These may be optionally prefixed by `1` to `4` or `l-` (for "last") signifying a "complex weekday", e.g. `2mo` for "the 2nd Monday of a month" or `l-fr` for "the last Friday of a month". Complex weekdays can only be used in tandem with a `months` or `years` recurrence.

### Response
An `ExecutionSchedule` resource.


## Delete Execution Schedule

> Request Example

```shell
$ curl -X DELETE \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/executions-schedules/<schedule-id>?deployment_id=<deployment-id>"
```

```python
# Using CloudifyClient
client.execution_schedules.delete(
    schedule_id='<schedule-id>',
    deployment_id='<deployment-id>'
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/executions-schedules/<schedule-id>'
headers = {'content-type': 'application/json'}
querystring = {'deployment_id': '<deployment-id>'}
requests.delete(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
```

`DELETE "{manager-ip}/api/v3.1/executions-schedules/{schedule-id}?deployment_id={deployment-id}"`

Deletes an execution schedule.

### URI Parameters
* `schedule-id`: The id of the execution schedule.
* `deployment-id`: The id of the deployment to which the schedule belongs.

### Response
No content - HTTP code 204.
# Execution Groups

## The Execution Group Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | A unique identifier for the group.
`created_at` | datetime | The time when the group was created.
`created_by` | string | Username of the creator of this group.
`tenant_name` | string | The name of the tenant that owns the group.
`visibility` | string | The visibility of the group.
`resource_availability` | string | The availability of the group.
`private_resource` | boolean | If set, the group will only be accessible by its creator (default: False).
`workflow_id` | string | The workflow that all executions in this group are running.
`concurrency` | integer | How many concurrent executions will this group run.
`deployment_group_id` | string | The ID of the deployment group that this execution group was started from.
`execution_ids` | list | IDs of all executions belonging to this group
`status` | string | Aggregate status of the executions in this group.

## List Execution Groups

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/execution-groups
```

```python
# Using CloudifyClient
groups = client.execution_groups.list()
groups_for_group = client.execution_groups.list(deployment_group_id='g1')
```

> Response Example

```json
{
  "items": [
    {
        "concurrency": 5,
        "created_at": "2021-04-27T10:29:10.350Z",
        "created_by": "admin",
        "deployment_group_id": "g1",
        "execution_ids": [
            "f89a7998-eb29-44fb-a5da-f565405ac6b2"
        ],
        "id": "9159be07-6741-482c-ab99-9ee6894122b9",
        "private_resource": false,
        "resource_availability": "tenant",
        "status": "terminated",
        "tenant_name": "default_tenant",
        "visibility": "tenant",
        "workflow_id": "create_deployment_environment"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 1,
      "offset": 0,
      "size": 1000
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/execution-groups"`

Lists all execution groups.
### Query Parameters
* `deployment_group_id`: Filter execution group by their creator deployment group ID

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `ExecutionGroup` resources.


## Get Execution

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/execution-groups/<group-id>"
```

```python
# Using CloudifyClient
client.execution_groups.get('<group-id>')

# Using requests
url = 'http://<manager-ip>/api/v3.1/execution-groups/<execution_id>'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
)
response.json()
```

> Response Example

```json
{
    "concurrency": 5,
    "created_at": "2021-04-27T10:29:10.350Z",
    "created_by": "admin",
    "deployment_group_id": "g1",
    "execution_ids": [
        "f89a7998-eb29-44fb-a5da-f565405ac6b2"
    ],
    "id": "9159be07-6741-482c-ab99-9ee6894122b9",
    "private_resource": false,
    "resource_availability": "tenant",
    "status": "terminated",
    "tenant_name": "default_tenant",
    "visibility": "tenant",
    "workflow_id": "create_deployment_environment"
}
```

`GET "{manager-ip}/api/v3.1/executions/{execution-id}"`

Gets an execution.

This is useful for polling execution group status, which works similarly to
polling a single execution status. The execution group status is:
* `pending` if all the executions are `pending`
* `started` if some executions are `started`, even if there are already finished
  executions
* `terminated` if all executions have ended and none have failed
* `failed` if all executions have ended, and at least one have failed

### Response
An `ExecutionGroup` resource.


## Start multiple executions - start an Execution Group

> Request Example

```shell
$ curl -X POST \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"deployment_group_id": "<group-id>", "workflow_id": "install"}' \
    "http://<manager_ip>/api/v3.1/execution-groups"
```

```python
# Using CloudifyClient
client.execution_groups.start(
  deployment_id='<deployment-id>',
  workflow_id='install',
  default_parameters={'param1': 'value'},
  parameters={'deployment_id1': {'param1': 'override'}},
  concurrency=10,
)
```

`POST -d '{"deployment_group_id": "<group-id>", "workflow_id": "<workflow-id>"}' "{manager-ip}/api/v3.1/execution-groups"`

Starts an execution group. This starts an execution for every deployment in
the target deployment group.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`workflow_id` | string | The workflow id/name to execute.
`deployment_group_id` | string | Start an execution for every deployment in this group.
`default_parameters` | object | Parameters for all executions in the group.
`parameters` | object | Parameter overrides keyed by deployment ID
`force` | boolean | Same meaning as for a single execution start
`concurrency` | integer | Run up to this many executions at a time

### Specifying parameters
When deciding the parameters to use for each execution in the group, the `default_parameters`
are merged with overrides from `parameters`.
`parameters` is an object mapping deployment ID to an object containing parameter overrides.
For each deployment in the deployment group, the overrides are merged with the
default parameters.

### Response
An `ExecutionGroup` resource.

## Cancel/Resume an Execution Group

> Request Example

```shell
curl -X POST \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"action": "cancel"}'
    "http://<manager-ip>/api/v3.1/execution-groups/<group-id>"
```

```python
# Using CloudifyClient
client.execution_groups.cancel('<group-id>')

# Using requests
url = 'http://<manager-ip>/api/v3.1/execution-groups/<group-id>'
headers = {
    'Content-Type': 'application/json',
    'Tenant': '<manager-tenant>',
}
payload ={'action': 'cancel'}
response = requests.post(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    json=payload,
)
response.json()
```

`POST -d '{"action":"<action-method>"}' "{manager-ip}/api/v3.1/execution-groups/{group-id}"`

Cancels or resumes an execution group.

This cancels or resumes all the executions belonging to this group.

When cancelling, executions that are still queued, will be put in the cancelled state immediately.
When resuming, executions that never started to run, will have the resume flag set nonetheless.

Each action's semantics are the same as in their single-execution case.

### URI Parameters
* `group-id`: The id of the execution group.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`action` | string | The method to perform: `cancel`, `force-cancel`, `kill`, `resume`, or `force-resume`.

### Response
An `ExecutionGroup` resource.


## Attach target success/failure groups

> Request Example

```shell
curl -X PATCH \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"success_group_id": "g1"}'
    "http://<manager-ip>/api/v3.1/execution-groups/<group-id>"
```

```python
# Using CloudifyClient
client.execution_groups.set_target_group(
    '<group-id>',
    success_group='g1',
    failed_group='g2'
)

```
`PATCH -d '{"success_group_id":"<dep-group>"}' "{manager-ip}/api/v3.1/execution-groups/{group-id}"`

Set target deployment groups, success and failure: deployments, for which the
execution in this execution-group succeeds, will be added to the "success"
target deployment group. Deployments, for which the execution in this
execution-group fails, will be added to the "failure" target deployment group.

If an execution is cancelled, the deployment will be added to neither group.

The target group must already exist.

### URI Parameters
* `group-id`: The id of the execution group.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`success_group_id` | string | The "success" target deployment group ID
`failure_group_id` | string | The "failure" target deployment group ID

### Response
An `ExecutionGroup` resource.


## Change execution-group concurrency

> Request Example

```shell
curl -X PATCH \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"concurrency": 15}'
    "http://<manager-ip>/api/v3.1/execution-groups/<group-id>"
```

```python
# Using CloudifyClient
client.execution_groups.set_concurrency(
    '<group-id>',
    concurrency=15,
)

```
`PATCH -d '{"concurrency":15}' "{manager-ip}/api/v3.1/execution-groups/{group-id}"`

Set the concurrency parameter of the execution group. De-queueing executions
will use the new setting. Note: setting concurrency to 0, effectively pauses
the group.

### URI Parameters
* `group-id`: The id of the execution group.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`concurrency` | integer | The new concurrency setting, a nonnegative integer

### Response
An `ExecutionGroup` resource.

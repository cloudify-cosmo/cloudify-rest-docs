# Executions

## The Execution Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | A unique identifier for the execution.
`workflow_id` | string | The id/name of the workflow the execution is of.
`blueprint_id` | string | The id of the blueprint the execution is in the context of.
`deployment_id` | string | The id of the deployment the execution is in the context of.
`status` | string | The executions status.
`error` | string | The execution's error message on execution failure.
`created_at` | datetime | The time the execution was queued at.
`created_by` | string | The name of the user that created the execution.
`tenant_name` | string | The name of the tenant that owns the execution.
`parameters` | object | A dict of the workflow parameters passed when starting the execution.
`is_system_workflow` | boolean | true if the execution is of a system workflow.


## Get Execution

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3/executions/<execution-id>?_include=id"
```

```python
# Using CloudifyClient
client.executions.get(execution_id='<execution_id>', _include=['id'])

# Using requests
url = 'http://<manager-ip>/api/v3/executions/<execution_id>'
headers = {'Tenant': 'default_tenant'}
querystring = {'_include': 'id'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', 'password'),
    headers=headers,
    params=querystring,
)
response.json()
```

> Response Example

```json
{
  "id": "ca3d7413-c8af-41a3-b864-571cef25899b"
}
```


`GET "{manager-ip}/api/v3/executions/{execution-id}"`

Gets an execution.

### URI Parameters
* `execution-id`: The id of the execution.

### Response
An `Execution` resource.



## List Executions

> Request Example

```shell
$ curl -X GET "<manager-ip>/api/v3/executions?_include=id
```

```python
# Using CloudifyClient
executions = client.executions.list(_include=['id'])
for execution in executions:
  print execution

# Using requests
url = 'http://<manager-ip>/api/v3/executions'
headers = {'Tenant': 'default_tenant'}
querystring = {'_include': 'id'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', 'password'),
    headers=headers,
    params=querystring,
)
```

> Response Example

```json
{
  "items": [
    {
      "id": "dab3d7ac-fef0-4b8b-912f-5611cc8f20b5"
    },
    {
      "id": "ca3d7413-c8af-41a3-b864-571cef25899b"
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

`GET "{manager-ip}/api/v3/executions"`

Lists all executions.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Execution` resources.


## Start Execution

> Request Example

```shell
$ curl -X POST \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"deployment_id": "<deployment-id>", "workflow_id": "install"}' \
    "http://<manager_ip>/api/v3/executions?_include=id"
```

```python
# Using CloudifyClient
client.executions.start(deployment_id='<deployment-id>', workflow_id='install')

# Using requests
url = 'http://<manager-ip>/api/v3/executions'
headers = {
    'Content-Type': 'application/json',
    'Tenant': 'default_tenant',
}
querystring = {'_include': 'id'}
payload ={
    'deployment_id': '<deployment-id>',
    'workflow_id': 'install',
}
response = requests.post(
    url,
    auth=HTTPBasicAuth('<manager-username>', 'password'),
    headers=headers,
    params=querystring,
    json=payload,
)
response.json()
```

> Response example

```json
{
  "id": "33dd51d4-5e24-4034-8ed6-2150cdbd98f7"
}
```

`POST -d '{"deployment_id":{deployment-id}, "workflow_id":"<workflow-id>"}' "{manager-ip}/api/v3/executions"`

Starts an execution.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`workflow_id` | string | The workflow id/name to execute.
`deployment_id` | string | The id of the deployment the workflow should be executed on.
`allow_custom_parameters` | boolean | Specifies whether to allow custom parameters, which are not present in the parameters schema of the workflow, to be passed when starting the execution (default=false).
`parameters` | object | A dictionary containing parameters to be passed to the execution when starting it.
`force` | boolean | Specifies whether to force the workflow execution in a case where there is already a running execution in the context of the same deployment or system wide workflow (default=false).

### Response
An `Execution` resource.


## Cancel Execution

> Request Example

```shell
curl -X POST \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"deployment_id": "dep", "action": "cancel"}'
    "http://<manager-ip>/api/v3/executions/<execution-id>?_include=id"
```

```python
# Using CloudifyClient
client.executions.cancel(execution_id='<execution-id>')

# Using requests
url = 'http://<manager-ip>/api/v3/executions/<execution-id>'
headers = {
    'Content-Type': 'application/json',
    'Tenant': 'default_tenant',
}
querystring = {'_include': 'id'}
payload ={'deployment_id': 'dep', 'action': 'cancel'}
response = requests.post(
    url,
    auth=HTTPBasicAuth('<manager-username>', 'password'),
    headers=headers,
    params=querystring,
    json=payload,
)
response.json()
```
> Example Response

```json
{
  "id": "e7821510-c536-47f3-8fe7-691a91dc91ff"
}
```

`POST -d '{"deployment_id":{deployment-id}, "action":"<action-method>"}' "{manager-ip}/api/v3/executions/{execution-id}"`

Cancels an execution.

If passing `cancel` as the action fails to cancel the execution, `force-cancel` can be passed which will then kill the process running the execution.


### URI Parameters
* `execution-id`: The id of the execution.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`action` | string | The cancellation method to perform: `cancel` or `force-cancel`

### Response
An `Execution` resource.


## Update Execution

> Request Example

```shell
curl -X PATCH \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"status": "cancelled"}' \
    "http://<manager-ip>/api/v3/executions/<execution-id>?_include=id"
```

```python
# Using CloudifyClient
client.executions.update(execution_id='<execution_id>', status='cancelled')

# Using requests
url = 'http://<manager-ip>/api/v3/executions/<execution-id>'
headers = {
    'Content-Type': 'application/json',
    'Tenant': 'default_tenant',
}
querystring = {'_include': 'id'}
payload ={'status': 'cancelled'}
response = requests.patch(
    url,
    auth=HTTPBasicAuth('<manager-username>', 'password'),
    headers=headers,
    params=querystring,
    json=payload,
)
response.json()
```

> Example Response

```json
{
  "id": "21236984-9d1f-445e-8bca-f923175441f1"
}
```

`PATCH "{manager-ip}/api/v3/executions/{execution-id}"`

Updates an execution.

### URI Parameters
* `execution-id`: The id of the execution.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`status` | string | The new status of the execution.

### Response
An `Execution` resource.

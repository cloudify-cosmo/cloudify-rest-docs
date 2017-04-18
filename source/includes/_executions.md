# Executions

## The Execution Resource

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
`id` | string | A unique identifier for the execution.
`workflow_id` | string | The id/name of the workflow the execution is of.
`blueprint_id` | string | The id of the blueprint the execution is in the context of.
`deployment_id` | string | The id of the deployment the execution is in the context of.
`status` | string | The executions status.
`error` | string | The execution's error message on execution failure.
`created_at` | datetime | The time the execution was queued at.
`parameters` | object | A dict of the workflow parameters passed when starting the execution.
`is_system_workflow` | boolean | true if the execution is of a system workflow.


## Get Execution

> Request Example

```shell
$ curl -X GET "<manager-ip>/api/v2.1/executions/2b422fb2-38b4-4b02-95ac-e9b91390599d?
deployment_id=hello1&_include=id,status,created_at"
```

```python
# Python Client-
print client.executions.get(execution_id='2b422fb2-38b4-4b02-95ac-e9b91390599d',
                            _include=['id','created_at','status'])

# Python Requests-
url = "http://<manager-ip>/api/v2.1/executions/2b422fb2-38b4-4b02-95ac-e9b91390599d"
querystring = {"deployment_id":"hello1","_include":"id,status,create_at"}
headers = {'content-type': "application/json"}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
print(response.text)
```

> Response Example

```json
{
  "status": "terminated",
  "created_at": "2015-11-18 06:54:14.238731",
  "workflow_id": "install",
  "is_system_workflow": false,
  "parameters": {},
  "blueprint_id": "hello-world",
  "deployment_id": "hello1",
  "error": "",
  "id": "2b422fb2-38b4-4b02-95ac-e9b91390599d"
}
```


`GET "{manager-ip}/api/v2.1/executions/{execution-id}?deployment_id={deployment_id}"`

Gets an execution.

### URI Parameters
* `execution-id`: The id of the execution.

### Response
An `Execution` resource.



## List Executions

> Request Example

```shell
$ curl -X GET "<manager-ip>/api/v2.1/executions?deployment_id=<deployment-id>&_include=id,status,
workflow_id,created_at"
```

```python
# Python Client-
executions = client.executions.list(deployment_id='<deployment-id>',_include=['id','status',
                                    'workflow_id','created_at'])
for execution in executions:
  print execution

# Python Requests-
url = "http://<manager-ip>/api/v2.1/executions"
querystring = {"deployment_id":"<deployments-id>","_include":"id,created_at,workflow_id,status"}
headers = {'content-type': "application/json"}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
print(response.text)
```

`GET "{manager-ip}/api/v2.1/executions?deployment_id={deployment-id}"`

Lists all executions.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Execution` resources.


## Start Execution

> Request Example

```shell
$ curl -X POST -H "Content-Type: application/json" -d '{"deployment_id":"sample-dep",
"workflow_id":"install"}' "<manager-ip>/api/v2.1/executions"
```

```python
# Python Client-
client.executions.start(deployment_id='<deployment-id>', workflow_id='install')

#Python Requests-
url = "http://<manager-ip>/api/v2.1/executions"
payload = "{\"deployment_id\":\"<deployment-id>\",\"workflow_id\":\"install\"}"
headers = {'content-type': "application/json"}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
```

`POST -d '{"deployment_id":{deployments-id}, "workflow_id":"<workflow-id>"}' "{manager-ip}/api/v2.1/executions"`

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
$ curl -X POST -H "Content-Type: application/json" -d '{"deployment_id":"<deployment-id>",
"action":"cancel"}' "<manager-ip>/api/v2.1/executions/<execution-id>"
```

```python
# Python Client-
client.executions.cancel(execution_id='<execution-id>')

# Python Requests-
url = "http://<manager-ip>/api/v2.1/executions/<execution-id>"
payload = "{\"deployment_id\":\"<deployment-id>\",\"action\":\"cancel\"}"
headers = {'content-type': "application/json"}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
```

`POST -d '{"deployment_id":{deployment-id}, "action":"<action-method>"}' "{manager-ip}/api/v2.1/executions/{execution-id}"`

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
`PATCH "{manager-ip}/api/v2.1/executions/{execution-id}"`

Updates an execution.

### URI Parameters
* `execution-id`: The id of the execution.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`status` | string | The new status of the execution.

### Response
An `Execution` resource.

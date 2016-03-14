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
`parameters` | object | A dict of the workflow parameters passed when starting the execution.
`is_system_workflow` | boolean | true if the execution is of a system workflow.


## Get Execution

> Request Example

```shell
$ curl -XGET http://localhost/api/v2/executions/2b422fb2-38b4-4b02-95ac-e9b91390599d
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


`GET /api/v2/executions/{execution-id}`

Gets an execution.

### URI Parameters
* execution-id: The id of the execution.

### Response
An `Execution` resource.



## List Executions
`GET /api/v2/executions`

Lists all executions.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Execution` resources.


## Start Execution
`POST /api/v2/executions`

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
`POST /api/v2/executions/{execution-id}`

Cancels an execution.

If passing `cancel` as the action fails to cancel the execution, `force-cancel` can be passed which will then kill the process running the execution.


### URI Parameters
* execution-id: The id of the execution.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`action` | string | The cancellation method to perform: `cancel` or `force-cancel`

### Response
An `Execution` resource.


## Update Execution
`PATCH /api/v2/executions/{execution-id}`

Updates an execution.

### URI Parameters
* execution-id: The id of the execution.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`status` | string | The new status of the execution.

### Response
An `Execution` resource.

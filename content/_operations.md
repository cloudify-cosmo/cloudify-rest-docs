# Operations

## The Operation Resource

```python
# Include this code when using the Cloudify Python client-
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
        host='<manager-ip>',
        username='<manager-username>',
        password='<manager-password>')
```

Represents a stored operation, as part of a tasks graph

### Attributes:

Attribute | Type | Description
--------- | ---- | -----------
`id` | string | Unique identifier of this operation
`name` | string | Name of this operation
`state` | string | The state of this operation, eg. PENDING, SENT or SUCCEEDED
`dependencies` | list | IDs of the operations that this operation depends on
`type` | string | Type of this operation, eg. RemoteWorkflowTask, LocalWorkflowTask or SubgraphTask
`parameters` | dict | Parameters as serialized by the operation class, to be used when reconstructing the operation
`tasks_graph` | string | ID of the tasks graph this operation belongs to

## List operations

> Request Example

```shell
$ curl -u user:password "http://<manager-ip>/api/v3.1/operations?graph_id=123"
```

```python
client.operations.list(graph_id)
```

> Response Example

```json
[
    {
        "id": "operation-id",
        "state": "PENDING",
        "dependencies": [],
        "type": "SubgraphTask",
        "name": "my-subgraph",
        "parameters": {}
    }
]
```


`GET "{manager-ip}/api/v3.1/operations"`

Lists operations. To be used when filtering by a tasks graph id. This is the primary method
of bulk-requesting operations when resuming a workflow.

### Query Parameters

Property | Type | Description
-------- | ---- | -----------
`graph_id` | string | Filter operations by this tasks graph


## Create operation

> Request Example

```shell
$ curl -u user:password -X PUT \
    -d '{"name": "abc", "graph_id": "123", "dependencies": [], "type": "RemoteWorkflowTask"}' \
    "http://<manager-ip>/api/v3.1/operations/<operation_id>"
```

```python
client.operations.create(operation_id, graph_id, name, type, parameters, dependencies)
```

> Response Example

```json
{
    "id": "operation-id",
    "state": "PENDING",
    "dependencies": [],
    "type": "SubgraphTask",
    "name": "my-subgraph",
    "parameters": {}
}
```

`PUT "{manager-ip}/api/v3.1/operations/{operation-id}"`
Creates a single operation. State defaults to PENDING. Note that instead of using this method, it is faster to create many operations in bulk while creating the tasks graph.

### Request Body

Property | Type | Description
-------- | ---- | -----------
`name` | string | Name of the operation
`graph_id` | string | ID of the tasks graph this operation belongs to
`state` | string | The state of this operation, eg. PENDING, SENT or SUCCEEDED
`dependencies` | list | IDs of the operations that this operation depends on
`type` | string | Type of this operation, eg. RemoteWorkflowTask, LocalWorkflowTask or SubgraphTask
`parameters` | dict | Parameters as serialized by the operation class, to be used when reconstructing the operation


## Update operation

> Request Example

```shell
$ curl -u user:password -X PATCH \
    -d '{"state": "FAILED"}' \
    "http://<manager-ip>/api/v3.1/operations/<operation_id>"
```

```python
client.operations.update(operation_id, state)
```

> Response Example

```json
{
    "id": "operation-id",
    "state": "FAILED",
    "dependencies": [],
    "type": "SubgraphTask",
    "name": "my-subgraph",
    "parameters": {}
}
```

`PATCH "{manager-ip}/api/v3.1/operations/{operation-id}"`
Updates the state of an operation. Other attributes are immutable.

### Request Body

Property | Type | Description
-------- | ---- | -----------
`state` | string | The state of this operation, eg. PENDING, SENT or SUCCEEDED


## Delete operation

> Request Example

```shell
$ curl -u user:password -X DELETE \
    "http://<manager-ip>/api/v3.1/operations/<operation_id>"
```

```python
client.operations.delete(operation_id)
```


`DELETE "{manager-ip}/api/v3.1/operations/{operation-id}"`
Deletes an operation. Note that operations which are terminated should still be stored in persistent storage, and should have their state updated to SUCCEEDED or FAILED rather than be deleted.

### Response
No content - HTTP code 204.

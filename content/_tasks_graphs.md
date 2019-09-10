# Tasks graphs

## The TasksGraph Resource

```python
# Include this code when using the Cloudify Python client-
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
        host='<manager-ip>',
        username='<manager-username>',
        password='<manager-password>')
```

Represents a stored tasks graph, created as part of an execution.

### Attributes:

Attribute | Type | Description
--------- | ---- | -----------
`id` | string | Unique identifier of this tasks graph
`execution_id` | string | ID of the execution that created this tasks graph
`name` | string | A label for this tasks graph, so that multiple graphs for a single execution can be distinguished

## List tasks graphs

> Request Example

```shell
$ curl -u user:password "http://<manager-ip>/api/v3.1/tasks_graphs?execution_id=123&name=abc"
```

```python
client.tasks_graphs.list(execution_id, name)
```

> Response Example

```json
{
    "id": "aaabbbccc",
    "execution_id": "123",
    "name": "abc"
}
```


`GET "{manager-ip}/api/v3.1/tasks_graphs"`

Lists tasks graphs. This is useful when filtering by execution ID.

### Query Parameters

Property | Type | Description
-------- | ---- | -----------
`execution_id` | string | Filter tasks graphs for this execution
`name` | string | Filter tasks graphs with this name


## Create tasks graph

> Request Example

```shell
$ curl -u user:password -X POST \
    -d '{"name": "abc", "execution_id": "123"}' \
    "http://<manager-ip>/api/v3.1/tasks_graphs"
```

```python
client.tasks_graphs.create(execution_id, name, operations=operations)
```

> Response Example

```json
{
    "id": "aaabbbccc",
    "execution_id": "123",
    "name": "abc"
}
```

`POST "{manager-ip}/api/v3.1/tasks_graphs"`

Creates a tasks graph. This can optionally also create a tasks graph with operations in it, where operations is a list of dicts containing a representation of each operation, as returned by its `dump` method. Operations can also be created one-by-one, however this method should be used instead for performance improvement.

### Request Body

Property | Type | Description
-------- | ---- | -----------
`execution_id` | string | ID of the current execution
`name` | string | An additional label for the tasks graph to distinguish multiple graphs for the same execution
`operations` | list | Serialized operations to create in this tasks graph

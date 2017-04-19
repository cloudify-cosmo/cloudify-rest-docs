# Cluster

## The ClusterState Resource

<aside class="notice">
This section describes the API features that are included with the Cloudify Premium Edition
</aside>

```python
# Include this code when using the Cloudify Python client-
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
        host='<manager-ip>',
        username='<manager-username>',
        password='<manager-password>')
```

The ClusterState resource represents the current state of a Cloudify Manager cluster.

### Attributes:

Attribute | Type | Description
--------- | ---- | -----------
`initialized` | boolean | Whether this node is part of a cluster.
`consul` | dict | Detailed state of the consul cluster being part of the manager infrastructure.
`error` | string | Description of a fatal error that occured during cluster configuration or operation, if any.
`logs` | list | Logs of the cluster operations on the current node.

## Get Cluster State

> Request Example

```shell
$ curl -u user:password "http://<manager-ip>/api/v3/cluster"
```

```python
client.cluster.status()
```

> Response Example (cluster not initialized)

```json
{
    "initialized": false
}
```

> Response Example

```json
{
    "initialized": true,
    "consul": {
        "leader": "172.20.0.3:8300"
    },
    "error": null,
    "logs": [
        {
            "message": "HA Cluster configuration complete",
            "timestamp": 1485778546965628,
            "cursor": "opaque cursor value"
        }
    ]
}
```

`GET "{manager-ip}/api/v3/cluster"`

Retrieves the current cluster state. The `logs` and `error` fields are hidden by
default, but can be added to the response if specified using the `_include`
query parameter.

### Response
A `ClusterState` resource.

### URI Parameters
* `since`: When including logs, fetch only logs that are more recent than this cursor value.


## Put Cluster State

> Request Example

```python
# starting a cluster
client.cluster.start(
    host_ip='172.20.0.2',
    node_name='manager',
)
# joining a cluster
client.cluster.join(
    host_ip='172.20.0.3',
    node_name='another-manager',
    credentials='<REDACTED>'
)
```

```shell
$ curl -X PUT -H "Content-Type: application/json" -u user:password -d '{"host_ip": "172.20.0.2", "node_name": "manager", "credentials": "<REDACTED>"}' "http://<manager-ip>/api/v3/cluster"
```


> Response Example

```json
{
    "initialized": false
}
```

`PUT "{manager-ip}/api/v3/cluster"`

Starts the cluster mechanisms on the current Cloudify Manager. If the `join_addrs`
parameter is provided, joins an existing cluster, otherwise bootstraps a new
cluster.
When joining a cluster, the "credentials" parameter is required. To generate
credentials for use by a new node, use the "Add cluster node" endpoint first.
Only admin users can execute this operation.

### Request Body

Property | Type | Description
-------- | ---- | -----------
host_ip | string | The externally accessible IP of this node.
node_name | string | A unique name for this node to be used internally within the cluster.
credentials | string | When joining a node, provide the credentials received from the cluster active node.
join_addrs | list | IPs of the nodes to connect with. If not provided, a new cluster will be created.


### Response

A `ClusterState` resource.


## Patch Cluster State

> Request Example

```python
client.cluster.update(
    config_key='config_value'
)
```

```shell
$ curl -X PATCH -H "Content-Type: application/json" -d '{"config_key": "config_value"}' -u user:password "http://<manager-ip>/api/v3/cluster"
```

> Response Example

```json
{
    "initialized": true,
    "error": null
}
```

`PATCH "{manager-ip}/api/v3/cluster"`

Updates the cluster configuration. The request body is a mapping containing
arbitrary settings, which can be used by either the core cluster mechanisms,
or user-specific extensions, if any.
Only admin users can execute this operation.

### Response

A `ClusterState` resource.


## The ClusterNode resource

The ClusterNode resource represents the state of a node in the cluster

### Attributes:

Attribute | Type | Description
--------- | ---- | -----------
`master`| boolean | Whether this node is the current cluster master.
`name` | string | The name of this node.
`host_ip` | string | The externally accessible IP of this node.
`online` | boolean | Whether this node is currently online.
`initialized` | boolean | Whether the node has been successfully joined to the cluster.
`credentials` | dict | Credentials used by this node to join the cluster.


## List Cluster Nodes

> Request Example

```python
client.cluster.nodes.list()
```

```shell
$ curl --header -u user:password "http://<manager-ip>/api/v3/cluster/nodes"
```

> Response Example

```json
{
    "items":
    [
        {
            "initialized": true,
            "online": true,
            "master": true,
            "host_ip": "172.20.0.2",
            "name": "cloudify_manager_LMJZA2",
            "credentials": "<REDACTED>"
        }
    ]
}
```

`GET "{manager-ip}/api/v3/cluster/nodes"`

Lists all nodes in the cluster.

### Response

Field | Type | Description
----- | ---- | -----------
`items` | list | A list of `ClusterNode` resources


## Get Cluster Node

> Request Example

```python
client.cluster.nodes.get("<node-id>")
```

```shell
$ curl --header -u user:password "http://<manager-ip>/api/v3/cluster/nodes/<node-id>"
```

> Response Example

```json
{
    "initialized": true,
    "online": true,
    "master": true,
    "host_ip": "172.20.0.2",
    "name": "cloudify_manager_LMJZA2",
    "credentials": "<REDACTED>"
}
```

`GET "{manager-ip}/api/v3/cluster/nodes/{node-id}"`

Fetches the details of a node in the cluster.

### URI Parameters
* `node-id`: The ID of the node to remove from the cluster

### Response

A `ClusterNode` resource.

## Add Cluster Node

> Request Example

```python
client.cluster.nodes.add(host_ip='172.20.0.3', node_name='second-manager')
```

```shell
$ curl -u user:password -d '{"host_ip": "172.20.0.3", "node_name": "second-manager"}' "http://<manager-ip>/api/v3/cluster/nodes"
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64')
}

var settings = {
  "url": "http://<manager-ip>/api/v3/cluster/nodes",
  "method": "GET",
  "headers": headers,
  "contentType": "application/json"
  "data": JSON.stringify({
      "host_ip": "172.20.0.3",
      "node_name": "second-manager"
  })
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> Response Example

```json
{
    "initialized": false,
    "online": false,
    "master": false,
    "host_ip": "172.20.0.3",
    "name": "second-manager",
    "credentials": "<REDACTED>"
}
```

`PUT "{manager-ip}/api/v3/cluster/nodes/{node-name}"`

Adds a node to the cluster. This prepares the cluster for contacting the new node,
runs validations and generates credentials for use by a new node. The received
credentials are passed in the "Join cluster" ("Put Cluster State") API call.


## Delete Cluster Node

> Request Example

```python
client.cluster.nodes.delete("<node-id>")
```

```shell
$ curl -X DELETE -u user:password "http://<manager-ip>/api/v3/cluster/nodes/<node-id>"
```

> Response Example

```json
{
    "initialized": true,
    "online": true,
    "master": true,
    "host_ip": "172.20.0.2",
    "name": "cloudify_manager_LMJZA2"
}
```

`DELETE "{manager-ip}/api/v3/cluster/nodes/{node-id}"`

Removes a node from the cluster. The node disconnects from the cluster and
disables all cluster mechanisms. You cannot rejoin it to the cluster.
Only admin users can execute this operation.

### URI Parameters
* `node-id`: The ID of the node to remove from the cluster

### Response
A `ClusterNode` resource representing the node that was removed from the cluster.

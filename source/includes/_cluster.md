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
`encryption_key` | string | Encryption key used for inter-cluster communication (only visible by admin users).
`consul` | dict | Detailed state of the consul cluster being part of the manager infrastructure.
`error` | string | Description of a fatal error that occured during cluster configuration or operation, if any.
`logs` | list | Logs of the cluster operations on the current node.

## Get Cluster State

> Request Example

```shell
$ curl --header "tenant: <tenant-name>" -u user:password "http://<manager-ip>/api/v3/cluster"
```

```python
client.cluster.status()
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/cluster",
  "method": "GET",
  "headers": headers
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
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
    "encryption_key": "<REDACTED>",
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
client.cluster.start(
    host_ip='172.20.0.2',
    node_name='manager',
    encryption_key='<REDACTED>'
)
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/cluster/",
  "method": "PUT",
  "headers": headers,
  "contentType": "application/json"
  "data": JSON.stringify({
      "host_ip": "172.20.0.2",
      "node_name": "manager",
      "encryption_key": "<REDACTED>"
  })
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```shell
$ curl -X PUT -H "Content-Type: application/json" -H "tenant: <tenant-name>" -u user:password -d '{"host_ip": "172.20.0.2", "node_name": "manager", "encryption_key": "<REDACTED>"}' "http://<manager-ip>/api/v3/cluster"
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
Only admin users can execute this operation.

### Request Body

Property | Type | Description
-------- | ---- | -----------
host_ip | string | The externally accessible IP of this node.
node_name | string | A unique name for this node to be used internally within the cluster.
encryption_key | string | A base64-encoded 16-byte encryption key, identical for all the nodes in the cluster.
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

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/cluster/",
  "method": "PATCH",
  "headers": headers,
  "contentType": "application/json"
  "data": JSON.stringify({
      "config_key": "config_value"
  })
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```shell
$ curl -X PATCH -H "Content-Type: application/json" -H "tenant: <tenant-name>" -d '{"config_key": "config_value"}' -u user:password "http://<manager-ip>/api/v3/cluster"
```

> Response Example

```json
{
    "initialized": true,
    "error": null,
    "encryption_key": "<REDACTED>"
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


## List Cluster Nodes

> Request Example

```python
client.cluster.nodes.list()
```

```shell
$ curl --header "tenant: <tenant-name>" -u user:password "http://<manager-ip>/api/v3/cluster/nodes"
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/cluster/nodes",
  "method": "GET",
  "headers": headers
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
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
            "name": "cloudify_manager_LMJZA2"
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
$ curl --header "tenant: <tenant-name>" -u user:password "http://<manager-ip>/api/v3/cluster/nodes/<node-id>"
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/cluster/nodes/<node-id>",
  "method": "GET",
  "headers": headers
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
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

`GET "{manager-ip}/api/v3/cluster/nodes/{node-id}"`

Fetches the details of a node in the cluster.

### URI Parameters
* `node-id`: The ID of the node to remove from the cluster

### Response

A `ClusterNode` resource.


## Delete Cluster Node

> Request Example

```python
client.cluster.nodes.delete("<node-id>")
```

```shell
$ curl -X DELETE --header "tenant: <tenant-name>" -u user:password "http://<manager-ip>/api/v3/cluster/nodes/<node-id>"
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/cluster/nodes/<node-id>",
  "method": "DELETE",
  "headers": headers
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
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

# Cluster

## The ManagerItem resource

The ManagerItem resource represents a node in the cluster

### Attributes:

Attribute | Type | Description
--------- | ---- | -----------
`id`| number | The id of the manager in the cluster.
`hostname` | string | The hostname of this node.
`private_ip` | string | The internal IP of the manager used for internal communication.
`public_ip` | string | The externally accessible IP of this node.
`version` | string | Cloudify version of the node.
`edition` | string | Cloudify edition: community / premium / spire.
`distribution` | string | Distribution of the OS the node is running on.
`distro_release` | string | Distribution release of the OS the node is running on.
`fs_sync_node_id` | string | Syncthing node ID used for FS replication.
`networks` | dict | A dictionary of the networks associated with the node.
`ca_cert_content` | string | CA certificate used by the manager.


## List Cluster Nodes

> Request Example

```python
client.manager.get_managers()
```

```shell
$ curl --header -u user:password "http://<manager-ip>/api/v3.1/managers"
```

> Response Example

```json
{
    "items":
    [
        {
            "id": 0,
            "hostname": "node1.openstack.local",
            "private_ip": "172.20.0.2",
            "public_ip": "191.31.72.16",
            "version": "5.0.0",
            "edition": "premium",
            "distribution": "centos",
            "distro_release": "core",
            "fs_sync_node_id": "P56IOI7-MZJNU2Y-IQGDREY-...",
            "networks": {
                "default": "172.20.0.2",
                "network_2": "174.40.0.4"
            },
            "ca_cert_content": "CERT CONTENT"
        }
    ]
}
```

`GET "{manager-ip}/api/v3.1/managers"`

Lists all nodes in the cluster.

### Response

Field | Type | Description
----- | ---- | -----------
`items` | list | A list of `ManagerItem` resources


## Get Cluster Node

> Request Example

```python
client.manager.get_managers("<hostname>")
```

```shell
$ curl --header -u user:password "http://<manager-ip>/api/v3.1/managers/<hostname>"
```

> Response Example

```json
{
    "id": 0,
    "hostname": "node1.openstack.local",
    "private_ip": "172.20.0.2",
    "public_ip": "191.31.72.16",
    "version": "5.0.0",
    "edition": "premium",
    "distribution": "centos",
    "distro_release": "core",
    "fs_sync_node_id": "P56IOI7-MZJNU2Y-IQGDREY-...",
    "networks": {
        "default": "172.20.0.2",
        "network_2": "174.40.0.4"
    },
    "ca_cert_content": "CERT CONTENT"
}
```

`GET "{manager-ip}/api/v3.1/managers/{hostname}"`

Fetches the details of a node in the cluster.

### URI Parameters
* `hostname`: The hostname of the node to retrieve from the cluster

### Response

A `ManagerItem` resource.


## Delete Cluster Node

> Request Example

```python
client.manager.remove_manager("<hostname>")
```

```shell
$ curl -X DELETE -u user:password "http://<manager-ip>/api/v3.1/managers/<hostname>"
```

> Response Example

```json
{
    "id": 0,
    "hostname": "node1.openstack.local",
    "private_ip": "172.20.0.2",
    "public_ip": "191.31.72.16",
    "version": "5.0.0",
    "edition": "premium",
    "distribution": "centos",
    "distro_release": "core",
    "fs_sync_node_id": "P56IOI7-MZJNU2Y-IQGDREY-...",
    "networks": {
        "default": "172.20.0.2",
        "network_2": "174.40.0.4"
    },
    "ca_cert_content": "CERT CONTENT"
}
```

`DELETE "{manager-ip}/api/v3.1/managers/{hostname}"`

Removes a node from the cluster. The node disconnects from the cluster and
disables all cluster mechanisms. You can rejoin it to the cluster.
The node is still connected to the DB of the cluster so it is highly 
recommended to dispose of it once removed.
Only admin users can execute this operation.

### URI Parameters
* `hostname`: The hostname of the node to remove from the cluster

### Response
A `ManagerItem` resource representing the node that was removed from the cluster.

## Cluster Status

**Supported for Cloudify Manager 5.0.5 and above.**

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/cluster-status"
```

```python
# Using ClodifyManager
client.cluster_status.get_status()

# Using requests
url = 'http://<manager-ip>/api/v3.1/cluster-status'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers
)
response.json()
```

> Response Example

```json
{
  "status": "OK",
  "services": {
    "manager": {
      "status": "OK",
      "nodes": {
        "cfy-manager": {
          "status": "OK",
          "version": "5.0.5",
          "public_ip": "172.20.0.2",
          "node_id": "89947217-e31b-4042-b68f-01576e02e27c",
          "private_ip": "172.20.0.2",
          "services": {
            <Cloudify manager's services status data>
      },
      "is_external": false
    },
    "db": {
      "status": "OK",
      "nodes": {
        "cfy-db": {
          "status": "OK",
          "version": "5.0.5",
          "public_ip": null,
          "node_id": "89947217-e31b-4042-b68f-01576e02e27c",
          "private_ip": "172.20.0.2",
          "services": {
            <DB's status data>
      },
      "is_external": false
    },
    "broker": {
      "status": "OK",
      "nodes": {
        "cfy-manager": {
          "status": "OK",
          "version": "5.0.5",
          "public_ip": null,
          "node_id": "89947217-e31b-4042-b68f-01576e02e27c",
          "private_ip": "172.20.0.2",
          "services": {
            "RabbitMQ": {
              "status": "Active",
              "is_remote": false,
              "extra_info": {
              }
            }
          }
        }
      },
      "is_external": false
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/cluster-status"`

Gets Cloudify cluster status.

### Getting summarised cluster status
Gets summarised cluster status and determines the return code based on it, i.e.   
return code 200 means: 'OK' or 'Degraded'; return code 500 means: 'FAIL'. 

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/cluster-status?summary=true"
```

```python
# Using ClodifyManager
client.cluster_status.get_status()

# Using requests
url = 'http://<manager-ip>/api/v3.1/cluster-status'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'summary': 'true'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring
)
response.json()
```

> Response Example

```json
{
  "status": "OK",
  "services": {}
}
```

`GET "{manager-ip}/api/v3.1/cluster-status?summary=true"`

Gets summary of Cloudify cluster status.

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`status` | string | The status of the cluster, can be `OK`, `Degraded` or `Fail`.
`services`| object | A dictionary containing the services data of the Cloudify cluster.

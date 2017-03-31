# Node Instances

## The NodeInstance Resource

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
`id` | string | The id of the node instance.
`deployment_id` | string | The id of the deployment the node instance belongs to.
`host_id` | string | The Compute node instance id the node is contained within.
`runtime_properties` | object | The runtime properties of the node instance.
`relationships` | list | The relationships the node has with other nodes.
`state` | string | The node instance state.
`version` | integer | A version attribute used for optimistic locking when updating the node instance.


## Get Node Instance

> Request Example

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/node-instances/vm_150f1"
```

```python
# Python Client-
print client.node_instances.get(node_instance_id='vm_150f1')

# Python Requests-
url = "http://<manager-ip>/api/v2.1/node-instances/vm_150f1"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/node-instances/vm_150f1",
  "method": "GET",
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> Response Example

```json
{
  "relationships": [
    {
      "target_name": "vm",
      "type": "cloudify.relationships.contained_in",
      "target_id": "vm_150f1"
    }
  ],
  "runtime_properties": {},
  "node_id": "http_web_server",
  "version": 1,
  "state": "uninitialized",
  "host_id": "vm_150f1",
  "deployment_id": "hello1",
  "id": "http_web_server_7e234"
}
```

`GET "{manager-ip}/api/v2.1/node-instances/{node-instance-id}"`

Gets a node instance.

### URI Parameters
* `node-instance-id`: The id of the node instance.

### Response
A `NodeInstance` resource.


## List Node Instances

> Request Example

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/node-instances"
```

```python
# Python Client-
instances = client.node_instances.list()
for instance in instances:
    print instance

# Python Requests-
url = "http://<manager-ip>/api/v2.1/node-instances"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/node-instances",
  "method": "GET",
  "headers": {"content-type": "application/json"},
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> Response Example

```json
{
  "items": [
    {
      "relationships": [
        {
          "target_name": "nodejs_host",
          "target_id": "nodejs_host_7f66d",
          "type": "cloudify.relationships.contained_in"
        }
      ],
      "version": null,
      "runtime_properties": {},
      "state": "uninitialized",
      "node_id": "nodejs",
      "host_id": "nodejs_host_7f66d",
      "deployment_id": "d1",
      "scaling_groups": [],
      "id": "nodejs_d5a3e"
    },
    {
      "relationships": [
        {
          "target_name": "nodejs_host",
          "target_id": "nodejs_host_83396",
          "type": "cloudify.relationships.contained_in"
        }
      ],
      "version": null,
      "runtime_properties": {},
      "state": "uninitialized",
      "node_id": "nodejs",
      "host_id": "nodejs_host_83396",
      "deployment_id": "d1",
      "scaling_groups": [],
      "id": "nodejs_836e3"
    },
    {
      "relationships": [
        {
          "target_name": "mongod_host",
          "target_id": "mongod_host_fa1d1",
          "type": "cloudify.relationships.contained_in"
        }
      ],
      "version": null,
      "runtime_properties": {},
      "state": "uninitialized",
      "node_id": "mongod",
      "host_id": "mongod_host_fa1d1",
      "deployment_id": "d1",
      "scaling_groups": [],
      "id": "mongod_9961b"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 28,
      "offset": 0,
      "size": 10000
    }
  }
}
```

`GET "{manager-ip}/api/v2.1/node-instances"`

Lists all node instances.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `NodeInstance` resources.


## Update Node Instance

> Requests Example

```shell
$ curl -X PATCH -H "Content-Type: application/json" -d 'version=0&state=starting&
runtime_properties={key: value}' "http://<manager-ip>/api/v2.1/node-instances?id=nodejs_host_7f66d"
```

```python
# Python Client-
client.node_instances.update(node_instance_id='nodejs_host_7f66d', state='starting',
                             runtime_properties={'key': 'value'}, version=0)

# Python Requests-
url = "http://<manager-ip>/api/v2.1/node-instances"
querystring = {"id":"<node-instance-id>"}
headers = {'content-type': "application/json"}
response = requests.request("PATCH", url, headers=headers, params=querystring)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/node-instances?id=nodejs_host_7f66d",
  "method": "PATCH",
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> Response Example

```json
{
    "relationships": [
      {
      "target_name": "nodecellar_security_group",
      "type": "cloudify.openstack.server_connected_to_security_group",
      "target_id": "nodecellar_security_group_deb08"
      }
    ],
    "runtime_properties": {"key": "value"},
    "state": "starting",
    "version": 3,
    "host_id": "nodejs_host_7f66d",
    "deployment_id": "d1",
    "scaling_groups": [],
    "id": "nodejs_host_7f66d",
    "node_id": "nodejs_host"
}
```

`PATCH "{manager-ip}/api/v2.1/node-instances?id={node-instance-id}"`

Updates a node instance.

### URI Parameters
* `node-instance-id`: The id of the node instance.


### Request Body
Property | Type | Description
--------- | ------- | -----------
`runtime_properties` | object | A dictionary containing the updated runtime properties of the node instance.
`state` | string | The new state of the node instance.
`version` | integer | The node instance current version (used for optimistic locking).

* The version property should be set to the current value of the node instance. The version is auto incremented by Cloudify on every update.

### Response
A `NodeInstance` resource.

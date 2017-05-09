# Node Instances

## The NodeInstance Resource

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
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3/node-instances/<node-instance-id>&_include=id"
```

```python
# Using CloudifyClient
client.node_instances.get('http_web_server_tfq3nt', _include=['id'])

# Using requests
url = 'http://<manager-ip>/api/v3/node-instances/<node-instance-id>'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_include': 'id'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
response.json()
```

> Response Example

```json
{
  "id": "http_web_server_tfq3nt"
}
```

`GET "{manager-ip}/api/v3/node-instances/{node-instance-id}"`

Gets a node instance.

### URI Parameters
* `node-instance-id`: The id of the node instance.

### Response
A `NodeInstance` resource.


## List Node Instances

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3/node-instances&_include=id"
```

```python
# Using CloudifyClient
instances = client.node_instances.list(_include=['id'])
for instance in instances:
    print instance

# Using requests
url = 'http://<manager-ip>/api/v3/node-instances'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_include': 'id'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
response.json()
```

> Response Example

```json
{
  "items": [
    {
      "id": "http_web_server_tfq3nt"
    },
    {
      "id": "vm_m7nmd7"
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

`GET "{manager-ip}/api/v3/node-instances"`

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

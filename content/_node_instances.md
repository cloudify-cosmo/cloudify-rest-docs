# Node Instances

## The NodeInstance Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`created_by` | string | The name of the user that created the node instance.
`deployment_id` | string | The id of the deployment the node instance belongs to.
`node_id` | string |  The id of the node of which this is an instance.
`host_id` | string | The Compute node instance id the node is contained within.
`id` | string | The id of the node instance.
`relationships` | list | The relationships the node has with other nodes.
`runtime_properties` | object | The runtime properties of the node instance.
`state` | string | The node instance state.
`tenant_name` | string | The name of the tenant that owns the node instance.
`version` | integer | A version attribute used for optimistic locking when updating the node instance.

## List Node Instances

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/node-instances&_include=id"
```

```python
# Using CloudifyClient
instances = client.node_instances.list(_include=['id'])
for instance in instances:
    print instance

# Using requests
url = 'http://<manager-ip>/api/v3.1/node-instances'
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

`GET "{manager-ip}/api/v3.1/node-instances"`

Lists all node instances.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `NodeInstance` resources.


## Get Node Instance

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/node-instances/<node-instance-id>&_include=id"
```

```python
# Using CloudifyClient
client.node_instances.get('http_web_server_tfq3nt', _include=['id'])

# Using requests
url = 'http://<manager-ip>/api/v3.1/node-instances/<node-instance-id>'
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

`GET "{manager-ip}/api/v3.1/node-instances/{node-instance-id}"`

Gets a node instance.

### URI Parameters
* `node-instance-id`: The id of the node instance.

### Response
A `NodeInstance` resource.


## Update Node Instance

> Requests Example

```shell
$ curl -X PATCH \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"version": 0, "runtime_properties": {"key": "value"}}' \
    "http://<manager-ip>/api/v3.1/node-instances/<node-instance-id>?_include=id,runtime_properties"
```

```python
# Using CloudifyClient
client.node_instances.update(
    node_instance_id='<node-instance-id>',
    version=0,
    runtime_properties={'key': 'value'},
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/node-instances/<node-instance-id>'
headers = {
    'Content-Type': 'application/json',
    'Tenant': '<manager_tenant>',
}
querystring = {'_include': 'id,runtime_properties'}
payload = {'version': 0, 'runtime_properties': {'key': 'value'}}
response = requests.patch(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
    json=payload,
)
response.json()
```

> Response Example

```json
{
  "runtime_properties": {
    "key": "value"
  },
  "id": "http_web_server_tfq3nt"
}
```

`PATCH "{manager-ip}/api/v3.1/node-instances/{node-instance-id}"`

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

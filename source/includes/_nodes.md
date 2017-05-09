# Nodes

## The Node Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | The name of the node.
`deployment_id` | string | The id of the deployment the node belongs to.
`blueprint_id` | string | The id of the blueprint the node belongs to.
`tenant_name` | string | The name of the tenant that owns the node.
`type` | string | The type of the node.
`type_hierarchy` | list | The type hierarchy of the node (ancestors).
`number_of_instances` | integer | The number of node instances the node has.
`planned_number_of_instances` | integer | -
`deploy_number_of_instances` | integer | Default number of instances on deploy.
`max_number_of_instances` | integer | Maximum number of instances.
`min_number_of_instances` | integer | Minimum number of instances.
`host_id` | string | The Compute node name the node is contained within.
`properties` | object | The properties of the node.
`operations` | object | The operations the node exposes.
`plugins` | list | A list of plugins the node is using for executing its operations.
`plugins_to_install` | list | A list of required plugins to install in order to execute the node's operations.
`relationships` | list | The relationships the node has with other nodes.

* `id` and `deployment_id` are combined together for uniquely identifying a node.

## List Nodes

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3/nodes?_include=id"
```

```python
# Using CloudifyClient
nodes = client.nodes.list(_include=['id'])
for node in nodes:
    print node

# Using request
url = 'http://<manager-ip>/api/v3/nodes'
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
      "id": "http_web_server"
    },
    {
      "id": "vm"
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

`GET "{manager-ip}/api/v3/nodes"`

Lists all nodes.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Node` resources.

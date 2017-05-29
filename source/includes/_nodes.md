# Nodes

## The Node Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`blueprint_id` | string | The id of the blueprint the node belongs to.
`deploy_number_of_instances` | integer | Default number of instances on deploy.
`deployment_id` | string | The id of the deployment the node belongs to.
`host_id` | string | The Compute node name the node is contained within.
`id` | string | The name of the node.
`max_number_of_instances` | integer | Maximum number of instances.
`min_number_of_instances` | integer | Minimum number of instances.
`number_of_instances` | integer | The number of node instances the node has.
`operations` | object | The operations the node exposes.
`planned_number_of_instances` | integer | -
`plugins_to_install` | list | A list of required plugins to install in order to execute the node's operations.
`plugins` | list | A list of plugins the node is using for executing its operations.
`properties` | object | The properties of the node.
`relationships` | list | The relationships the node has with other nodes.
`tenant_name` | string | The name of the tenant that owns the node.
`type_hierarchy` | list | The type hierarchy of the node (ancestors).
`type` | string | The type of the node.

* `id` and `deployment_id` are combined together for uniquely identifying a node.

## List Nodes

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/nodes?_include=id"
```

```python
# Using CloudifyClient
nodes = client.nodes.list(_include=['id'])
for node in nodes:
    print node

# Using request
url = 'http://<manager-ip>/api/v3.1/nodes'
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

`GET "{manager-ip}/api/v3.1/nodes"`

Lists all nodes.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Node` resources.

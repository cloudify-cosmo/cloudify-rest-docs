# Nodes

## The Node Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`actual_number_of_instances` | integer | The number of deployed node instances the node has. This number _accounts_ for scaled groups.<br>**Note:** this attribute appears in the CLI table as `number_of_instances`.<br>**Supported for Cloudify Manager 5.0.5 and above.**
`actual_planned_number_of_instances` | integer | The number of node instances specified for this node in the deployment.<br>This number _accounts_ for scaled groups.<br>**Note:** this attribute appears in the CLI table as `planned_number_of_instances`.<br>**Supported for Cloudify Manager 5.0.5 and above.**
`blueprint_id` | string | The id of the blueprint the node belongs to.
`deploy_number_of_instances` | integer | Default number of instances on deploy.
`deployment_id` | string | The id of the deployment the node belongs to.
`host_id` | string | The Compute node name the node is contained within.
`id` | string | The name of the node.
`max_number_of_instances` | integer | Maximum number of instances.
`min_number_of_instances` | integer | Minimum number of instances.
`number_of_instances` | integer | The number of deployed node instances the node has. This number _does not_ account for scaled groups.
`operations` | object | The operations the node exposes.
`planned_number_of_instances` | integer | The number of node instances specified for this node in the deployment.<br>This number _does not_ account for scaled groups.
`plugins_to_install` | list | A list of required plugins to install in order to execute the node's operations.
`plugins` | list | A list of plugins the node is using for executing its operations.
`properties` | object | The properties of the node.
`relationships` | list | The relationships the node has with other nodes.
`tenant_name` | string | The name of the tenant that owns the node.
`type_hierarchy` | list | The type hierarchy of the node (ancestors).
`type` | string | The type of the node.
`unavailable_instances` | integer | Amount of instances that failed their status check.
`drifted_instances` | integer | Amount of instances that have configuration drift.

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

### URI Parameters

For filtering, or returning additional data, the following parameters can be provided in the querystring:

* `deployment_id` - return nodes of this deployment
* `id` - return only the node matching this id
* `evaluate_functions` - evaluate intrinsic functions
* `_instance_counts` - count unavailable and drifted instances. This is only available when used together with `deployment_id`. When this is set, the `unavailable_instances` and `drifted_instances` fields are populated.


### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Node` resources.

# Nodes

## The Node Resource

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
`id` | string | The name of the node.
`deployment_id` | string | The id of the deployment the node belongs to.
`blueprint_id` | string | The id of the blueprint the node belongs to.
`type` | string | The type of the node.
`type_hierarchy` | list | The type hierarchy of the node (ancestors).
`number_of_instances` | integer | The number of node instances the node has.
`planned_number_of_instances` | integer | -
`deploy_number_of_instances` | integer | -
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
$ curl -X GET "<manager-ip>/api/v2.1/nodes"
```

```python
# Python Client-
nodes = client.nodes.list()
for node in nodes:
    print node

# Python Requests-
url = "http://<manager-ip>/api/v2.1/nodes"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/nodes",
  "method": "GET",
  "headers": {
    "content-type": "application/json"}
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
      "operations": {
        "cloudify.interfaces.lifecycle.create": {
          "inputs": {},
          "has_intrinsic_functions": false,
          "plugin": "",
          "retry_interval": null,
          "max_retries": null,
          "executor": null,
          "operation": ""
        },
        ...
        }
      },
      "deploy_number_of_instances": "1",
      "type_hierarchy": [
        "cloudify.nodes.Root",
        "cloudify.nodes.SoftwareComponent",
        "cloudify.nodes.WebServer"
      ],
      "blueprint_id": "hello-world",
      "plugins": [
        {
          "distribution_release": null,
          "install_arguments": null,
          "name": "script",
          "package_name": "cloudify-script-plugin",
          "distribution_version": null,
          "package_version": "1.3",
          "supported_platform": null,
          "source": null,
          "install": false,
          "executor": "host_agent",
          "distribution": null
        }
      ],
      "host_id": "vm",
      "properties": {
        "port": 8080
      },
      "relationships": [
        {
          "source_operations": {
            "cloudify.interfaces.relationship_lifecycle.unlink": {
              "inputs": {},
              "has_intrinsic_functions": false,
              "plugin": "",
              "retry_interval": null,
              "max_retries": null,
              "executor": null,
              "operation": ""
            },
            ...
            }
          },
          "type_hierarchy": [
            "cloudify.relationships.depends_on",
            "cloudify.relationships.contained_in"
          ],
          "target_id": "vm",
          "type": "cloudify.relationships.contained_in",
          "properties": {
            "connection_type": "all_to_all"
          }
        }
      ],
      "plugins_to_install": null,
      "type": "cloudify.nodes.WebServer",
      "id": "http_web_server",
      "number_of_instances": "1",
      "deployment_id": "hello1",
      "planned_number_of_instances": "1"
    }
  ]
}
```

`GET "{manager-ip}/api/v2.1/nodes"`

Lists all nodes.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Node` resources.

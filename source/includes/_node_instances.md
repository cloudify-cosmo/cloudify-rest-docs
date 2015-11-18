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
$ curl -XGET http://localhost/api/v2/node_instances/vm_150f1
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

`GET /api/v2/node_instances/{node-instance-id}`

Gets a node instance.

### URI Parameters
* node-instance-id: The id of the node instance.

### Response
A `NodeInstance` resource.


## List Node Instances
`GET /api/v2/node_instances`

Lists all node instances.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `NodeInstance` resources.


## Update Node Instance
`PATCH /api/v2/node_instances/{node-instance-id}`

Updates a node instance.

### URI Parameters
* node-instance-id: The id of the node instance.


### Request Body
Property | Type | Description
--------- | ------- | -----------
`runtime_properties` | object | A dictionary containing the updated runtime properties of the node instance.
`state` | string | The new state of the node instance.
`version` | integer | The node instance current version (used for optimistic locking).

* The version property should be set to the current value of the node instance. The version is auto incremented by Cloudify on every update.

### Response
A `NodeInstance` resource.

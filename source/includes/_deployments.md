# Deployments

## The Deployment Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | A unique identifier for the deployment.
`blueprint_id` | string | The id of the blueprint the deployment is based on.
`created_at` | datetime | The time the blueprint was uploaded to the manager.
`updated_at` | datetime | The last time the blueprint was updated.
`workflows` | list | A list of workflows that can be executed on a deployment.
`inputs` | object | A dictionary containing key value pairs which represents a deployment input and its provided value.
`policy_types` | object | A dictionary containing policies of a deployment.
`policy_triggers` | object | A dictionary containing policy triggers of a deployment.
`groups` | object | A dictionary containing the groups definition of deployment.
`outputs` | object | A dictionary containing an outputs definition of a deployment.


## Get Deployment

> Request Example

```shell
$ curl -XGET http://localhost/api/v2/deployments/hello1
```

> Response Example

```json
{
  "inputs": {
    "webserver_port": 8080,
    "agent_user": "centos",
    "server_ip": "localhost",
    "agent_private_key_path": "/root/.ssh/key.pem"
  },
  "policy_triggers": {
    "cloudify.policies.triggers.execute_workflow": {
      "source": "https://raw.githubusercontent.com/cloudify-cosmo/cloudify-manager/master/resources/rest-service/cloudify/triggers/execute_workflow.clj",
      "parameters": {
        "workflow_parameters": {
          "default": {},
          "description": "Workflow paramters"
        },
        "force": {
          "default": false,
          "description": "Should the workflow be executed even when another execution\nfor the same workflow is currently in progress\n"
        },
        "workflow": {
          "description": "Workflow name to execute"
        },
        "socket_timeout": {
          "default": 1000,
          "description": "Socket timeout when making request to manager REST in ms"
        },
        "allow_custom_parameters": {
          "default": false,
          "description": "Should parameters not defined in the workflow parameters\nschema be accepted\n"
        },
        "conn_timeout": {
          "default": 1000,
          "description": "Connection timeout when making request to manager REST in ms"
        }
      }
    }
  },
  "groups": {},
  "blueprint_id": "hello-world",
  "policy_types": {
    "cloudify.policies.types.threshold": {
      "source": "https://raw.githubusercontent.com/cloudify-cosmo/cloudify-manager/master/resources/rest-service/cloudify/policies/threshold.clj",
      "properties": {
        "is_node_started_before_workflow": {
          "default": true,
          "description": "Before triggering workflow, check if the node state is started"
        },
        "upper_bound": {
          "default": true,
          "description": "boolean value for describing the semantics of the threshold.\nif 'true': metrics whose value is bigger than the threshold will cause the triggers to be processed.\nif 'false': metrics with values lower than the threshold will do so.\n"
        },
        "service": {
          "default": [
            "service"
          ],
          "description": "Service names whose events should be taken into consideration"
        },
        "stability_time": {
          "default": 0,
          "description": "How long a threshold must be breached before the triggers will be processed"
        },
        "policy_operates_on_group": {
          "default": false,
          "description": "If the policy should maintain its state for the whole group\nor each node instance individually.\n"
        },
        "threshold": {
          "description": "The metric threshold value"
        },
        "interval_between_workflows": {
          "default": 300,
          "description": "Trigger workflow only if the last workflow was triggered earlier than interval-between-workflows seconds ago.\nif < 0  workflows can run concurrently.\n"
        }
      }
    }
  },
  "outputs": {
    "http_endpoint": {
      "description": "Web server external endpoint",
      "value": "http://localhost:8080"
    }
  },
  "created_at": "2015-11-08 06:53:45.845046",
  "workflows": [
    {
      "created_at": null,
      "name": "execute_operation",
      "parameters": {
        "operation_kwargs": {
          "default": {}
        },
        "node_ids": {
          "default": []
        },
        "node_instance_ids": {
          "default": []
        },
        "run_by_dependency_order": {
          "default": false
        },
        "operation": {},
        "allow_kwargs_override": {
          "default": null
        },
        "type_names": {
          "default": []
        }
      }
    },
    {
      "created_at": null,
      "name": "install",
      "parameters": {}
    }
  ],
  "id": "hello1",
  "updated_at": "2015-11-08 06:53:45.845046"
}
```


`GET /api/v2/deployments/{deployment-id}`

Gets a deployment.

### URI Parameters
* deployment-id: The id of the deployment.

### Response
A `Deployment` resource.



## List Deployments
`GET /api/v2/deployments`

Lists all deployments.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Deployment` resources.



## Create Deployment
`PUT /api/v2/deployments/{deployment-id}`

Creates a new deployment.

### URI Parameters
* deployment-id: The id of the new deployment.

### Request Body
Property | Default | Description
--------- | ------- | -----------
`blueprint_id` | string | The id of the blueprint the new deployment will be based on (required).

### Response
A `Deployment` resource.


## Delete Deployment
`DELETE /api/v2/deployments/{deployment-id}`

Deletes a deployment.

An error is raised if the deployment has any live node instances. In order to ignore this validation, the `ignore_live_nodes` argument in request body can be used.

### URI Parameters
* deployment-id: The id of the deployment.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`ignore_live_nodes` | boolean | Specifies whether to ignore the live nodes validation.



### Response
A `Deployment` resource.

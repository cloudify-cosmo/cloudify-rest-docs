# Deployments

## The Deployment Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`blueprint_id` | string | The id of the blueprint the deployment is based on.
`created_at` | datetime | The time when the deployment was created.
`created_by` | string | The name of the user that created the deployment.
`description` | string | Deployment description.
`groups` | object | A dictionary containing the groups definition of deployment.
`id` | string | A unique identifier for the deployment.
`inputs` | object | A dictionary containing key value pairs which represents a deployment input and its provided value.
`outputs` | object | A dictionary containing an outputs definition of a deployment.
`capabilities` | object | A dictionary containing an capabilities definition of a deployment.
`policy_triggers` | object | A dictionary containing policy triggers of a deployment.
`policy_types` | object | A dictionary containing policies of a deployment.
`tenant_name` | string | The name of the tenant that owns the deployment.
`updated_at` | datetime | The time the deployment was last updated at.
`workflows` | list | A list of workflows that can be executed on a deployment.


## List Deployments

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/deployments?_include=id"
```

```python
# Using CloudifyClient
deployments = client.deployments.list(_include=['id'])
for deployment in deployments:
  print deployment

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments'
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
      "id": "hello1"
    },
    {
      "id": "hello2"
    },
    {
      "id": "hello3"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 3,
      "offset": 0,
      "size": 0
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/deployments"`

Lists all deployments.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Deployment` resources.


## Get Deployment

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/deployments?id=<deployment-id>&_include=id"
```

```python
# Using CloudifyClient
client.deployments.get(deployment_id='<deployment-id>', _include=['id'])

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments'
headers = {'Tenant': '<manager-tenant>'}
querystring = {
    'id': '<deployment-id>',
    '_include': 'id',
}
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
      "id": "hello1"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 1,
      "offset": 0,
      "size": 0
    }
  }
}
```


`GET "{manager-ip}/api/v3.1/deployments?id={deployment-id}"`

Gets a deployment.

### URI Parameters
* `deployment-id`: The id of the deployment.

### Response
A `Deployment` resource.

## Create Deployment

> Request Example

```shell
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"blueprint_id": "<blueprint-id>", "inputs": {...}, "visibility": "<visibility>"}' \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>?_include=id"
```

```python
# Using CloudifyClient
client.deployments.create(
    blueprint_id='<blueprint-id>',
    deployment_id='<deployment-id>',
    inputs={...},
    visibility='<visibility>'
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments/<deployment-id>'
headers = {
    'Content-Type': 'application/json',
    'Tenant': '<manager-tenant>',
}
querystring = {'_include': 'id'}
payload ={
    'blueprint_id': '<blueprint-id>',
    'inputs': {...},
    'visibility': '<visibility>'
}
response = requests.put(
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
  "id": "hello4"
}
```

`PUT -d '{"blueprint_id": "<blueprint-id>", "inputs": {...}}' "{manager-ip}/api/v3.1/deployments/{deployment-id}"`

Creates a new deployment.

### URI Parameters
* `deployment-id`: The id of the new deployment.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`blueprint_id` | string | The id of the blueprint the new deployment will be based on (required).
`inputs` | object | The dictionary containing key value pairs which represents the deployment inputs.
`private_resource` | boolean | Optional parameter, if set to True the uploaded resource will only be accessible by its creator. Otherwise, the resource is accessible by all users that belong to the same tenant (default: False).
`skip_plugins_validation` | boolean | Optional parameter, determines whether to validate if the required deployment plugins exist on the manager (default: False).
`visibility` | string | Optional parameter, defines who can see the deployment (default: tenant). **Supported for Cloudify Manager 4.3 and above.**

Valid visibility values are:

* `private`: The resource is visible to the user that created the resource, the tenant’s managers and the system’s admins.
* `tenant`: The resource is visible to all users in the current tenant. (Default value)

### Response
A `Deployment` resource.


## Delete Deployment

> Request Example

```shell
$ curl -X DELETE \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>?_include=id"
```

```python
# Using CloudifyClient
client.deployments.delete(deployment_id='<deployments-id>')

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments/<deployment-id>'
headers = {'content-type': 'application/json'}
response = requests.delete(
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
  "id": "hello4"
}
```

`DELETE "{manager-ip}/api/v3.1/deployments/{deployment-id}"`

Deletes a deployment.

An error is raised if the deployment has any live node instances. In order to ignore this validation, the `ignore_live_nodes` argument in request body can be used.

### URI Parameters
* `deployment-id`: The id of the deployment.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`ignore_live_nodes` | boolean | Specifies whether to ignore the live nodes validation.



### Response
A `Deployment` resource.


## Set Deployment Visibility

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"visibility": "<visibility>"}' \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>/set-visibility"
```

```python
# Python Client
client.deployments.set_visibility('<deployment-id>', '<visibility>')
```

> Response Example

```json
{
  "inputs": {
    ...
  },
  "permalink": null,
  "description": "deployment_1",
  "blueprint_id": "blueprint_1",
  "policy_types": {
    ...
  },
  "tenant_name": "default_tenant",
  "created_at": "2017-12-17T09:28:22.800Z",
  "updated_at": "2017-12-17T09:29:20.750Z",
  "created_by": "admin",
  "policy_triggers": {
    ...
  },
  "private_resource": false,
  "visibility": "tenant",
  "groups": {
    ...
  },
  "workflows": {
    ...
  },
  "id": "deployment_1",
  "outputs": {
    ...
  }
}

```

`PATCH "<manager-ip>/api/v3.1/deployments/{deployment-id}/set-visibility"`

Update the visibility of the deployment. **Supported for Cloudify Manager 4.3 and above.**

### URI Parameters
* `deployment-id`: The id of the deployment to update.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`visibility` | string | Defines who can see the deployment. (Required)

The visibility value must be `tenant` because global visibility is not allowed.

### Response
A `Deployment` resource.


## The Deployment Update Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | A unique identifier for the deployment update.
`deployment_id` | string | The id of the deployment.
`old_blueprint_id` | string | The id of the deployment's blueprint before the update.
`new_blueprint_id` | string | The id of the deployment's blueprint after the update.
`old_inputs` | string | The inputs of the deployment before the update.
`new_inputs` | string | The inputs of the deployment after the update.
`state` | string | The state of this update (successful, failed, updating, etc...).
`tenant_name` | string | The name of the tenant the deployment belongs to.
`created_at` | datetime | The time when the deployment update was started.
`created_by` | string | The name of the user that started the deployment update.
`execution_id` | string | The id of the execution performing the update.
`private_resource` | boolean | Is the deployment private.
`visibility` | string | The visibility of the deployment.
`resource_availability` | string | The availability of the deployment.
`deployment_update_nodes` | object | The list of the nodes in the deployment update.
`deployment_update_node_instances` | object | A dict containing the node instances in the deployment update.
`modified_entity_ids` | object | A dict containing the modified entities.
`steps` | object | The list of deployment update steps.
`deployment_plan` | object | A dict of the deployment plan.
`deployment_update_deployment` | object | A dict of the raw deployment.


## Update Deployment

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"skip_install": "<skip_install>", "skip_uninstall": "<skip_uninstall>", "skip_reinstall": "<skip_reinstall>", "force": "<force>", "ignore_failure": "<ignore_failure>", "install_first": "<install_first>", "blueprint_id": "<blueprint_id>", "inputs": "<inputs>", "reinstall_list": "<reinstall_list>"}' \
    "http://<manager-ip>/api/v3.1/deployment-updates/<deployment-id>/update/initiate"
```

```python
# Python Client
client.deployment_updates.update_with_existing_blueprint(skip_install="<skip_install>", skip_uninstall="<skip_uninstall>", skip_reinstall="<skip_reinstall>", force="<force>", ignore_failure="<ignore_failure>", install_first="<install_first>", blueprint_id="<blueprint_id>", inputs="<inputs>", reinstall_list="<reinstall_list>")
```

> Response Example

```json
{
  "old_inputs": {
    ...
  },
  "new_inputs": {
    ...
  },
  "state": "successful",
  "deployment_id": "deployment_1",
  "old_blueprint_id": "blueprint_1",
  "new_blueprint_id": "blueprint_2",
  "steps": [
    ...
  ],
  "tenant_name": "default_tenant",
  "created_at": "2017-12-17T09:28:22.800Z",
  "created_by": "admin",
  "execution_id": "f92754a0-4cf4-4baa-80d3-0602f03f2b91",
  "deployment_update_deployment": {
    ...
  },
  "private_resource": false,
  "visibility": "tenant",
  "resource_availability": "tenant",
  "modified_entity_ids": {
    ...
  },
  "deployment_plan": {
    ...
  },
  "id": "deployment_1-b22cd6b3-6dc1-4215-b9c0-404155eea939",
  "deployment_update_node_instances": {
    ...
  }
  "deployment_update_nodes": [
    ...
  ]
}

```

`PUT "<manager-ip>/api/v3.1/deployment-updates/<deployment-id>/update/initiate"`

Update the deployment. **Supported for Cloudify Manager 4.4 and above.**

### URI Parameters
* `deployment-id`: The id of the deployment to update.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`blueprint_id` | string | The id of the blueprint to use for the update
`skip_install` | boolean | Determines whether to skip installing node instances in update workflow
`skip_install` | boolean | Determines whether to skip uninstalling node instances in update workflow
`skip_reinstall` | boolean | Determines whether to reinstall the node instances whose properties or operations are modified in the deployment update
`force` | boolean | Force running update even if previous update failed
`ignore_failure` | boolean | Ignore operation failures while unisntalling node instances in update workflow
`install_first` | boolean | Install new node instances before reinstalling removed ones (default: first uninstall, then install)
`inputs` | object | Dictionary containing inputs to update in the deployment
`reinstall_list` | object | List of IDs for node instances to reinstall (even if skip_reinstall is true)


### Response
A `Deployment Update` resource.


## Get Deployment-Update

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/deployment-updates/<deployment-update-id>?_include=id"
```

```python
# Using CloudifyClient
deployment_update = client.deployment_updates.get(update_id)
```

> Response Example

```json
{
  "old_inputs": {
    ...
  },
  "new_inputs": {
    ...
  },
  "state": "successful",
  "deployment_id": "deployment_1",
  "old_blueprint_id": "blueprint_1",
  "new_blueprint_id": "blueprint_2",
  "steps": [
    ...
  ],
  "tenant_name": "default_tenant",
  "created_at": "2017-12-17T09:28:22.800Z",
  "created_by": "admin",
  "execution_id": "f92754a0-4cf4-4baa-80d3-0602f03f2b91",
  "deployment_update_deployment": {
    ...
  },
  "private_resource": false,
  "visibility": "tenant",
  "resource_availability": "tenant",
  "modified_entity_ids": {
    ...
  },
  "deployment_plan": {
    ...
  },
  "id": "deployment_1-b22cd6b3-6dc1-4215-b9c0-404155eea939",
  "deployment_update_node_instances": {
    ...
  }
  "deployment_update_nodes": [
    ...
  ]
}

```

`GET "{manager-ip}/api/v3.1/deployment-updates/<deployment-update-id>"`

Get a deployment update. **Supported for Cloudify Manager 4.4 and above.**

### Response
A `Deployment Update` resource.


## List Deployment Updates

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/deployment-updates?_include=id"
```

```python
# Using CloudifyClient
deployment_updates = client.deployment_updates.list(
        sort=sort_by,
        is_descending=descending,
        _all_tenants=all_tenants,
        _search=search,
        _offset=pagination_offset,
        _size=pagination_size,
        deployment_id=deployment_id
    )
```

> Response Example

```json
{
  "items": [
    {
      "id": "update1"
    },
    {
      "id": "update2"
    },
    {
      "id": "update3"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 3,
      "offset": 0,
      "size": 0
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/deployment-updates"`

Lists deployment updates. **Supported for Cloudify Manager 4.4 and above.**

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Deployment Update` resources.

## Get Deployment Outputs

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>/outputs"
```

```python
# Using CloudifyClient
client.deployments.outputs.get(deployment_id='<deployment-id>')

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments/<deployment-id>/outputs'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
)
response.json()
```

> Response Example

```json
{
  "deployment_id": "dep", 
  "outputs": {
    "output_1": "node_vbs4o4",
    "output_2": "some_value"
  }
}
```


`GET "{manager-ip}/api/v3.1/deployments/{deployment-id}/outputs"`

Gets deployment outputs.

### URI Parameters
* `deployment-id`: The id of the deployment.

### Response
A `DeploymentOutput` resource.

## Get Deployment Capabilities

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>/capabilities"
```

```python
# Using CloudifyClient
client.deployments.capabilities.get(deployment_id='<deployment-id>')

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments/<deployment-id>/capabilities'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
)
response.json()
```

> Response Example

```json
{
  "deployment_id": "dep", 
  "capabilities": {
    "capability_1": "node_vbs4o4",
    "capability_2": "some_capability"
  }
}
```


`GET "{manager-ip}/api/v3.1/deployments/{deployment-id}/capabilities"`

Gets deployment capabilities.

### URI Parameters
* `deployment-id`: The id of the deployment.

### Response
A `DeploymentOutput` resource.
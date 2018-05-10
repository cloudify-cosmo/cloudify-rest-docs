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
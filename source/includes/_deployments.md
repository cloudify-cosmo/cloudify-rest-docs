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
    -d '{"blueprint_id": "<blueprint-id>", "inputs": {...}}' \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>?_include=id"
```

```python
# Using CloudifyClient
client.deployments.create(
    blueprint_id='<blueprint-id>',
    deployment_id='<deployment-id>',
    inputs={...},
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

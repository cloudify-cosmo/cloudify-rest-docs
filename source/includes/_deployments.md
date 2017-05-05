# Deployments

## The Deployment Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | A unique identifier for the deployment.
`blueprint_id` | string | The id of the blueprint the deployment is based on.
`created_at` | datetime | The time when the deployment was created.
`updated_at` | datetime | The time the deployment was last updated at.
`created_by` | string | The name of the user that created the deployment.
`tenant_name` | string | The name of the tenant that owns the deployment.
`description` | string | Deployment description.
`workflows` | list | A list of workflows that can be executed on a deployment.
`inputs` | object | A dictionary containing key value pairs which represents a deployment input and its provided value.
`policy_types` | object | A dictionary containing policies of a deployment.
`policy_triggers` | object | A dictionary containing policy triggers of a deployment.
`groups` | object | A dictionary containing the groups definition of deployment.
`outputs` | object | A dictionary containing an outputs definition of a deployment.


## Get Deployment

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3/deployments?id=<deployment-id>&_include=id"
```

```python
# Using CloudifyClient
client.deployments.get(deployment_id='<deployment-id>', _include=['id'])

# Using requests
url = 'http://<manager-ip>/api/v3/deployments'
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


`GET "{manager-ip}/api/v3/deployments?id={deployment-id}"`

Gets a deployment.

### URI Parameters
* `deployment-id`: The id of the deployment.

### Response
A `Deployment` resource.



## List Deployments

> Request Example

```shell
$ curl -X GET "<manager-ip>/api/v2.1/deployments?blueprint_id=<blueprint-id>&_include=id,created_at"
```

```python
# Python Client-
deployments = client.deployments.list(blueprint_id='<blueprint-id>',_include=['id','created_at'])
for deployment in deployments:
  print deployment

# Python Requests-
url = "http://<manager-ip>/api/v2.1/deployments"
querystring = {"blueprint_id":"<blueprint-id>","_include":"id,created_at"}
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
```

`GET "{manager-ip}/api/v2.1/deployments"`

Lists all deployments.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Deployment` resources.



## Create Deployment

> Request Example

```shell
$ curl -X PUT -H "Content-Type: application/json" -d '{"inputs":{"image":"<image-id>","flavor":"<flavor-id>",
"agent_user":"<user-name>"}, "blueprint_id":"<blueprint-id>"}' "<manager-ip>/api/v2.1/deployments/<deployment-id>"
```

```python
# Python Client-
client.deployments.create(blueprint_id='<blueprint-id>', deployment_id='<deployment-id>', inputs={
                          'image':'<image-id>','flavor':'<flavor-id>','agent_user':'<user-name>'})

# Python Requests-
url = "http://<manager-ip>/api/v2.1/deployments/<deployment-id>"
payload = "{\"inputs\":{\"image\":\"<image-id>\",\"flavor\":\"<flavor-id>\",\"agent_user\":\"<user-name>\"},
            \"blueprint_id\":\"<blueprint-id>\"}"
headers = {'content-type': "application/json"}
response = requests.request("PUT", url, data=payload, headers=headers)
print(response.text)
```

`PUT -d '{"inputs":{...}, "blueprint_id":"<blueprint-id>"}' "{manager-ip}/api/v2.1/deployments/{deployment-id}"`

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
$ curl -X DELETE "<manager-ip>/deployments/<deployments-id>"
```

```python
# Python Client-
client.deployments.delete(deployment_id='<deployments-id>')

# Python Requests-
url = "http://<manager-ip>/deployments/<deployment-id>"
headers = {'content-type': "application/json"}
response = requests.request("DELETE", url, headers=headers)
print(response.text)
```

`DELETE "{manager-ip}/api/v2.1/deployments/{deployment-id}"`

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

# Workflows

## The Workflow Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`name` | string | The name of the workflow (e.g. `install`, `update`)
`created_at` | datetime | The time when the workflow was created.
`parameters` | object | A dictionary containing definitions of the workflow's parameters.
`plugin` | string | The name of the plugin containing workflow implementation.
`operation` | string | The name of the system task performed by the workflow.
`is_available` | boolean | Whether or not this workflow is currently available for running

## List Workflows

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/workflows?id=<deployment_id>"

$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/workflows?deployment_group_id=<deployment_group_id>"
```

```python
# Using CloudifyClient
workflows = client.workflows.list(id='dep1')
for workflow in workflows:
  print workflow

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'deployment_group_id': 'g1'}
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
      "name": "hello1",
      "created_at": "2021-04-27T06:51:29.541Z",
      "parameters": {},
      "plugin": "cloudify-hello-plugin",
      "operation": "",
      "is_available": true
    },
    {
      "name": "hello2"
      "created_at": "2021-04-27T06:51:29.542Z",
      "parameters": {},
      "plugin": "cloudify-hello-plugin",
      "operation": "",
      "is_available": false
    },
    {
      "name": "hello3"
      "created_at": "2021-04-27T06:51:29.543Z",
      "parameters": {},
      "plugin": "cloudify-hello-plugin",
      "operation": "",
      "is_available": true
    }
  ],
  "metadata": {
    "pagination": {
      "total": 3,
      "offset": 0,
      "size": 3
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/workflows"`

Lists all of the workflows specified for the deployments selected by the additional parameters.  A
special parameter `_filter_id` can be used to describe a deployments filter used to select specific
deployments.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Deployment` resources.


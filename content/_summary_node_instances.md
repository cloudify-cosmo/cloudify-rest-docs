# Node Instance Summary

## Summaries of node instance resources

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`_target_field` | string | The field to generate a summary on. Valid: deployment_id, node_id

All attributes for filtering node instances are also supported, e.g. filtering by `deployment_id`.
See Node Instance documentation for details.

## Summarize Node Instances

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/node_instances?_target_field=deployment_id"
```

```python
# Using CloudifyClient
summaries = client.summary.node_instances.get(_target_field='deployment_id')
for summary in summaries:
    print(summary)

# Using request
url = 'http://<manager-ip>/api/v3.1/summary/node_instances'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_target_field': 'deployment_id'}
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
      "deployment_id": "s",
      "node_instances": 2
    },
    {
      "deployment_id": "s2",
      "node_instances": 2
    },
    {
      "deployment_id": "s3",
      "node_instances": 2
    },
    {
      "deployment_id": "s4",
      "node_instances": 2
    },
    {
      "deployment_id": "s5",
      "node_instances": 2
    },
    {
      "deployment_id": "sga",
      "node_instances": 51
    },
    {
      "deployment_id": "sga2",
      "node_instances": 51
    }
  ],
  "metadata": {
    "pagination": {
      "total": 7,
      "offset": 0,
      "size": 0
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/summary/node_instances?_target_field={target-field}"`

Get a summary of node instances based on the target field.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of node instance summaries based on the target field.

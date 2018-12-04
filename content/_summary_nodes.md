# Node Summary

## Summaries of node resources

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`_target_field` | string | The field to generate a summary on. Valid: deployment_id

All attributes for filtering nodes are also supported, e.g. filtering by `blueprint_id`.
See Node documentation for details.

## Summarize Nodes

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/nodes?_target_field=deployment_id"
```

```python
# Using CloudifyClient
summaries = client.summary.nodes.get(_target_field='deployment_id')
for summary in summaries:
    print(summary)

# Using request
url = 'http://<manager-ip>/api/v3.1/summary/nodes'
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
    {"deployment_id": "s", "nodes": 1},
    {"deployment_id": "s2", "nodes": 1},
    {"deployment_id": "s3", "nodes": 1},
    {"deployment_id": "s4", "nodes": 1},
    {"deployment_id": "s5", "nodes": 1},
    {"deployment_id": "sga", "nodes": 5},
    {"deployment_id": "sga2", "nodes": 5}
  ],
  "metadata": {
    "pagination": {
      "offset": 0,
      "size": 0,
      "total": 7
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/summary/nodes?_target_field={target-field}"`

Get a summary of nodes based on the target field.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of node summaries based on the target field.

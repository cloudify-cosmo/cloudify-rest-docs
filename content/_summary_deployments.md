# Deployment Summary

## Summaries of deployment resources

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`_target_field` | string | The field to generate a summary on. Valid: blueprint_id

All attributes for filtering deployments are also supported, e.g. filtering by `blueprint_id`.
See Deployment documentation for details.

## Summarize Deployments

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/deployments?_target_field=blueprint_id"
```

```python
# Using CloudifyClient
summaries = client.summary.deployments.get(_target_field='blueprint_id')
for summary in summaries:
    print(summary)

# Using request
url = 'http://<manager-ip>/api/v3.1/summary/deployments'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_target_field': 'blueprint_id'}
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
      "blueprint_id": "s",
      "deployments": 5
    },
    {
      "blueprint_id": "sga",
      "deployments": 2
    }
  ],
  "metadata": {
    "pagination": {
      "size": 0,
      "total": 2,
      "offset": 0
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/summary/deployments?_target_field={target-field}"`

Get a summary of deployments based on the target field.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of deployment summaries based on the target field.

# Execution Summary

## Summaries of execution resources

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`_target_field` | string | The field to generate a summary on. Valid: status, blueprint_id, deployment_id, workflow_id, tenant_name, visibility
`_sub_field` | string | Optional sub-field to summarise on. Valid fields are identical to those for `_target_field`.

All attributes for filtering executions are also supported, e.g. filtering by `blueprint_id`.
See Execution documentation for details.

## Summarize Executions

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/executions?_target_field=blueprint_id"
```

With sub-field:
```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/executions?_target_field=tenant_name&_sub_field=workflow_id&_all_tenants=true"
```

```python
# Using CloudifyClient
summaries = client.summary.executions.get(_target_field='blueprint_id')
for summary in summaries:
    print(summary)

# Using request
url = 'http://<manager-ip>/api/v3.1/summary/executions'
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
      "blueprint_id": "sga",
      "executions": 6
    },
    {
      "blueprint_id": "s",
      "executions": 10
    },
    {
      "blueprint_id": "sg",
      "executions": 2
    }
  ],
  "metadata": {
    "pagination": {
      "offset": 0,
      "size": 1000,
      "total": 3
    }
  }
}
```

With sub-field:
```json
{
  "items": [
    {
      "by workflow_id": [
        {
          "executions": 9,
          "workflow_id": "create_deployment_environment"
        },
        {
          "executions": 1,
          "workflow_id": "create_snapshot"
        },
        {
          "executions": 9,
          "workflow_id": "install"
        },
        {
          "executions": 1,
          "workflow_id": "restore_snapshot"
        }
      ],
      "executions": 20,
      "tenant_name": "default_tenant"
    }
  ],
  "metadata": {
    "pagination": {
      "offset": 0,
      "size": 1000,
      "total": 4
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/summary/executions?_target_field={target-field}&_sub_field={optional sub-field}"`

Get a summary of executions based on the target field and optional sub-field.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of execution summaries based on the target field and optional sub-field.

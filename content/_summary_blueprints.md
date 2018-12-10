# Blueprint Summary

## Summaries of blueprint resources

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`_target_field` | string | The field to generate a summary on. Valid: tenant_name, visibility
`_sub_field` | string | Optional sub-field to summarise on. Valid fields are identical to those for `_target_field`.

All attributes for filtering blueprints are also supported, e.g. filtering by `blueprint_id`.
See Blueprint documentation for details.

## Summarize Blueprints

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/blueprints?_target_field=tenant_name&_all_tenants=true"
```

With sub-field:
```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/blueprints?_target_field=tenant_name&_sub_field=visibility&_all_tenants=true"
```

```python
# Using CloudifyClient
summaries = client.summary.blueprints.get(_target_field='blueprint_id')
for summary in summaries:
    print(summary)

# Using request
url = 'http://<manager-ip>/api/v3.1/summary/blueprints'
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
      "blueprints": 3,
      "tenant_name": "test1"
    },
    {
      "blueprints": 3,
      "tenant_name": "test2"
    },
    {
      "blueprints": 3,
      "tenant_name": "default_tenant"
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
      "blueprints": 3,
      "by visibility": [
        {
          "blueprints": 3,
          "visibility": "tenant"
        }
      ],
      "tenant_name": "test1"
    },
    {
      "blueprints": 3,
      "by visibility": [
        {
          "blueprints": 3,
          "visibility": "tenant"
        }
      ],
      "tenant_name": "test2"
    },
    {
      "blueprints": 3,
      "by visibility": [
        {
          "blueprints": 3,
          "visibility": "tenant"
        }
      ],
      "tenant_name": "default_tenant"
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

`GET "{manager-ip}/api/v3.1/summary/blueprints?_target_field={target-field}&_sub_field={optional sub-field}"`

Get a summary of blueprints based on the target field and optional sub-field.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of blueprint summaries based on the target field and optional sub-field.

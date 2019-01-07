# Deployment Summary

## Summaries of deployment resources

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`_target_field` | string | The field to generate a summary on. Valid: blueprint_id, tenant_name, visibility
`_sub_field` | string | Optional sub-field to summarise on. Valid fields are identical to those for `_target_field`.

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

> With sub-field

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/deployments?_target_field=tenant_name&_sub_field=blueprint_id&_all_tenants=true"
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
      "size": 1000,
      "total": 2,
      "offset": 0
    }
  }
}
```

> With sub-field

```json
{
  "items": [
    {
      "by blueprint_id": [
        {
          "blueprint_id": "s",
          "deployments": 1
        },
        {
          "blueprint_id": "sg",
          "deployments": 3
        },
        {
          "blueprint_id": "sga",
          "deployments": 5
        }
      ],
      "deployments": 9,
      "tenant_name": "test1"
    },
    {
      "by blueprint_id": [
        {
          "blueprint_id": "sga",
          "deployments": 1
        },
        {
          "blueprint_id": "s",
          "deployments": 3
        },
        {
          "blueprint_id": "sg",
          "deployments": 5
        }
      ],
      "deployments": 9,
      "tenant_name": "test2"
    },
    {
      "by blueprint_id": [
        {
          "blueprint_id": "sga",
          "deployments": 3
        },
        {
          "blueprint_id": "s",
          "deployments": 5
        },
        {
          "blueprint_id": "sg",
          "deployments": 1
        }
      ],
      "deployments": 9,
      "tenant_name": "default_tenant"
    }
  ],
  "metadata": {
    "pagination": {
      "offset": 0,
      "size": 1000,
      "total": 9
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/summary/deployments?_target_field={target-field}&_sub_field={optional sub-field}"`

Get a summary of deployments based on the target field and optional sub-field.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of deployment summaries based on the target field and optional sub-field.

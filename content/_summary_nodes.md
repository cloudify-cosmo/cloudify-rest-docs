# Node Summary

## Summaries of node resources

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`_target_field` | string | The field to generate a summary on. Valid: deployment_id, tenant_name, visibility
`_sub_field` | string | Optional sub-field to summarise on. Valid fields are identical to those for `_target_field`.

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

> With sub-field

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/nodes?_target_field=tenant_name&_sub_field=deployment_id&_all_tenants=true"
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
      "size": 1000,
      "total": 7
    }
  }
}
```

> With sub-field

```json
{
    "items": [
        {
            "by deployment_id": [
                {
                    "deployment_id": "s1",
                    "nodes": 1
                },
                {
                    "deployment_id": "sg1",
                    "nodes": 2
                },
                {
                    "deployment_id": "sg2",
                    "nodes": 2
                },
                {
                    "deployment_id": "sg3",
                    "nodes": 2
                },
                {
                    "deployment_id": "sga1",
                    "nodes": 5
                },
                {
                    "deployment_id": "sga2",
                    "nodes": 5
                },
                {
                    "deployment_id": "sga3",
                    "nodes": 5
                },
                {
                    "deployment_id": "sga4",
                    "nodes": 5
                },
                {
                    "deployment_id": "sga5",
                    "nodes": 5
                }
            ],
            "nodes": 32,
            "tenant_name": "test1"
        },
        {
            "by deployment_id": [
                {
                    "deployment_id": "s1",
                    "nodes": 1
                },
                {
                    "deployment_id": "s2",
                    "nodes": 1
                },
                {
                    "deployment_id": "s3",
                    "nodes": 1
                },
                {
                    "deployment_id": "sg1",
                    "nodes": 2
                },
                {
                    "deployment_id": "sg2",
                    "nodes": 2
                },
                {
                    "deployment_id": "sg3",
                    "nodes": 2
                },
                {
                    "deployment_id": "sg4",
                    "nodes": 2
                },
                {
                    "deployment_id": "sg5",
                    "nodes": 2
                },
                {
                    "deployment_id": "sga1",
                    "nodes": 5
                }
            ],
            "nodes": 18,
            "tenant_name": "test2"
        },
        {
            "by deployment_id": [
                {
                    "deployment_id": "s1",
                    "nodes": 1
                },
                {
                    "deployment_id": "s2",
                    "nodes": 1
                },
                {
                    "deployment_id": "s3",
                    "nodes": 1
                },
                {
                    "deployment_id": "s4",
                    "nodes": 1
                },
                {
                    "deployment_id": "s5",
                    "nodes": 1
                },
                {
                    "deployment_id": "sg1",
                    "nodes": 2
                },
                {
                    "deployment_id": "sga1",
                    "nodes": 5
                },
                {
                    "deployment_id": "sga2",
                    "nodes": 5
                },
                {
                    "deployment_id": "sga3",
                    "nodes": 5
                }
            ],
            "nodes": 22,
            "tenant_name": "default_tenant"
        }
    ],
    "metadata": {
        "pagination": {
            "offset": 0,
            "size": 1000,
            "total": 27
        }
    }
}
```

`GET "{manager-ip}/api/v3.1/summary/nodes?_target_field={target-field}&_sub_field={optional sub-field}"`

Get a summary of nodes based on the target field and optional sub-field.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of node summaries based on the target field and optional sub-field.

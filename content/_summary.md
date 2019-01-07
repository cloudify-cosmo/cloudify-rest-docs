# Summaries

## The summary resource

### Attributes:
Attribute | Type | Description
--------- | ------- | -------
`_target_field` | string | The field to generate a summary on. Valid fields are listed for each sub-resource.
`_sub_field` | string | Optional sub-field to summarise on. Valid fields are identical to those for `_target_field`.

All attributes for filtering the specific resources are also supported, e.g. filtering blueprints by `blueprint_id` or filtering deployments by `deployment_id`.
See documentation for each resource to find applicable filtering attributes.

## Summarize Blueprints

Valid fields: tenant_name, visibility

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/blueprints?_target_field=tenant_name&_all_tenants=true"
```

> With sub-field

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

> With sub-field

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

## Summarize Deployments

Valid fields: blueprint_id, tenant_name, visibility

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

## Summarize Executions

Valid fields: status, blueprint_id, deployment_id, workflow_id, tenant_name, visibility

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/executions?_target_field=blueprint_id"
```

> With sub-field

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

> With sub-field

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

## Summarize Node Instances

Valid fields: deployment_id, node_id, host_id, state, tenant_name, visibility

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/node_instances?_target_field=deployment_id"
```

> With sub-field

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/summary/node_instances?_target_field=node_id&_sub_field=state"
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
      "size": 1000
    }
  }
}
```

> With sub-field

```json
{
  "items": [
    {
      "by state": [
        {
          "node_instances": 42,
          "state": "started"
        }
      ],
      "node_id": "fakeapp1",
      "node_instances": 42
    },
    {
      "by state": [
        {
          "node_instances": 84,
          "state": "started"
        }
      ],
      "node_id": "fakevm2",
      "node_instances": 84
    },
    {
      "by state": [
        {
          "node_instances": 3,
          "state": "started"
        }
      ],
      "node_id": "fakeplatformthing1",
      "node_instances": 3
    },
    {
      "by state": [
        {
          "node_instances": 66,
          "state": "started"
        }
      ],
      "node_id": "fakevm",
      "node_instances": 66
    },
    {
      "by state": [
        {
          "node_instances": 3,
          "state": "started"
        }
      ],
      "node_id": "fakeappconfig1",
      "node_instances": 3
    }
  ],
  "metadata": {
    "pagination": {
      "offset": 0,
      "size": 1000,
      "total": 5
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/summary/node_instances?_target_field={target-field}&_sub_field={optional sub-field}"`

Get a summary of node instances based on the target field and optional sub-field.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of node instance summaries based on the target field and optional sub-field.

## Summarize Nodes

Valid fields: deployment_id, tenant_name, visibility

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

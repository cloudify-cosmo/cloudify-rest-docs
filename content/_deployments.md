# Deployments

## The Deployment Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`blueprint_id` | string | The id of the blueprint the deployment is based on.
`created_at` | datetime | The time when the deployment was created.
`created_by` | string | The name of the user that created the deployment.
`description` | string | Deployment description.
`groups` | object | A dictionary containing the groups definition of deployment.
`id` | string | A unique identifier for the deployment.
`inputs` | object | A dictionary containing key value pairs which represents a deployment input and its provided value.
`outputs` | object | A dictionary containing an outputs definition of a deployment.
`capabilities` | object | A dictionary containing an capabilities definition of a deployment. **Supported for Cloudify Manager 4.5.5 and above.**
`site_name` | string | The name of the site the deployment is assigned to. **Supported for Cloudify Manager 5.0 and above.**
`policy_triggers` | object | A dictionary containing policy triggers of a deployment.
`policy_types` | object | A dictionary containing policies of a deployment.
`tenant_name` | string | The name of the tenant that owns the deployment.
`updated_at` | datetime | The time the deployment was last updated at.
`workflows` | list | A list of workflows that can be executed on a deployment.
`labels` | list | A list of the deployment's labels. **Supported for Cloudify Manager 5.1.1 and above.**


## List Deployments

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/deployments?_include=id"
```

```python
# Using CloudifyClient
deployments = client.deployments.list(_include=['id'])
for deployment in deployments:
  print deployment

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_include': 'id'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
response.json()
```

> Request Example Using Filter-Rules

In order to filter out the deployments' list based on the deployments' labels, you can use filter-rules in one of two forms:
1. Providing the ID of a pre-created filter, using the parameter `_filter_id`. 
2. Providing a list of filter rules separated by a comma (`,`), using the parameter `_filter_rules`. E.g. `_filter_rules="env=aws,arch!=k8s"`

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/deployments?_filter_id=<filter_id>&_include=id"
    
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/deployments?_filter_rules=<filter_rules>&_include=id"
```

```python
# Using CloudifyClient
deployments = client.deployments.list(filter_rules={'_filter_id': 'london_sites'})
for deployment in deployments:
  print deployment

deployments = client.deployments.list(filter_rules={'_filter_rules': ['env=aws', 'arch is null']})
for deployment in deployments:
  print deployment

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_include': 'id', '_filter_id': 'london_sites'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
response.json()

url = 'http://<manager-ip>/api/v3.1/deployments'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_include': 'id', '_filter_rules': ['env=aws', 'arch is null']}
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
    },
    {
      "id": "hello2"
    },
    {
      "id": "hello3"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 3,
      "offset": 0,
      "size": 0
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/deployments"`

Lists all deployments.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Deployment` resources.


## Get a Filtered List of Deployments

You can get a filtered list of deployments based on their labels and certain attributes (`blueprint_id`, `created_by`, `site_name`, and `schedules`).
The filtering can be done by specifying a pre-created filter ID, or by providing a list of filter rules. 
A filter rule is a dictionary of the following form: 
```text
{
 "key": "<key>",
 "values": [<list of values>],
 "operator": "<LabelsOperator>" or "<AttrsOperator>",
 "type": "<FilterRuleType>"
}
```
`<LabelsOperator>` can be one of: "any_of", "not_any_of", "is_null" or "is_not_null".

`<AttrsOperator>` can be one of: "any_of", "not_any_of", "contains", "not_contains", "starts_with", "ends_with", "is_not_empty".

`<FilterRuleType>` can be one of: "label" or "attribute". If "label" is provided, then the operator must be a `<LabelsOperator>`, and if "attribute" is provided, then 
the operator must be an `<AttrsOperator>`. 

E.g. filtering by the following filter rules, will return all deployments that their creator name starts with "alice" or "bob", 
and have the label `environment:aws` assigned to them.

```json
[
 {
  "key": "created_by",
  "values": ["alice", "bob"],
  "operator": "starts-with",
  "type": "attribute"
 },
 {
  "key": "environment",
  "values": ["aws"],
  "operator": "any_of",
  "type": "label"
 }
]
```

> Request Example

```shell
$ curl -X POST \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"filter_rules": <a list of filter rules as described above>}' \
    "http://<manager-ip>/api/v3.1/searches/deployments?_include=id"
```

```python
# Using CloudifyClient
deployments = client.deployments.list(filter_rules=[...])

# Using requests
url = 'http://<manager-ip>/api/v3.1/searches/deployments'
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_include': 'id'}
data = {'filter_rules': [...]}
response = requests.patch(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
    date=data
)
response.json()

```

> Response Example

```json
{
  "items": [
    {
      "id": "dep1"
    },
    {
      "id": "dep2"
    },
    {
      "id": "dep3"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 3,
      "offset": 0,
      "size": 0
    }
  }
}
```

`POST "{manager-ip}/api/v3.1/searches/deployments"`

Get a filtered list of deployments.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of filtered `Deployment` resources.


## Get Deployment

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/deployments?id=<deployment-id>&_include=id"
```

```python
# Using CloudifyClient
client.deployments.get(deployment_id='<deployment-id>', _include=['id'])

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments'
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


`GET "{manager-ip}/api/v3.1/deployments?id={deployment-id}"`

Gets a deployment.

### URI Parameters
* `deployment-id`: The id of the deployment.

### Response
A `Deployment` resource.

## Create Deployment

> Request Example

```shell
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"blueprint_id": "<blueprint-id>", "inputs": {...}, "visibility": "<visibility>", "site_name": "<site name>", "labels": [{"<key1>": "<val1>"}, {"<key2>": "<val2>"}]}' \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>?_include=id"
```

```python
# Using CloudifyClient
client.deployments.create(
    blueprint_id='<blueprint-id>',
    deployment_id='<deployment-id>',
    inputs={...},
    visibility='<visibility>',
    site_name='<site name>',
    labels=[{'<key1': '<val1>', '<key2>': '<val2>'}]
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments/<deployment-id>'
headers = {
    'Content-Type': 'application/json',
    'Tenant': '<manager-tenant>',
}
querystring = {'_include': 'id'}
payload ={
    'blueprint_id': '<blueprint-id>',
    'inputs': {...},
    'visibility': '<visibility>',
    'site_name': '<site name>',
    'labels': [{'<key1>': '<val1>'}, {'<key2>': '<val2>'}]
}
response = requests.put(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
    json=payload,
)
response.json()
```

> Response Example

```json
{
  "id": "hello4"
}
```

`PUT -d '{"blueprint_id": "<blueprint-id>", "inputs": {...}}' "{manager-ip}/api/v3.1/deployments/{deployment-id}"`

Creates a new deployment.

### URI Parameters
* `deployment-id`: The id of the new deployment.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`blueprint_id` | string | The id of the blueprint the new deployment will be based on (required).
`inputs` | object | The dictionary containing key value pairs which represents the deployment inputs.
`site_name` | string | The name of the site to assign the new deployment to. **Supported for Cloudify Manager 5.0 and above.**
`labels` | list | A list of labels to assign to the new deployment. **Supported for Cloudify Manager 5.1.1 and above.**
`private_resource` | boolean | Optional parameter, if set to True the uploaded resource will only be accessible by its creator. Otherwise, the resource is accessible by all users that belong to the same tenant (default: False).
`skip_plugins_validation` | boolean | Optional parameter, determines whether to validate if the required deployment plugins exist on the manager (default: False).
`visibility` | string | Optional parameter, defines who can see the deployment (default: tenant). **Supported for Cloudify Manager 4.3 and above.**

Valid visibility values are:

* `private`: The resource is visible to the user that created the resource, the tenant’s managers and the system’s admins.
* `tenant`: The resource is visible to all users in the current tenant. (Default value)
* `global`: The resource is visible to all users in all tenants across the manager.
A deployment can only be global if the blueprint from which it was created is
also global. Only administrators or users with access to the tenant on which
the deployment was created have permissions to execute workflow on it. **Supported for Cloudify Manager 4.5.5 and above.**

### Response
A `Deployment` resource.


## Delete Deployment

> Request Example

```shell
$ curl -X DELETE \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>?_include=id&delete_logs=True"
```

```python
# Using CloudifyClient
client.deployments.delete(deployment_id='<deployments-id>',
                          with_logs=False)

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments/<deployment-id>'
headers = {'content-type': 'application/json'}
querystring = {
    'delete_logs': True
}
requests.delete(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
```

`DELETE "{manager-ip}/api/v3.1/deployments/{deployment-id}"`

Deletes a deployment.

An error is raised if the deployment has any live node instances, or there
 are installations which depend on this deployment. In order to ignore this
 validation, the `force` argument in request body can be used.

### URI Parameters
* `deployment-id`: The id of the deployment.
* `delete_logs`: Determines if to delete the deployment logs, default: false.


### Request Body
Property | Type | Description
--------- | ------- | -----------
`force` | boolean | Specifies whether to force deployment deletion even if there are existing live nodes for it, or existing installations which depend on it



### Response
No content - HTTP code 204.


## Set Deployment Visibility

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"visibility": "<visibility>"}' \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>/set-visibility"
```

```python
# Python Client
client.deployments.set_visibility('<deployment-id>', '<visibility>')
```

> Response Example

```json
{
  "inputs": {
    ...
  },
  "permalink": null,
  "description": "deployment_1",
  "blueprint_id": "blueprint_1",
  "policy_types": {
    ...
  },
  "tenant_name": "default_tenant",
  "created_at": "2017-12-17T09:28:22.800Z",
  "updated_at": "2017-12-17T09:29:20.750Z",
  "created_by": "admin",
  "policy_triggers": {
    ...
  },
  "private_resource": false,
  "visibility": "tenant",
  "groups": {
    ...
  },
  "workflows": {
    ...
  },
  "id": "deployment_1",
  "outputs": {
    ...
  },
  "labels": [
    ...
  ]
}

```

`PATCH "<manager-ip>/api/v3.1/deployments/{deployment-id}/set-visibility"`

Update the visibility of the deployment. **Supported for Cloudify Manager 4.3 and above.**

### URI Parameters
* `deployment-id`: The id of the deployment to update.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`visibility` | string | Defines who can see the deployment. (Required)

Valid values are `tenant` or `global`. **`global` is supported for Cloudify Manager 4.5.5 and above.**

### Response
A `Deployment` resource.


## Set Deployment Site

> Request Example

```shell
$ curl -X POST \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"site_name": "<site name>"}' \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>/set-site"
```

```python
# Python Client
client.deployments.set_site('<deployment-id>', site_name='<site name>', detach_site=False)
```

> Response Example

```json
{
  "inputs": {
    ...
  },
  "permalink": null,
  "description": "deployment_1",
  "blueprint_id": "blueprint_1",
  "tenant_name": "default_tenant",
  "created_at": "2017-12-17T09:28:22.800Z",
  "updated_at": "2017-12-17T09:29:20.750Z",
  "created_by": "admin",
  "site_name": "a site name",
  "private_resource": false,
  "visibility": "tenant",
  "groups": {
    ...
  },
  "workflows": {
    ...
  },
  "id": "deployment_1",
  "outputs": {
    ...
  },
  "labels": [
    ...
  ]
}

```

`POST "<manager-ip>/api/v3.1/deployments/{deployment-id}/set-site"`

Update the site of the deployment. **Supported for Cloudify Manager 5.0 and above.**

### URI Parameters
* `deployment-id`: The id of the deployment to update.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`site_name` | string | The site name to assign the deployment.
`detach_site` | Boolean | Clear site relation from the deployment.



### Response
A `Deployment` resource.


## The Deployment Update Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | A unique identifier for the deployment update.
`deployment_id` | string | The id of the deployment.
`old_blueprint_id` | string | The id of the deployment's blueprint before the update.
`new_blueprint_id` | string | The id of the deployment's blueprint after the update.
`old_inputs` | string | The inputs of the deployment before the update.
`new_inputs` | string | The inputs of the deployment after the update.
`state` | string | The state of this update ("updating", "executing_workflow", "finalizing", "successful", "failed", or "preview").
`tenant_name` | string | The name of the tenant the deployment belongs to.
`created_at` | datetime | The time when the deployment update was started.
`created_by` | string | The name of the user that started the deployment update.
`execution_id` | string | The id of the execution performing the update.
`private_resource` | boolean | Is the deployment private.
`visibility` | string | The visibility of the deployment.
`resource_availability` | string | The availability of the deployment.
`deployment_update_nodes` | object | The list of the nodes in the deployment update.
`deployment_update_node_instances` | object | A dict containing the node instances in the deployment update.
`modified_entity_ids` | object | A dict containing the modified entities.
`steps` | object | The list of deployment update steps.
`deployment_plan` | object | A dict of the deployment plan.
`deployment_update_deployment` | object | A dict of the raw deployment.
`central_plugins_to_install` | list | A list of the plugins that are executed by the central deployment agent and will be installed.
`central_plugins_to_uninstall` | list | A list of the plugins that are executed by the central deployment agent and will be uninstalled.


## Update Deployment

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"skip_install": "<skip_install>", "skip_uninstall": "<skip_uninstall>", "skip_reinstall": "<skip_reinstall>", "force": "<force>", "ignore_failure": "<ignore_failure>", "install_first": "<install_first>", "blueprint_id": "<blueprint_id>", "inputs": "<inputs>", "reinstall_list": "<reinstall_list>", "update_plugins": "<update_plugins>", "runtime_eval": "<runtime_eval>", "auto_correct_args": "<auto_correct_args>", "reevaluate_active_statuses": "<reevaluate_active_statuses>"}' \
    "http://<manager-ip>/api/v3.1/deployment-updates/<deployment-id>/update/initiate"
```

```python
# Python Client
client.deployment_updates.update_with_existing_blueprint(skip_install="<skip_install>", skip_uninstall="<skip_uninstall>", skip_reinstall="<skip_reinstall>", force="<force>", ignore_failure="<ignore_failure>", install_first="<install_first>", blueprint_id="<blueprint_id>", inputs="<inputs>", reinstall_list="<reinstall_list>", runtime_eval="<runtime_eval>", auto_correct_args="<auto_correct_args>", reevaluate_active_statuses="<reevaluate_active_statuses>")
```

> Response Example

```json
{
  "old_inputs": {
    ...
  },
  "new_inputs": {
    ...
  },
  "state": "successful",
  "deployment_id": "deployment_1",
  "old_blueprint_id": "blueprint_1",
  "new_blueprint_id": "blueprint_2",
  "steps": [
    ...
  ],
  "tenant_name": "default_tenant",
  "created_at": "2017-12-17T09:28:22.800Z",
  "created_by": "admin",
  "execution_id": "f92754a0-4cf4-4baa-80d3-0602f03f2b91",
  "deployment_update_deployment": {
    ...
  },
  "private_resource": false,
  "visibility": "tenant",
  "resource_availability": "tenant",
  "modified_entity_ids": {
    ...
  },
  "deployment_plan": {
    ...
  },
  "id": "deployment_1-b22cd6b3-6dc1-4215-b9c0-404155eea939",
  "deployment_update_node_instances": {
    ...
  }
  "deployment_update_nodes": [
    ...
  ],
  "central_plugins_to_install": [
    ...
  ],
  "central_plugins_to_uninstall": [
    ...
  ]
}

```

`PUT "<manager-ip>/api/v3.1/deployment-updates/<deployment-id>/update/initiate"`

Update the deployment. **Supported for Cloudify Manager 4.4 and above.**

### URI Parameters
* `deployment-id`: The id of the deployment to update.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`blueprint_id` | string | The id of the blueprint to use for the update
`skip_install` | boolean | Determines whether to skip installing node instances in update workflow
`skip_install` | boolean | Determines whether to skip uninstalling node instances in update workflow
`skip_reinstall` | boolean | Determines whether to reinstall the node instances whose properties or operations are modified in the deployment update
`force` | boolean | Force running the update also in case a deployment is used as a component
`ignore_failure` | boolean | Ignore operation failures while unisntalling node instances in update workflow
`install_first` | boolean | Install new node instances before reinstalling removed ones (default: first uninstall, then install)
`inputs` | object | Dictionary containing inputs to update in the deployment
`reinstall_list` | object | List of IDs for node instances to reinstall (even if skip_reinstall is true)
`preview` | boolean | If set, does not perform the update and returns the steps this update would make (default: False). **Supported for Cloudify Manager 5.0 and above.**
`runtime_eval` | boolean | If set, all intrinsic functions will only be evaluated at runtime, and no intrinsic functions will be evaluated at parse time (such as _get_input_, _get_property_)
`auto_correct_args` | boolean | If set, before creating plan for a new deployment, an attempt will be made to cast old inputs' values to the valid types declared in blueprint
`reevaluate_active_statuses` | boolean | If set, before attempting to update, the statuses of previous active update operations will be reevaluated based on relevant executions' statuses


### Response
A `Deployment Update` resource.


## Get Deployment-Update

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/deployment-updates/<deployment-update-id>?_include=id"
```

```python
# Using CloudifyClient
deployment_update = client.deployment_updates.get(update_id)
```

> Response Example

```json
{
  "old_inputs": {
    ...
  },
  "new_inputs": {
    ...
  },
  "state": "successful",
  "deployment_id": "deployment_1",
  "old_blueprint_id": "blueprint_1",
  "new_blueprint_id": "blueprint_2",
  "steps": [
    ...
  ],
  "tenant_name": "default_tenant",
  "created_at": "2017-12-17T09:28:22.800Z",
  "created_by": "admin",
  "execution_id": "f92754a0-4cf4-4baa-80d3-0602f03f2b91",
  "deployment_update_deployment": {
    ...
  },
  "private_resource": false,
  "visibility": "tenant",
  "resource_availability": "tenant",
  "modified_entity_ids": {
    ...
  },
  "deployment_plan": {
    ...
  },
  "id": "deployment_1-b22cd6b3-6dc1-4215-b9c0-404155eea939",
  "deployment_update_node_instances": {
    ...
  }
  "deployment_update_nodes": [
    ...
  ],
  "central_plugins_to_install": [
    ...
  ],
  "central_plugins_to_uninstall": [
    ...
  ]
}

```

`GET "{manager-ip}/api/v3.1/deployment-updates/<deployment-update-id>"`

Get a deployment update. **Supported for Cloudify Manager 4.4 and above.**

### Response
A `Deployment Update` resource.


## List Deployment Updates

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/deployment-updates?_include=id"
```

```python
# Using CloudifyClient
deployment_updates = client.deployment_updates.list(
        sort=sort_by,
        is_descending=descending,
        _all_tenants=all_tenants,
        _search=search,
        _offset=pagination_offset,
        _size=pagination_size,
        deployment_id=deployment_id
    )
```

> Response Example

```json
{
  "items": [
    {
      "id": "update1"
    },
    {
      "id": "update2"
    },
    {
      "id": "update3"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 3,
      "offset": 0,
      "size": 0
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/deployment-updates"`

Lists deployment updates. **Supported for Cloudify Manager 4.4 and above.**

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Deployment Update` resources.

## Get Deployment Outputs

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>/outputs"
```

```python
# Using CloudifyClient
client.deployments.outputs.get(deployment_id='<deployment-id>')

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments/<deployment-id>/outputs'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
)
response.json()
```

> Response Example

```json
{
  "deployment_id": "dep",
  "outputs": {
    "output_1": "node_vbs4o4",
    "output_2": "some_value"
  }
}
```


`GET "{manager-ip}/api/v3.1/deployments/{deployment-id}/outputs"`

Gets deployment outputs.

### URI Parameters
* `deployment-id`: The id of the deployment.

### Response
A `DeploymentOutput` resource.

## Get Deployment Capabilities

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>/capabilities"
```

```python
# Using CloudifyClient
client.deployments.capabilities.get(deployment_id='<deployment-id>')

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments/<deployment-id>/capabilities'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
)
response.json()
```

> Response Example

```json
{
  "deployment_id": "dep",
  "capabilities": {
    "capability_1": "node_vbs4o4",
    "capability_2": "some_capability"
  }
}
```


`GET "{manager-ip}/api/v3.1/deployments/{deployment-id}/capabilities"`

Gets deployment capabilities. **Supported for Cloudify Manager 4.5.5 and above.**

### URI Parameters
* `deployment-id`: The id of the deployment.

### Response
A `DeploymentOutput` resource.

## Get Inter Deployment Dependencies List

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/deployments/inter-deployment-dependencies"
```

```python
# Using CloudifyClient
client.inter_deployment_dependencies.list()

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments/inter-deployment-dependencies'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=('<manager-username>', '<manager-password>'),
    headers=headers,
)
response.json()
```

> Response Example

```json
{
  "items": [
    {
      "dependency_creator": "nodes.jboss.operations.cloudify.interfaces.lifecycle.stop.inputs.fabric_env.key_filename.get_capability",
      "tenant_name": "default_tenant",
      "created_at": "2020-04-27T06:51:29.543Z",
      "visibility": "tenant",
      "private_resource": false,
      "target_deployment_id": null,
      "resource_availability": "tenant",
      "created_by": "admin",
      "id": "769589d1-51bf-4f18-bcc5-726fa667a10a",
      "source_deployment_id": "jboss-app"
    },
    {
      "dependency_creator": "component.infrastructure_vkd2zx",
      "tenant_name": "default_tenant",
      "created_at": "2020-04-27T06:51:43.124Z",
      "visibility": "tenant",
      "private_resource": false,
      "target_deployment_id": "infrastructure_vkd2zx",
      "resource_availability": "tenant",
      "created_by": "admin",
      "id": "7392a4ad-484c-4b6f-aa42-75d78e884918",
      "source_deployment_id": "jboss-app"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 2,
      "offset": 0,
      "size": 1000
    }
  }
}
```


`GET "{manager-ip}/api/v3.1/deployments/inter-deployment-dependencies"`

Gets an inter deployment dependencies list. **Supported for Cloudify Manager 5.1 and above.**

## Create Inter Deployment Dependency

> Request Example

```shell
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"dependency_creator": "<dependency_creator>", "source_deployment": "<source_deployment>", "target_deployment": "<target_deployment>"}' \
    "http://<manager-ip>/api/v3.1/deployments/inter-deployment-dependencies"
```

```python
# Using CloudifyClient
client.inter_deployment_dependencies.create(
    dependency_creator='<dependency_creator>',
    source_deployment='<source_deployment>',
    target_deployment='<target_deployment>'
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments/inter-deployment-dependencies'
headers = {
    'Content-Type': 'application/json',
    'Tenant': '<manager-tenant>',
}
payload ={
    'dependency_creator': '<dependency_creator>',
    'source_deployment': '<source_deployment>',
    'target_deployment': '<target_deployment>'
}
response = requests.put(
    url,
    auth=('<manager-username>', '<manager-password>'),
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example

```json
{
  "dependency_creator": "component.infrastructure_vkd2zx",
  "tenant_name": "default_tenant",
  "created_at": "2020-04-27T08:24:45.938Z",
  "visibility": "tenant",
  "private_resource": false,
  "target_deployment_id": "infrastructure_vkd2zx",
  "resource_availability": "tenant",
  "created_by": "admin",
  "id": "451f2d61-448a-47db-a786-aa8b64c905ed",
  "source_deployment_id": "jboss-app"
}
```

`PUT -d '{"dependency_creator": "<dependency_creator>", "source_deployment": "<source_deployment>", "target_deployment": "<target_deployment>"}'`

Creates a new inter deployment dependency. **Supported for Cloudify Manager 5.1 and above.**

## Delete Inter Deployment Dependency

> Request Example

```shell
$ curl -X DELETE \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"dependency_creator": "<dependency_creator>", "source_deployment": "<source_deployment>", "target_deployment": "<target_deployment>"}' \
    "http://<manager-ip>/api/v3.1/deployments/inter-deployment-dependencies"
```

```python
# Using CloudifyClient
client.inter_deployment_dependencies.delete(
    dependency_creator='<dependency_creator>',
    source_deployment='<source_deployment>',
    target_deployment='<target_deployment>'
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployments/inter-deployment-dependencies'
headers = {
    'Content-Type': 'application/json',
    'Tenant': '<manager-tenant>',
}
payload ={
    'dependency_creator': '<dependency_creator>',
    'source_deployment': '<source_deployment>',
    'target_deployment': '<target_deployment>'
}
response = requests.delete(
    url,
    auth=('<manager-username>', '<manager-password>'),
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example

```json
{
  "dependency_creator": "component.infrastructure_vkd2zx",
  "tenant_name": "default_tenant",
  "created_at": "2020-04-27T08:24:45.938Z",
  "visibility": "tenant",
  "private_resource": false,
  "target_deployment_id": "infrastructure_vkd2zx",
  "resource_availability": "tenant",
  "created_by": "admin",
  "id": "451f2d61-448a-47db-a786-aa8b64c905ed",
  "source_deployment_id": "jboss-app"
}
```

`DELETE -d '{"dependency_creator": "<dependency_creator>", "source_deployment": "<source_deployment>", "target_deployment": "<target_deployment>"}'`

Deletes an inter deployment dependency. **Supported for Cloudify Manager 5.1 and above.**


## Update (add / delete) Deployment Labels

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"labels": [{"<key1>": "<val1>"}, {"<key2>": "<val2>"}]}' \
    "http://<manager-ip>/api/v3.1/deployments/<deployment-id>"
```

```python
# Python Client
client.deployments.update_labels(
deployment_id='<deployment-id>', 
labels=[{'<key1>': '<val1>', '<key2>': '<val2>'}]
)
```

> Response Example

```json
{
  "inputs": {
    ...
  },
  "permalink": null,
  "description": "deployment_1",
  "blueprint_id": "blueprint_1",
  "policy_types": {
    ...
  },
  "tenant_name": "default_tenant",
  "created_at": "2020-11-29T11:18:01.324Z",
  "updated_at": "2020-11-29T11:18:01.324Z",
  "created_by": "admin",
  "policy_triggers": {
    ...
  },
  "private_resource": false,
  "visibility": "tenant",
  "groups": {
    ...
  },
  "workflows": {
    ...
  },
  "id": "deployment_1",
  "outputs": {
    ...
  },
  "labels": [
    {
      "key": "key2",
      "value": "val2",
      "created_at": "2020-11-29T11:19:03.324Z",
      "creator_id": 0
    },
    {
      "key": "key1",
      "value": "val1",
      "created_at": "2020-11-29T11:19:03.324Z",
      "creator_id": 0
    }
  ]
}

```

`PATCH "<manager-ip>/api/v3.1/deployments/{deployment-id}"`

Update the deployment's labels. **Supported for Cloudify Manager 5.1.1 and above.**

### URI Parameters
* `deployment-id`: The id of the deployment to update.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`labels` | list | A list of the new deployment's labels (required).


### Response
A `Deployment` resource.


## Get all Deployments' Labels' Keys

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/labels/deployments"
```

```python
# Python Client
client.deployments_labels.list_keys()
```

> Response Example

```json
{
  "metadata": {
    "pagination": {
      "total": 5,
      "size": 1000,
      "offset": 0
    }
  },
  "items": [
    "key1",
    "key2"
  ]
}

```

`GET "<manager-ip>/api/v3.1/labels/deployments"`

Get all deployments' labels' keys in the specified tenant. **Supported for Cloudify Manager 5.1.1 and above.**

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of all deployments' labels' keys.


## Get All Deployments' Labels' Values For a Specified Key

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/labels/deployments/<label-key>"
```

```python
# Python Client
client.deployments_labels.list_key_values(label_key='<label-key>')
```

> Response Example

```json
{
  "metadata": {
    "pagination": {
      "total": 5,
      "size": 1000,
      "offset": 0
    }
  },
  "items": [
    "val1"
  ]
}

```

`GET "<manager-ip>/api/v3.1/labels/deployments/<label-key>"`

Get all deployments' labels' values for the specified key. **Supported for Cloudify Manager 5.1.1 and above.**

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of all deployments' labels' values associated with the specified key.

# Deployment Groups

Deployment groups are collections of deployments, that allow operating on multiple deployments in bulk.

## The Deployment Group Resource

A deployment group represents an unordered set of deployments.

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | A unique identifier for the group.
`created_at` | datetime | The time when the group was created.
`created_by` | string | Username of the creator of this group.
`tenant_name` | string | The name of the tenant that owns the group.
`visibility` | string | The visibility of the group.
`resource_availability` | string | The availability of the group.
`private_resource` | boolean | If set, the group will only be accessible by its creator (default: False).
`description` | string | A free-form description of the group.
`default_blueprint_id` | string | ID of the blueprint to be used when creating new deployments in this group.
`default_inputs` | dict | Inputs to be used when creating new deployments in this group.
`deployment_ids` | list | IDs of the deployments belonging to this group.
`labels` | list | Labels attached to the group.


## List Deployment Groups

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/deployment-groups"
```

```python
# Using CloudifyClient
groups = client.deployment_groups.list()

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployment-groups'
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
  "items": [
    {
        "created_at": "2021-04-26T09:02:05.597Z",
        "created_by": "admin",
        "default_blueprint_id": null,
        "default_inputs": {},
        "deployment_ids": [],
        "description": null,
        "id": "g1",
        "labels": [],
        "private_resource": false,
        "resource_availability": "tenant",
        "tenant_name": "default_tenant",
        "visibility": "tenant"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 1,
      "offset": 0,
      "size": 1000
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/deployment-groups"`

Lists all deployment groups.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `DeploymentGroup` resources.


## Get Deployment Group

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/deployment-groups/<group-id>
```

```python
# Using CloudifyClient
client.deployment_groups.get('<deployment-group-id>')

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployment-groups'
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
    "created_at": "2021-04-26T09:02:05.597Z",
    "created_by": "admin",
    "default_blueprint_id": "bp1",
    "default_inputs": {"inp1": "value1"},
    "deployment_ids": ["dep1", "dep2", "dep3"],
    "description": "This is a description",
    "id": "g1",
    "labels": [
      {
          "created_at": "2021-04-26T09:44:40.807Z",
          "creator_id": 0,
          "key": "x",
          "value": "y"
      }
    ],
    "private_resource": false,
    "resource_availability": "tenant",
    "tenant_name": "default_tenant",
    "visibility": "tenant"
}
```


`GET "{manager-ip}/api/v3.1/deployment-groups/<group-id>"`

Gets a deployment group.

### Response
A `DeploymentGroup` resource.

## Create/update Deployment Group

The PUT method creates-or-replaces the deployment group attributes with the ones provided in the request body.

### New deployments
This endpoint can also create new deployments. Provide the specification of the deployments to be created as the `new_deployments` request body field, and new deployments will be created.
This specification is a list of objects that can contain the fields:
 * `id` - if absent, a new deployment ID will be auto-generated
 * `display_name` - sets the display name for the deployment
 * `inputs` - these inputs will be used when creating the new deployment, merged with the `default_inputs` group attribute
 * `labels` - the newly-created deployment will contain these labels. By providing `labels`, it is possible to assign deployment object type, or deployment parents.
Note that this means that `new_deployments` can also be a list of empty objects.
 * `site_name` - the newly-created deployments will have that site assigned
 * `runtime_only_evaluation` - sets the `runtime_only_evaluation` flag for the deployment
 * `skip_plugins_validation` - sets the `skip_plugins_validation` flag for the deployment

### Deployment ID template
The `id` parameter is a string that can contain template parameters:
 * `{uuid}` - replaced with a new UUID4
 * `{group_id}` - replaced with the Deployment Group ID

<aside class="note">
  If the ID template contains the `{uuid}` template, additional uniqueness checks can be skipped, which greatly speeds up creating new deployments.
</aside>

If there are new deployments created, an ExecutionGroup resource will also be
created, containing the new deployments' `create_deployment_environment`
executions.

<aside class="note">
  If <strong>deployment_ids</strong>, <strong>filter_id</strong>, and <strong>deployments_from_group</strong> are all passed in the same request, the group will contain the union of deployments specified by these fields.
</aside>

### Adding existing deployments
There's several ways of adding existing deployments to the group:
 * `deployment_ids` - specify the deployments to be added by the deployments' IDs
 * `filter_id` - add deployments returned by this filter
 * `deployments_from_group` - add deployments belonging to another group, specified by that group's ID

<aside class="warning">
  Providing <strong>filter_id</strong>, <strong>deployment_ids</strong>, or <strong>deployments_from_group</strong> to PUT will replace the group's deployments with the ones defined by these arguments, and deployments belonging to the group before will be unassigned from it.
</aside>

### Labels
Labels added to the group will also be added to all deployments in the group.
New deployments created as part of the group, will inherit the group's labels.
Removing a label from the group will remove it from all deployments in the group.

<aside class="warning">
  These labels rules mean that if a deployment belongs to two groups, and both groups add a label, then one group removes it, then the deployment will <strong>NOT</strong> have that label, even though one of the groups has it.
</aside>

<aside class="note">
  Creating short-lived groups allows a way of assigning labels to a batch of deployments at once.
</aside>

> Request Example

```shell
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    -d '{"description": "hello", "deployment_ids": ["dep1", "dep2"]}' \
    "http://<manager-ip>/api/v3.1/deployment-groups/<group-id>"
```

```python
# Using CloudifyClient
client.deployment_groups.put(
    blueprint_id='<blueprint-id>',
    new_deployments=[
      {
        'labels': [{'csys-environment': 'env1'}],
        'id': 'dep-1',
        'inputs': {'inp1': 'value'}
      }
    ],
    labels=[{'<key1': '<val1>', '<key2>': '<val2>'}]
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployment-groups/<group-id>'
headers = {
    'Content-Type': 'application/json',
    'Tenant': '<manager-tenant>',
}
payload ={
    'blueprint_id': '<blueprint-id>',
    'default_inputs': {'inp1': 'value'},
}
response = requests.put(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    json=payload,
)
response.json()
```

`PUT "{manager-ip}/api/v3.1/deployment-groups/{group-id}"`

### URI Parameters
* `group-id`: The id of the new-or-updated group.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`blueprint_id` | string | The ID of the default blueprint for this group.
`default_inputs` | object | Default inputs for creating new deployments in this group.
`description` | string | A freeform description.
`labels` | list | A list of labels to assign to the group.
`visibility` | string | Optional parameter, defines who can see the deployment (default: tenant). **Supported for Cloudify Manager 4.3 and above.**
`deployment_ids` | list | A list of deployments this group should contain.
`filter_id` | string | The group will contain deployments returned by this filter.
`deployments_from_group` | string | The group will contain deployments that belong to this group.
`new_deployments` | list | Create new deployments specified by this list and add them to the group.

Valid visibility values are:

* `private`: The resource is visible to the user that created the resource, the tenant’s managers and the system’s admins.
* `tenant`: The resource is visible to all users in the current tenant. (Default value)
* `global`: The resource is visible to all users in all tenants across the manager.
A deployment can only be global if the blueprint from which it was created is
also global. Only administrators or users with access to the tenant on which
the deployment was created have permissions to execute workflow on it. **Supported for Cloudify Manager 4.5.5 and above.**

### Response
A `DeploymentGroup` resource.

## Add or remove deployments from group

> Request Example

```shell
$ curl -X PATCH \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"add": {"deployment_ids": ["dep1", "dep2"]}, "remove": {"deployment_ids": ["dep3"]}}'
    "http://<manager-ip>/api/v3.1/deployment-groups/<group-id>
```

```python
client.deployment_groups.add_deployments(
  'group1',
  deployment_ids=['dep1'],
  new_deployments=[{}, {}, {}],
  filter_id='filter1',
  deployments_from_group='group2',
)

client.deployment_groups.add_deployments(
  'group1',
  # the REST client has a `count` shorthand - this is equivalent
  # to `new_deployments` with 10 empty objects
  count=10
)

client.deployment_groups.add_deployments(
  'group1',
  count=20000,
  # the REST client can split creating huge amount of deployments into
  # several requests: in this case it would do 20 PATCH requests behind
  # the scenes
  batch_size=1000,
)

client.deployment_groups.remove_deployments(
  'group1',
  deployment_ids=['dep2'],
  filter_id='filter2',
  deployments_from_group='group3',
)
```

`PATCH "{manager-ip}/api/v3.1/deployment-groups/{group-id}"`

Adding or removing deployments from a group without overwriting the whole group
or its contents is done by specifying the deployments to add and to remove in the
body of a PATCH request.

The body of that request can contain the objects `add` or `remove`, specifying
the deployments to be added and deleted. These object contain keys similar to the
deployment-adding fields that the PUT request supports.

If a deployment is both added and removed at the same time (possibly using
different ways, eg. added by filter but removed by id), it stays removed.

### Adding deployments
The `add` object can contain the following fields (those are the same fields
that were available for specifying deployments in the PUT request):

* `deployment_ids`: add deployments specified by their IDs
* `filter_id`: add deployments returned by this filter
* `deployments_from_group`: add deployments belonging to another group, specified by that group's ID
* `new_deployments`: create new deployments in the group. Same semantics as in the PUT request.

<aside class="note">
  When adding huge amounts of deployments (tens of thousands), you might want to split the request
  into several batches, to only create reasonable amounts in each request: remember that the manager
  will have to parse and process the inputs for each deployment, and this object could become
  many megabytes of data.

  The time this request would take depends highly on the manager machine and the connection to it,
  but amounts on the order of 5000 are considered safe, while amounts on the order of 50000 are
  considered too high.
</aside>

### Removing deployments
The `remove` object can contain the following fields (these are similar to
the ones available in `add` or in the PUT request, except for `new_deployments`):

* `deployment_ids`: remove the deployment specified by their IDs
* `filter_id`: remove deployments returned by this filter
* `deployments_from_group`: remove deployments belonging to the group given by this ID


### Request Body
Property | Type | Description
--------- | ------- | -----------
add | object | Specify the deployments to be added to the group
remove | object | Specify the deployments to be removed from the group

### Response
A `DeploymentGroup` resource.

## Delete Deployment Group

> Request Example

```shell
$ curl -X DELETE \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/deployment-groups/<group-id>
```

```python
# Using CloudifyClient
client.deployment_groups.delete(
    '<group-id>',
    delete_deployments=False,
    force=False,
    with_logs=False)

# Using requests
url = 'http://<manager-ip>/api/v3.1/deployment-groups/<group-id>'
headers = {'Tenant': '<manager-tenant>'}
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

`DELETE "{manager-ip}/api/v3.1/deployment-groups/{group-id}"`

Deletes a deployment group. If `delete_deployments` is "true", also bulk-delete all deployments in the group.
In case of deleting deployments, same semantics as in Deployments DELETE apply, regarding live nodes and the `force` flag

<aside class="warning">
  Use with caution - deleting a set of deployments is an <strong>EXTREMELY</strong> destructive operation!
</aside>

### URI Parameters
* `delete_deployments`: if "true", also delete all deployments belonging to this group
* `force`: Same meaning as in Deployments DELETE
* `delete_logs`: Same meaning as in Deployments DELETE


### Response
No content - HTTP code 204.

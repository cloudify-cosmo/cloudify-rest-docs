# Permissions

The permissions endpoints allow assigning and removing specific permissions from roles.

## The Permission resource

### Attributes:

Attribute | Type | Description
`permission` | string | The name of the permission, eg. "blueprint_list"
`role` | string | The role that has the permission, eg. "operations"

## List all permissions

> Request Example

```shell
$ curl -X GET \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/permissions"
```

```python
permissions = client.permissions.list()

for p in permissions:
    print("role ", p['role'], " has permission ", p['permission'])
```

> Response Example

```json
{
  "items": [
    {"role": "operations", "permission": "agent_list"},
    {"role": "operations", "permission": "agent_create"},
    {"role": "operations", "permission": "agent_update"},
    ...
  ],
  "metadata": {
    "pagination": {
      "total": 128,
      "offset": 0,
      "size": 1000
    }
  }
}
```


`GET "{manager-ip}/api/v3.1/permissions"`

Lists all permissions, assigned to all roles.

### Response

List of Permission resources.


## List permission for a given role

> Request Example

```shell
$ curl -X GET \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/permissions/<role-name>"
```

```python
permissions = client.permissions.list(role='<role-name>')
```

> Response Example

```json
{
  "items": [
    {"role": "operations", "permission": "agent_list"},
    {"role": "operations", "permission": "agent_create"},
    {"role": "operations", "permission": "agent_update"},
    ...
  ],
  "metadata": {
    "pagination": {
      "total": 128,
      "offset": 0,
      "size": 1000
    }
  }
}
```


`GET "{manager-ip}/api/v3.1/permissions/{role-name}"`

Lists all permissions, assigned to the given role.

### Response

List of Permission resources.


## Assign permission for a role

> Request Example

```shell
$ curl -X PUT \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/permissions/<role-name>/<permission-name>"
```

```python
permissions = client.permissions.add(
    permission='blueprint_list',
    role='viewer'
)
```

`PUT "{manager-ip}/api/v3.1/permissions/{role-name}/{permission-name}"`

Add a permission to a role. Users who have this role assigned will immediately
be able to use endpoints that require the added permission.

### Response

The newly-created Permission resource.

## Remove permission from a role

> Request Example

```shell
$ curl -X DELETE \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/permissions/<role-name>/<permission-name>"
```

```python
permissions = client.permissions.delete(
    permission='blueprint_list',
    role='viewer'
)
```

`DELETE "{manager-ip}/api/v3.1/permissions/{role-name}/{permission-name}"`

Remove a permission from a role. Users who have this role will immediately
be prevented from using endpoints that require the removed permission
(unless they also have another role that allows it).

### Response

No content.

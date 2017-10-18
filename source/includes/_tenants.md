# Tenants

## The Tenant Resource

<aside class="notice">
This section describes API features that are part of the Cloudify premium edition
</aside>

> `Note`

```python
# include this code when using cloudify python client-
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
        host='<manager-ip>',
        username='<manager-username>',
        password='<manager-password>',
        tenant='<manager-tenant>')
```

The Tenant resource is a logical component that represents a closed environment with its own resources.


### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | integer | Auto increment, unique identifier for the tenant.
`name` | string | The tenant's name.


## List Tenants

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: default_tenant" \
    -u <user>:<password> \
    "http://<manager-ip>/api/v3.1/tenants"
```

```python
# Python Client-
client.tenants.list()
```

> Response Example

```json
{
 "items":
    [
        {
            "name": "default_tenant",
            "groups": 0,
            "users": 1
        }
    ]
}
```

`GET "{manager-ip}/api/v3.1/tenants"`

List all tenants.


### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Tenant` resources.

## Get Tenant

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: default_tenant" \
    -u <user>:<password> \
    "http://<manager-ip>/api/v3.1/tenants/{tenant-name}"
```

```python
# Python Client-
client.tenants.get('default_tenant')
```

> Response Example

```json
{
    "name": "default_tenant",
    "groups": 0,
    "users": 1
}
```

`GET "{manager-ip}/api/v3.1/tenants?name={tenant-name}"`

Retrieves a specific tenant.

### URI Parameters
* `tenant-name`: The name of the tenant to retrieve.

### Response
A `Tenant` resource.




## Create Tenant

> Request Example

```shell
$ curl -X POST \
    -H "Content-Type: application/json" \
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    "http://<manager-ip>/api/v3.1/tenants/<new-tenant-name>"
```

```python
# Python Client-
client.tenants.create(<new-tenant-name>)
```

> Response Example

```json
{
    "name": "new_tenant",
    "groups": 0,
    "users": 0
}
```

`POST "{manager-ip}/api/v3.1/tenants/{new-tenant-name}"`

Creates a tenant.

### URI Parameters
* `new-tenant-name`: The name of the tenant to create.

### Response
A `Tenant` resource.





## Delete Tenant

> Request Example

```shell
$ curl -X DELETE \
    -H "Content-Type: application/json" \
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    "http://<manager-ip>/api/v3.1/tenants/<tenant-name-to-delete>"
```

```python
# Python Client-
client.tenants.delete(<tenant-name>)
```

> Response Example

```json
{
    "name": "tenant-name",
    "groups": 0,
    "users": 0
}
```

`DELETE "{manager-ip}/api/v3.1/tenants/{tenant-name-to-delete}"`

Delete a tenant.

### URI Parameters
* `tenant-name-to-delete`: The name of the tenant to delete.

### Response
A `Tenant` resource.





## Add User to Tenant

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    -d '{"username": <user-name>, "tenant_name": <tenant-name>, "role": <role_name>}' \
    "http://<manager-ip>/api/v3.1/tenants/users"
```

```python
# Python Client-
client.tenants.add_user(<user-name>, <tenant-name>, <role>)
```

> Response Example

```json
{
    "name": "<tenant-name>",
    "groups": 0,
    "users": 1
}
```

`PUT "{manager-ip}/api/v3.1/tenants/users"`

Add a user to a tenant.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username` | string | The user name to add to the tenant.
`tenant_name` | string | The name of the tenant to which to add the user.
`role` | string | (Optional) The name of the role assigned to the user in the tenant. If not passed the default tenant role will be used.

### Response
A `Tenant` resource.





## Remove User from Tenants

> Request Example

```shell
$ curl -X DELETE \
    -H "Content-Type: application/json"
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    -d '{"username": <user-name>, "tenant_name": <tenant-name>}' \
     "http://<manager-ip>/api/v3.1/tenants/users"
```

```python
# Python Client-
client.tenants.remove_user(<user-name>, <tenant-name>)
```

> Response Example

```json
{
    "name": "tenant-name",
    "groups": 0,
    "users": 0
}
```

`DELETE "{manager-ip}/api/v3.1/tenants/users"`

Delete a user from a tenant.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username` | string | The user name to remove from the tenant.
`tenant_name` | string | The tenant name to add the user into it.

### Response
A `Tenant` resource.





## Add User-Group to Tenant

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    -d '{"group_name": <group-name>, "tenant_name": <tenant-name>, "role": <role-name>}' \
    "http://<manager-ip>/api/v3.1/tenants/user-groups"
```

```python
# Python Client-
client.tenants.add_group(<group-name>, <tenant-name>, <role>)
```

> Response Example

```json
{
    "name": "tenant-name",
    "groups": 1,
    "users": 0
}
```

`PUT "{manager-ip}/api/v3.1/tenants/user-groups"`

Add a user group to a tenant.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`group_name` | string | The name of the user group to add to the tenant.
`tenant_name` | string | The name of the tenant to which to add the user group.
`role` | string | (Optional) The name of the role assigned to the users members of the group. If not passed the default tenant role will be used.

### Response
A `Tenant` resource.





## Remove User-Group from Tenants

> Request Example

```shell
$ curl -X DELETE \
    -H "Content-Type: application/json" \
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    -d '{"group_name": <group-name>, "tenant_name": <tenant-name>}' \
    "http://<manager-ip>/api/v3.1/tenants/user-groups"
```

```python
# Python Client-
client.tenants.remove_user(<group-name>, <tenant-name>)
```

> Response Example

```json
{
    "name": "tenant-name",
    "groups": 0,
    "users": 0
}
```

`DELETE "{manager-ip}/api/v3.1/tenants/user-groups"`

Delete a user group from a tenant.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`group_name` | string | The name of the user group to delete from the tenant.
`tenant_name` | string | The name of the tenant from which to delete the user group.

### Response
A `Tenant` resource.

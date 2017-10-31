# User Groups

## The User Group Resource

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

The User Group is a group of users.


### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | integer | Auto increment, unique identifier for the tenant.
`ldap_dn` | string | The distinguished name of corresponding LDAP group (if using LDAP).
`name` | string | The name of the user group.


## List User Groups

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<password> \
    "http://<manager_ip>/api/v3.1/user-groups"
```

```python
# Python Client-
client.user_groups.list()
```

> Response Example

```json
{
    "items":
        [
            {
                "ldap_dn": null,
                "tenants": [],
                "name": "new_group",
                "users": []
            }
        ]
}
```

`GET "{manager-ip}/api/v3.1/user-groups"`

List all user groups.

### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Group` resources.


## Get User Group

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/user-groups/<group_name>"
```

```python
# Python Client-
client.user_groups.get(<group-name>)
```

> Response Example

```json
{
    "ldap_dn": null,
    "name": "new_group",
    "tenants": [],
    "users": []
}
```

`GET "{manager-ip}/api/v3.1/user-groups/{group-name}"`

Retrieves a specific group.

### URI Parameters
* `group-name`: The name of the group to retrieve.

### Response
A `Group` resource.


## Create User Groups

> Request Example

```shell
$ curl -X POST \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"group_name": <group_name>, "ldap_group_dn": <optional_ldap_dn>}' \
    "http://<manager_ip>/api/v3.1/user-groups"
```

```python
# Python Client-
client.user_groups.create(group_name=<group-name>, ldap_group_dn=<optional-ldap-dn>)
```

> Response Example

```json
{
    "ldap_dn": "group_ldap_dn",
    "name": "new_group",
    "tenants": [],
    "users": []
}
```

`POST -d '{"group_name": <group-name>, "ldap_group_dn": <optional-ldap-dn>}' "{manager-ip}/api/v3.1/user-groups"`

Creates a new user group.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`group_name` | string | The group name.
`ldap_group_dn` | string | Optional parameter, The distinguishing name of the corresponding LDAP group, if appropriate.

### Response
A `User` resource.





## Delete User Group

> Request Example

```shell
$ curl -X DELETE \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/user-groups/<user_group_name_to_delete>"
```

```python
# Python Client-
client.user_groups.delete(<group-name>)
```

> Response Example

```json
{
    "ldap_dn": "group_ldap_dn",
    "name": "new_group",
    "tenants": [],
    "users": []
}
```

`DELETE "{manager-ip}/api/v3.1/user-groups/{user-group-to-delete}"`

Deletes a user group.

### URI Parameters
* `user-group-to-delete`: The name of the user group to delete.

### Response
A `Group` resource.





## Add User to Group

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"username": <username>, "group_name": <group_name>}' \
    "http://<manager_ip>/api/v3.1/user-groups/users"
```

```python
# Python Client-
client.user_groups.add_user(<user-name>, <group-name>)
```

> Response Example

```json
{
    "ldap_dn": "group_ldap_dn",
    "name": "new_group",
    "tenants": [],
    "users": ["user_name"]
}
```

`PUT "{manager-ip}/api/v3.1/user-groups/users"`

Add a user to group.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username` | string | The name of the user to add to the group.
`group_name` | string | The name of the group to which to add the user.

### Response
A `Group` resource.





## Remove User from Group

> Request Example

```shell
$ curl -X DELETE \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"username": <username>, "group_name": <group_name>}' \
    "http://<manager_ip>/api/v3.1/user-groups/users"
```

```python
# Python Client-
client.user_groups.remove_user(<user-name>, <group-name>)
```

> Response Example

```json
{
    "ldap_dn": "group_ldap_dn",
    "name": "new_group",
    "tenants": [],
    "users": ["user_name"]
}
```

`DELETE "{manager-ip}/api/v3.1/user-groups/users"`

Delete a user from a group.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username` | string | The name of the user to remove from the group.
`group_name` | string | The name of the group from which to remove the user.

### Response
A `Group` resource.

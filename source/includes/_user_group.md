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

```html

```

The User Group is a group of users.


### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | integer | Auto increment, unique identifier for the tenant.
`name` | string | The name of the user group.
`ldap_dn` | string | The distinguish name of corresponding LDAP group (if using LDAP).




## Get User Group

> Request Example

```shell
$ curl -X GET --header "tenant: default_tenant" -u user:password "http://<manager-ip>/api/v3/user-groups/<group-name>"
```

```python
# Python Client-
client.user_groups.get(<group-name>)
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/users/<group-name>",
  "method": "GET",
  "headers": headers
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
obsolete
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

`GET "{manager-ip}/api/v3/user-groups/{group-name}"`

Retrieves a specific group.

### URI Parameters
* `group-name`: The name of the group to retrieve.

### Response
A `Group` resource.





## List User Groups

> Request Example

```shell
$ curl -X GET --header "tenant: default_tenant" -u user:password "http://<manager-ip>/api/v3/user-groups"
```

```python
# Python Client-
client.user_groups.list()
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': 'default_tenant'
}

var settings = {
  "url": "http://<manager-ip>/api/v3/user-groups",
  "method": "GET",
  "headers": headers
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
obsolete
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

`GET "{manager-ip}/api/v3/user-groups"`

List all user groups.

### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Group` resources.



## Create User Groups

> Request Example

```shell
$ curl -X POST -H "Content-Type: application/json" -H "tenant: default_tenant" -d '{"group_name": <group-name>, "ldap_group_dn": <optional-ldap-dn>}' -u user:password "http://<manager-ip>/api/v3/user-groups"
```

```python
# Python Client-
client.user_groups.create(group_name=<group-name>, ldap_group_dn=<optional-ldap-dn>)
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

vat data = {
    "group_name": <group-name>,
    "ldap_group_dn": <optional-ldap-dn>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/user-groups",
  "method": "POST",
  "headers": headers,
  "data": data
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
obsolete
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

`POST -d '{"group_name": <group-name>, "ldap_group_dn": <optional-ldap-dn>}' "{manager-ip}/api/v3/user-groups"`

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
$ curl -X DELETE -H "Content-Type: application/json" -H "tenant: <tenant-name>" -u user:password "http://<manager-ip>/api/v3/user-groups/<user-group-name-to-delete>"
```

```python
# Python Client-
client.user_groups.delete(<group-name>)
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/user-groups/<user-group-name-to-delete>",
  "method": "DELETE",
  "headers": headers
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
obsolete
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

`DELETE "{manager-ip}/api/v3/user-groups/{user-group-to-delete}"`

Deletes a user group.

### URI Parameters
* `user-group-to-delete`: The name of the user group to delete.

### Response
A `Group` resource.





## Add User to Group

> Request Example

```shell
$ curl -X PUT -H "Content-Type: application/json" -H "tenant: <tenant-name>" -u user:password -d '{"username": <user-name>, "group_name": <group-name>}' `"http://<manager-ip>/api/v3/user-groups/users"
```

```python
# Python Client-
client.user_groups.add_user(<user-name>, <group-name>)
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

vat data = {
    "username": <user-name>,
    "group_name": <group-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/user-groups/users",
  "method": "PUT",
  "headers": headers,
  "data": data
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
obsolete
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

`PUT "{manager-ip}/api/v3/user-groups/users"`

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
$ curl -X DELETE -H "Content-Type: application/json" -H "tenant: <tenant-name>" -u user:password -d '{"username": <user-name>, "group_name": <group-name>}' `"http://<manager-ip>/api/v3/user-groups/users"
```

```python
# Python Client-
client.user_groups.remove_user(<user-name>, <group-name>)
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

vat data = {
    "username": <user-name>,
    "group_name": <group-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/user-groups/users",
  "method": "DELETE",
  "headers": headers,
  "data": data
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
obsolete
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

`DELETE "{manager-ip}/api/v3/user-groups/users"`

Delete a user from a group.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username` | string | The name of the user to remove from the group.
`group_name` | string | The name of the group from which to remove the user.

### Response
A `Group` resource.
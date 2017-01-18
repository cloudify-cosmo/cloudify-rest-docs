# Users

## The User Resource

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

Since Cloudify 4.0, Cloudify user management has been added


### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | integer | Auto increment, unique identifier for the tenant.
`username` | string | The username.
`password` | string | The user hashed password.
`first_name` | string | The user's first name..
`last_name` | string | The user's last name.
`active` | boolean | Whether the user's status is active or suspended.
`created_at` | UTCDateTime | Date on which the user was created.
`last_login_at` | UTCDateTime | Date of last request performed by the user.




## Get User

> Request Example

```shell
$ curl -X GET --header "tenant: default_tenant" -u user:password "http://<manager-ip>/api/v3/users/<user-name>"
```

```python
# Python Client-
client.users.get(<user-name>)
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/users/<user-name>",
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
    "username": "admin",
    "last_login_at": "2017-01-22T15:09:33.799Z",
    "role": "administrator",
    "groups": [],
    "active": true,
    "tenants": ["default_tenant"]
}
```

`GET "{manager-ip}/api/v3/users/{user-name}"`

Retrieves a specific user.

### URI Parameters
* `user-name`: The name of the user to retrieve.

### Response
A `User` resource.





## List Users

> Request Example

```shell
$ curl -X GET --header "tenant: default_tenant" -u user:password "http://<manager-ip>/api/v3/users"
```

```python
# Python Client-
client.users.list()
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': 'default_tenant'
}

var settings = {
  "url": "http://<manager-ip>/api/v3/users",
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
            "username": "admin",
            "last_login_at": "2017-01-22T15:09:33.799Z",
            "role": "administrator",
            "groups": [],
            "active": true,
            "tenants": ["default_tenant"]
        }
    ]
}
```

`GET "{manager-ip}/api/v3/users"`

List all users.

### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `User` resources.



## Create User

> Request Example

```shell
$ curl -X PUT -H "Content-Type: application/json" -H "tenant: <tenant-name>" -d '{"username": <new-user-name>, "password": <password>, "role": <role>}' -u admin:dbm4uXXPjCuL "http://172.20.0.2/api/v3/users"
```

```python
# Python Client-
client.users.create(<new-user-name>,
                    <password>,
                    <role>)
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

vat data = {
    "username": <new-user-name>,
    "password": <password>,
    "role": <role>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/users/<new-tenant-name>",
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
    "username": "admin",
    "last_login_at": "2017-01-22T15:09:33.799Z",
    "role": "administrator",
    "groups": [],
    "active": true,
    "tenants": ["default_tenant"]
}
```

`PUT -d '{"username": <new-user-name>, "password": <password>, "role": <role>}' "{manager-ip}/api/v3/users"`

Creates a new user.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username` | string | The username.
`password` | string | The user password.
`role` | string | The user role. One of the following: `user`, `administrator`, `suspended`.

### Response
A `User` resource.





## Delete User

> Request Example

```shell
$ curl -X DELETE -H "Content-Type: application/json" -H "tenant: <tenant-name>" -u user:password "http://<manager-ip>/api/v3/tenants/<user-name-to-delete>"
```

```python
# Python Client-
client.users.delete(<user-name>)
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/tenants/<user-name>",
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
    "username": "user",
    "last_login_at": "2017-01-22T15:09:33.799Z",
    "role": "user",
    "groups": [],
    "active": true,
    "tenants": ["default_tenant"]
}
```

`DELETE "{manager-ip}/api/v3/tenants/{user-name-to-delete}"`

Delete a user.

### URI Parameters
* `user-name-to-delete`: The name of the user to delete.

### Response
A `User` resource.

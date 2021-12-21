# Users

## The User Resource

<aside class="notice">
This section describes API features that are part of the Cloudify premium edition
</aside>

Since Cloudify 4.0, Cloudify user management has been added


### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`active` | boolean | Whether the user's status is active or suspended.
`username` | string | The username.
`first_login_at` | UTCDateTime | Date of first request performed by the user.
`last_login_at` | UTCDateTime | Date of last request performed by the user.
`is_locked` | boolean | Whether the user is temporarily locked out (due to numerous failed login attempts).
`tenant_roles` | set | The roles of the tenant user is associated with.
`role` | string | The role of the user (the first one in case there are many).
`groups` | list | The groups the user belongs to
`tenants` | object | Dictionary of tenants the user is associated with.
`group_system_roles` | object | Dictionary of lists of groups the user is associated with, per the role.
`show_getting_started` | boolean | Whether the user will be displayed the "Getting started" modal upon logging in.


## List Users

> Request Example - List users (tenants and user groups count)

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/users"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
)
client.users.list()

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/users'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
)
```

> Response Example - List users (tenants and user groups count)

```json
{
  "items": [
    {
      "active": true,
      "first_login_at": "2021-12-20T16:17:13.673Z",
      "group_system_roles": {},
      "groups": 0,
      "is_locked": false,
      "last_login_at": "2021-12-21T13:05:47.533Z",
      "role": "sys_admin",
      "show_getting_started": false,
      "tenant_roles": null,
      "tenants": 1,
      "username": "admin"
    }
  ],
  "metadata": {
    "filtered": null,
    "pagination": {
      "offset": 0,
      "size": 1000,
      "total": 1
    }
  }
}
```

> Request Example - List users (tenants and user groups details)

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/users?_get_data=true"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
)
client.users.list(_get_data=True)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/users?_get_data=true'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
)
```

> Response Example - Get tenants and user groups details

```json
{
  "items": [
    {
      "active": true,
      "first_login_at": "2021-12-20T16:17:13.673Z",
      "group_system_roles": {},
      "groups": [],
      "is_locked": false,
      "last_login_at": "2021-12-21T13:29:07.079Z",
      "password_hash": null,
      "role": "sys_admin",
      "show_getting_started": false,
      "tenant_roles": {
        "direct": {
          "default_tenant": "user"
        },
        "groups": {}
      },
      "tenants": {
        "default_tenant": {
          "roles": [
            "user"
          ],
          "tenant-role": "user"
        }
      },
      "username": "admin"
    }
  ],
  "metadata": {
    "filtered": null,
    "pagination": {
      "offset": 0,
      "size": 1000,
      "total": 1
    }
  }
}
```

`GET "{manager_ip}/api/v3.1/users"`

List all users.

### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `User` resources.


## Get User

> Request Example - Get user

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/users/<username>"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
)
client.users.get(<username>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/users/<username>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
)
```

> Response Example - Get user

```json
{
    "active": true,
    "first_login_at": "2021-12-20T16:17:13.673Z",
    "group_system_roles": {},
    "groups": 0,
    "is_locked": false,
    "last_login_at": "2021-12-21T13:32:06.194Z",
    "password_hash": null,
    "role": "sys_admin",
    "show_getting_started": false,
    "tenant_roles": null,
    "tenants": 1,
    "username": "admin"
}
```

> Request Example - Get user

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/users/<username>?_get_data=true"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
)
client.users.get('<username>', _get_data=True)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/users/<username>?_get_data=true'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
)
```

> Response Example - Get user

```json
{
  "active": true,
  "first_login_at": "2021-12-20T16:17:13.673Z",
  "group_system_roles": {},
  "groups": [],
  "is_locked": false,
  "last_login_at": "2021-12-21T15:48:25.067Z",
  "password_hash": null,
  "role": "sys_admin",
  "show_getting_started": false,
  "tenant_roles": {
    "direct": {
      "default_tenant": "user"
    },
    "groups": {}
  },
  "tenants": {
    "default_tenant": {
      "roles": [
        "user"
      ],
      "tenant-role": "user"
    }
  },
  "username": "admin"
}
```

`GET "{manager_ip}/api/v3.1/users/{username}"`

Retrieves a specific user.

### URI Parameters
* `username`: The name of the user to retrieve.

### Response
A `User` resource.


## Create User

> Request Example - Create user

```shell
$ curl -X PUT \
    -H "Content-Type: application/json"
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"username": <new_username>, "password": <password>, "role": <role_name>}'
    "http://{manager_ip}/api/v3.1/users"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
)
client.users.create(
    '<new_username>',
    '<password>',
    '<role_name>',
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/users'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'username': '<new_username>',
    'password': '<password>',
    'role': '<role_name>',
}
response = requests.put(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
```

> Response Example - Create user

```json
{
  "active": true,
  "first_login_at": "2021-12-20t16:17:13.673z",
  "group_system_roles": {},
  "groups": 0,
  "is_locked": false,
  "last_login_at": "2021-12-21t13:32:06.194z",
  "password_hash": null,
  "role": "sys_admin",
  "show_getting_started": false,
  "tenant_roles": null,
  "tenants": 1,
  "username": "admin"
}
```

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username` | string | The username.
`password` | string | The user password.
`role` | string | The user role. One of the following: `sys_admin`, `default`.

Valid system roles are:

* `sys_admin` - User that can manage Cloudify

* `default` - User exists, but has no special permissions


### Response
A `User` resource.


## Delete User

> Request Example

```shell
$ curl -X DELETE \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/users/<username_to_delete>"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
)
client.users.delete('<username_to_delete>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/users/<username_to_delete>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
requests.delete(
    url,
    auth=auth,
    headers=headers,
)
```

`DELETE "{manager_ip}/api/v3.1/tenants/{username_to_delete}"`

Delete a user.

### URI Parameters
* `username_to_delete`: The name of the user to delete.

### Response
No content - HTTP code 204.




## Set user password

> Request Example - Set user password

```shell
$ curl -X POST \
    -H "Content-Type: application/json"
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"password": <new_password>}' \
    "http://<manager_ip>/api/v3.1/users/<username>"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
)
client.users.set_password('<username>', '<new_password>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/users/<username>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {'password': '<new_password>'}
response = requests.post(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
```

> Response Example - Set user password

```json
{
  "active": true,
  "first_login_at": "2021-12-20T16:17:13.673Z",
  "group_system_roles": {},
  "groups": 0,
  "is_locked": false,
  "last_login_at": "2021-12-21T13:32:06.194Z",
  "password_hash": null,
  "role": "sys_admin",
  "show_getting_started": false,
  "tenant_roles": null,
  "tenants": 1,
  "username": "admin"
}
```

Specify a password.

### URI Parameters
* `username`: The name of the user whose password is to be changed.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`password` | string | The new user password.

### Response
A `User` resource.


## Set user role

> Request Example - Set user role

```shell
$ curl -X POST \
    -H "Content-Type: application/json" \
    -H "tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"role": <user_role>}' \
    "http://<manager_ip>/api/v3.1/users/<username>"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
)
client.users.set_role('<username>', '<new_role_name>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/users/<username>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {'role': '<new_role_name>'}
response = requests.post(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
```

> Response Example - Set user role

```json
{
  "active": true,
  "first_login_at": "2021-12-20T16:17:13.673Z",
  "group_system_roles": {},
  "groups": 0,
  "is_locked": false,
  "last_login_at": "2021-12-21T13:32:06.194Z",
  "password_hash": null,
  "role": "sys_admin",
  "show_getting_started": false,
  "tenant_roles": null,
  "tenants": 1,
  "username": "admin"
}
```


`POST -d '{"role": <new_role_name>}' "{manager_ip}/api/v3.1/users/{username}"`

Set a new system role for the user.


### URI Parameters
* `username`: The name of the user whose role is to be set.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`role` | string | The user role. One of the following: `sys_admin`, `default`.

Valid system roles are:

* `sys_admin` - User that can manage Cloudify

* `default` - User exists, but has no special permissions


### Response
A `User` resource.

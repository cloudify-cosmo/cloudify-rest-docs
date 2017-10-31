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
`created_at` | UTCDateTime | Date on which the user was created.
`first_name` | string | The user's first name..
`id` | integer | Auto increment, unique identifier for the tenant.
`last_login_at` | UTCDateTime | Date of last request performed by the user.
`last_name` | string | The user's last name.
`password` | string | The user hashed password.
`username` | string | The username.


## List Users

> Request Example - Get tenants and user groups count

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

> Response Example - Get tenants and user groups count

```json
{
  "items": [
    {
      "username": "admin",
      "last_login_at": "2017-10-30T15:45:25.703Z",
      "role": "sys_admin",
      "groups": 0,
      "active": true,
      "tenants": 1
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

> Request Example - Get tenants and user groups details

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
      "username": "admin",
      "last_login_at": "2017-10-31T10:38:53.227Z",
      "role": "sys_admin",
      "groups": [],
      "active": true,
      "tenants": {
        "default_tenant": {
          "tenant-role": "user",
          "roles": [
            "user"
          ]
        }
      }
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

`GET "{manager_ip}/api/v3.1/users"`

List all users.

### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `User` resources.





## Get User

> Request Example - Get tenants and user groups count

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

> Response Example - Get tenants and user groups count

```json
{
  "username": "admin",
  "last_login_at": "2017-10-30T15:53:04.951Z",
  "role": "sys_admin",
  "groups": 0,
  "active": true,
  "tenants": 1
}
```

> Request Example - Get tenants and user groups details

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

> Response Example - Get tenants and user groups details

```json
{
  "username": "admin",
  "last_login_at": "2017-10-31T10:47:20.220Z",
  "role": "sys_admin",
  "groups": [],
  "active": true,
  "tenants": {
    "default_tenant": {
      "tenant-role": "user",
      "roles": [
        "user"
      ]
    }
  }
}
```

`GET "{manager_ip}/api/v3.1/users/{username}"`

Retrieves a specific user.

### URI Parameters
* `username`: The name of the user to retrieve.

### Response
A `User` resource.


## Create User

> Request Example - Get tenants and user groups count

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

> Response Example - Get tenants and user groups count

```json
{
  "username": "<new_username>",
  "last_login_at": null,
  "role": "<role_name>",
  "groups": 0,
  "active": true,
  "tenants": 0
}
```

> Request Example - Get tenants and user groups details

```shell
$ curl -X PUT \
    -H "Content-Type: application/json"
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"username": <new_username>, "password": <password>, "role": <role_name>}'
    "http://{manager_ip}/api/v3.1/users?_get_data=true"
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
    _get_data=True,
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/users?_get_data=true'
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

> Response Example - Get tenants and user groups details

```json
{
  "username": "<new_username>",
  "last_login_at": null,
  "role": "<role_name>",
  "groups": [],
  "active": true,
  "tenants": {}
}
```
`PUT -d '{"username": <new_username>, "password": <password>, "role": <role_name>}' "{manager_ip}/api/v3.1/users"`

Creates a new user.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`new_username` | string | The username.
`password` | string | The user password.
`role_name` | string | The user role. One of the following: `sys_admin`, `default`.

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
response = requests.delete(
    url,
    auth=auth,
    headers=headers,
)
```

> Response Example

```json
{
  "username": "<username_to_delete>",
  "last_login_at": null,
  "role": "default",
  "groups": 0,
  "active": true,
  "tenants": 0
}
```

`DELETE "{manager_ip}/api/v3.1/tenants/{username_to_delete}"`

Delete a user.

### URI Parameters
* `username_to_delete`: The name of the user to delete.

### Response
A `User` resource.




## Set user password

> Request Example

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

> Response Example

```json
{
  "username": "<username>",
  "last_login_at": null,
  "role": "default",
  "groups": 0,
  "active": true,
  "tenants": 0
}
```

`POST -d '{"password": <new_password>}' '"{manager_ip}/api/v3.1/users/{username}"`

Specify a password.

### URI Parameters
* `username`: The name of the user whose password is to be changed.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`new_password` | string | The new user password.

### Response
A `User` resource.



## Set user role

> Request Example

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

> Response Example

```json
{
  "username": "<username>",
  "last_login_at": null,
  "role": "default",
  "groups": 0,
  "active": true,
  "tenants": 0
}
```

`POST -d '{"role": <new_role_name>}' '"{manager_ip}/api/v3.1/users/{username}"`

Set a new system role for the user.


### URI Parameters
* `username`: The name of the user whose role is to be set.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`new_role_name` | string | The user role. One of the following: `sys_admin`, `default`.

Valid system roles are:

* `sys_admin` - User that can manage Cloudify

* `default` - User exists, but has no special permissions


### Response
A `User` resource.

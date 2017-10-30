# Tenants

## The Tenant Resource

<aside class="notice">
This section describes API features that are part of the Cloudify premium edition
</aside>

The Tenant resource is a logical component that represents a closed environment with its own resources.


### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | integer | Auto increment, unique identifier for the tenant.
`name` | string | The tenant's name.


## List Tenants

> Request Example - Get user and user group counts

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/tenants"
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
client.tenants.list()

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
)
response.json()
```

> Response Example - Get user and user group counts

```json
{
  "items": [
    {
      "name": "default_tenant",
      "groups": 0,
      "users": 1
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

> Request Example - Get user and user group details

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/tenants?_get_data=true"
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
client.tenants.list(_get_data=True)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants?_get_data=true'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
)
response.json()
```

> Response Example - Get user and user group details

```json
{
  "items": [
    {
      "name": "default_tenant",
      "groups": {},
      "users": {
        "admin": {
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

`GET "{manager_ip}/api/v3.1/tenants"`

List all tenants.


### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Tenant` resources.

## Get Tenant

> Request Example - Get user and user group counts

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/tenants/{tenant_name}"
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
client.tenants.get('<tenant_name>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/<tenant_name>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
)
response.json()
```

> Response Example - Get user and user group counts

```json
{
    "name": "<tenant_name>",
    "groups": 0,
    "users": 1
}
```

> Request Example - Get user and user group details

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/tenants/{tenant_name}?_get_data=true"
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
client.tenants.get('<tenant_name>', _get_data=True)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/<tenant_name>?_get_data=true'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
)
response.json()
```

> Response Example - Get user and user group counts

```json
{
  "name": "<tenant_name>",
  "groups": {},
  "users": {
    "admin": {
      "tenant-role": "user",
      "roles": [
        "user"
      ]
    }
  }
}
```

`GET "{manager_ip}/api/v3.1/tenants?name={tenant_name}"`

Retrieves a specific tenant.

### URI Parameters
* `tenant_name`: The name of the tenant to retrieve.

### Response
A `Tenant` resource.




## Create Tenant

> Request Example - Get user and user group counts

```shell
$ curl -X POST \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/tenants/<new_tenant_name>"
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
client.tenants.create('<new_tenant_name>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/<new_tenant_name>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.post(
    url,
    auth=auth,
    headers=headers,
)
response.json()
```

> Response Example - Get user and user group counts

```json
{
    "name": "<new_tenant_name>",
    "groups": 0,
    "users": 0
}
```

> Request Example - Get user and user group details


```shell
$ curl -X POST \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/tenants/<new_tenant_name>?_get_data=true"
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
client.tenants.create('<new_tenant_name>', _get_data=True)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/<new_tenant_name>?_get_data=true'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.post(
    url,
    auth=auth,
    headers=headers,
)
response.json()
```

> Response Example - Get user and user group details

```json
{
    "name": "<new_tenant_name>",
    "groups": {},
    "users": {}
}
```
`POST "{manager_ip}/api/v3.1/tenants/{new_tenant_name}"`

Creates a tenant.

### URI Parameters
* `new_tenant_name`: The name of the tenant to create.

### Response
A `Tenant` resource.





## Delete Tenant

> Request Example - Get user and user group counts

```shell
$ curl -X DELETE \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/tenants/<tenant_name_to_delete>"
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
client.tenants.delete('<tenant_name_to_delete>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/<tenant_name-to-delete>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.delete(
    url,
    auth=auth,
    headers=headers,
)
response.json()

```

> Response Example - Get user and user group counts

```json
{
    "name": "tenant_name_to_delete",
    "groups": 0,
    "users": 0
}
```

> Request Example - Get user and user group details

```shell
$ curl -X DELETE \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/tenants/<tenant_name_to_delete>?_get_data=true"
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
client.tenants.delete('<tenant_name_to_delete>', _get_data=True)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/<tenant_name_to_delete>?_get_data=true'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.delete(
    url,
    auth=auth,
    headers=headers,
)
response.json()

```

> Response Example - Get user and user group details

```json
{
    "name": "tenant_name_to_delete",
    "groups": {},
    "users": {}
}
```
`DELETE "{manager_ip}/api/v3.1/tenants/{tenant_name_to_delete}"`

Delete a tenant.

### URI Parameters
* `tenant_name_to_delete`: The name of the tenant to delete.

### Response
A `Tenant` resource.





## Add User to Tenant

> Request Example - Get user and user group counts

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"username": "<username_to_add>", "tenant_name": "<tenant_name>", "role": "<role_name>"}' \
    "http://<manager_ip>/api/v3.1/tenants/users"
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
client.tenants.add_user(
    '<username_to_add>',
    '<tenant_name>',
    '<role_name>',
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/users'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'tenant_name': '<tenant_name>',
    'username': '<username_to_add>',
    'role': '<role_name>',
}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example - Get user and user group counts

```json
{
    "name": "<tenant_name>",
    "groups": 0,
    "users": 1
}
```

> Request Example - Get user and user group details

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"username": <username_to_add>, "tenant_name": <tenant_name>, "role": <role_name>}' \
    "http://<manager_ip>/api/v3.1/tenants/users?_get_data=true"
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
client.tenants.add_user(
    '<username_to_add>',
    '<tenant_name>',
    '<role_name>',
    _get_data=True,
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/users?_get_data=true'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'tenant_name': '<tenant_name>',
    'username': '<username_to_add>',
    'role': '<role_name>',
}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
    json=payload,
    _get_data=True,
)
response.json()
```

> Response Example - Get user and user group details

```json
{
  "name": "<tenant_name>",
  "groups": {},
  "users": {
    "<username_to_add>": {
      "tenant-role": "<role_name>",
      "roles": [
        "<role_name>"
      ]
    }
  }
}
```

`PUT "{manager_ip}/api/v3.1/tenants/users"`

Add a user to a tenant.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username_to_add` | string | The user name to add to the tenant.
`tenant_name` | string | The name of the tenant to which to add the user.
`role_name` | string | (Optional) The name of the role assigned to the user in the tenant. If not passed the default tenant role will be used.

### Response
A `Tenant` resource.


## Update User in Tenant


> Request Example - Get user and user group counts

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json"
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"username": "<username_to_update>", "tenant_name": "<tenant_name>", "role": "<role_name>"}' \
     "http://<manager_ip>/api/v3.1/tenants/users"
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
client.tenants.update_user(
    '<username_to_update>',
    '<tenant_name>',
    '<role_name>',
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/users'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'tenant_name': '<tenant_name>',
    'username': '<username_to_update>',
    'role': '<role_name>',
}
response = requests.patch(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example - Get user and user group counts

```json
{
    "name": "tenant_name",
    "groups": 0,
    "users": 1
}
```

> Request Example - Get user and user group details

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json"
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"username": <username_to_update>, "tenant_name": <tenant_name>, "role": <role_name>}' \
     "http://<manager_ip>/api/v3.1/tenants/users?_get_data=true"
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
client.tenants.update_user(
    '<username_to_update>',
    '<tenant_name>',
    '<role_name>',
    _get_data=True,
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/users?_get_data=true'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'tenant_name': '<tenant_name>',
    'username': '<username_to_update>',
    'role': '<role_name>',
}
response = requests.patch(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example - Get user and user group details

```json
{
  "name": "<tenant_name>",
  "groups": {},
  "users": {
    "my-user": {
      "tenant-role": "<role_name>",
      "roles": [
        "<role_name>"
      ]
    }
  }
}
```
`PATCH "{manager_ip}/api/v3.1/tenants/users"`

Update a user in a tenant.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username_to_update` | string | The user name to remove from the tenant.
`tenant_name` | string | The tenant name to add the user into it.
`role_name` | string | The name of the role assigned to the user in the tenant. If not passed the default tenant role will be used.

### Response
A `Tenant` resource.


## Remove User from Tenant

> Request Example - Get user and user group counts

```shell
$ curl -X DELETE \
    -H "Content-Type: application/json"
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"username": "<username_to_remove>", "tenant_name": "<tenant_name>"}' \
     "http://<manager_ip>/api/v3.1/tenants/users"
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
client.tenants.remove_user('<username_to_remove>', '<tenant_name>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/users'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'tenant_name': '<tenant_name>',
    'username': '<username_to_remove>',
}
response = requests.delete(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example - Get user and user group counts

```json
{
    "name": "tenant_name",
    "groups": 0,
    "users": 0
}
```

> Request Example - Get user and user group details

```shell
$ curl -X DELETE \
    -H "Content-Type: application/json"
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"username": "<username_to_remove>", "tenant_name": "<tenant_name>"}' \
     "http://<manager_ip>/api/v3.1/tenants/users?_get_data=true"
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
client.tenants.remove_user(
    '<username_to_remove>',
    '<tenant_name>',
    _get_data=True,
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/users?_get_data=true'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'tenant_name': '<tenant_name>',
    'username': '<username_to_remove>',
}
response = requests.delete(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example - Get user and user group details

```json
{
    "name": "<tenant_name>",
    "groups": {},
    "users": {}
}
```
`DELETE "{manager_ip}/api/v3.1/tenants/users"`

Delete a user from a tenant.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username_to_remove` | string | The user name to remove from the tenant.
`tenant_name` | string | The tenant name to add the user into it.

### Response
A `Tenant` resource.





## Add User-Group to Tenant

> Request Example - Get user and user group counts

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"group_name": "<group_name>", "tenant_name": "<tenant_name>", "role": "<role_name>"}' \
    "http://<manager_ip>/api/v3.1/tenants/user-groups"
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
client.tenants.add_user_group(
    '<group_name>',
    '<tenant_name>',
    '<role_name>',
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/user-groups'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'tenant_name': '<tenant_name>',
    'group_name': '<group_name>',
    'role': '<role_name>',
}
response = requests.put(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example - Get user and user group counts

```json
{
    "name": "tenant_name",
    "groups": 1,
    "users": 0
}
```

> Request Example - Get user and user group details

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"group_name": "<group_name>", "tenant_name": "<tenant_name>", "role": "<role_name>"}' \
    "http://<manager_ip>/api/v3.1/tenants/user-groups?_get_data=true"
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
client.tenants.add_user_group(
    '<group_name>',
    '<tenant_name>',
    '<role_name>',
    _get_data=True,
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/user-groups?_get_data=true'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'tenant_name': '<tenant_name>',
    'group_name': '<group_name>',
    'role': '<role_name>',
}
response = requests.put(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example - Get user and user group details

```json
{
  "name": "<tenant_name>",
  "groups": {
    "<group_name>": "<role_name>"
  },
  "users": {}
}
```

`PUT "{manager_ip}/api/v3.1/tenants/user-groups"`

Add a user group to a tenant.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`group_name` | string | The name of the user group to add to the tenant.
`tenant_name` | string | The name of the tenant to which to add the user group.
`role` | string | (Optional) The name of the role assigned to the users members of the group. If not passed the default tenant role will be used.

### Response
A `Tenant` resource.


## Update User-Group in Tenant


> Request Example - Get user and user group counts

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json"
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"tenant_name": "<tenant_name>", "group_name": "<group_name>", "role": "<role_name>"}' \
     "http://<manager_ip>/api/v3.1/tenants/user-groups"
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
client.tenants.update_user_group(
    '<group_name>',
    '<tenant_name>',
    '<role_name>',
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/user-groups'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'tenant_name': '<tenant_name>',
    'group_name': '<group_name>',
    'role': '<role_name>',
}
response = requests.patch(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example - Get user and user group counts

```json
{
    "name": "tenant_name",
    "groups": 1,
    "users": 0
}
```

> Request Example - Get user and user group details

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json"
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"tenant_name": "<tenant_name>", "group_name": "<group_name>", "role": "<role_name>"}' \
     "http://<manager_ip>/api/v3.1/tenants/user-groups?_get_data=true"
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
client.tenants.update_user_group(
    '<group_name>',
    '<tenant_name>',
    '<role_name>',
    _get_data=True,
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/user-groups?_get_data=true'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'tenant_name': '<tenant_name>',
    'group_name': '<group_name>',
    'role': '<role_name>',
}
response = requests.patch(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example - Get user and user group details

```json
{
  "name": "<tenant_name>",
  "groups": {
    "<group_name>": "<role_name>"
  },
  "users": {}
}
```

`PATCH "{manager_ip}/api/v3.1/tenants/user-groups"`

Update a user group in a tenant.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`group_name` | string | The group name to update in the tenant.
`tenant_name` | string | The tenant name to which the user group is assigned.
`role_name` | string | The name of the role assigned to the user in the tenant. If not passed the default tenant role will be used.

### Response
A `Tenant` resource.


## Remove User-Group from Tenant

> Request Example - Get user and user group counts

```shell
$ curl -X DELETE \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"group_name": "<group_name>", "tenant_name": "<tenant_name>"}' \
    "http://<manager_ip>/api/v3.1/tenants/user-groups"
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
client.tenants.remove_user_group('<group_name>', '<tenant_name>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/user-groups'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'tenant_name': '<tenant_name>',
    'group_name': '<group_name>',
}
response = requests.delete(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example - Get user and user group counts

```json
{
    "name": "tenant_name",
    "groups": 0,
    "users": 0
}
```

> Request Example - Get user and user group details

```shell
$ curl -X DELETE \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"group_name": "<group_name>", "tenant_name": "<tenant_name>"}' \
    "http://<manager_ip>/api/v3.1/tenants/user-groups?_get_data=true"
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
client.tenants.remove_user_group(
    '<group_name>',
    '<tenant_name>',
    _get_data=True,
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/tenants/user-groups?_get_data=true'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'tenant_name': '<tenant_name>',
    'group_name': '<group_name>',
}
response = requests.delete(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example - Get user and user group details

```json
{
    "name": "tenant_name",
    "groups": {},
    "users": {}
}
```
`DELETE "{manager_ip}/api/v3.1/tenants/user-groups"`

Delete a user group from a tenant.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`group_name` | string | The name of the user group to delete from the tenant.
`tenant_name` | string | The name of the tenant from which to delete the user group.

### Response
A `Tenant` resource.

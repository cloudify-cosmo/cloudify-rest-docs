# Tenants

## The Tenant Resource

<aside class="notice">
This section describes API features that are part of the Cloudify premium edition
</aside>

> `Note`

```python
# Include this code when using the Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
        host='<manager-ip>',
        username='<manager-username>',
        password='<manager-password>',
        tenant='<manager-tenant>')

# Include this code when using python requests
import requests
from requests.auth import HTTPBasicAuth

headers = {'Tenant': '<tenant-name>'}
auth = HTTPBasicAuth(<user>, <password>)
```

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
    -H "Tenant: default_tenant" \
    -u <user>:<password> \
    "http://<manager-ip>/api/v3.1/tenants"
```

```python
# Using Cloudify client
client.tenants.list()

# Using requests
url = 'http://<manager-ip>/api/v3.1/tenants'
response = requests.get(url, auth=auth, headers=headers)
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
    -H "Tenant: default_tenant" \
    -u <user>:<password> \
    "http://<manager-ip>/api/v3.1/tenants?_get_data=true"
```

```python
# Using Cloudify client
client.tenants.list(_get_data=True)

# Using requests
url = 'http://<manager-ip>/api/v3.1/tenants?_get_data=true'
response = requests.get(url, auth=auth, headers=headers)
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

`GET "{manager-ip}/api/v3.1/tenants"`

List all tenants.


### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Tenant` resources.

## Get Tenant

> Request Example - Get user and user group counts

```shell
$ curl -X GET \
    -H "Tenant: default_tenant" \
    -u <user>:<password> \
    "http://<manager-ip>/api/v3.1/tenants/{tenant-name}"
```

```python
# Using Cloudify client
client.tenants.get('default_tenant')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager-ip>/api/v3.1/tenants/<tenant-name>'
response = requests.get(url, auth=auth, headers=headers)
response.json()
```

> Response Example - Get user and user group counts

```json
{
    "name": "default_tenant",
    "groups": 0,
    "users": 1
}
```

> Request Example - Get user and user group details

```shell
$ curl -X GET \
    -H "Tenant: default_tenant" \
    -u <user>:<password> \
    "http://<manager-ip>/api/v3.1/tenants/{tenant-name}?_get_data=true"
```

```python
# Using Cloudify client
client.tenants.get('default_tenant', _get_data=True)

# Using requests
url = 'http://<manager-ip>/api/v3.1/tenants/<tenant-name>?_get_data=true'
response = requests.get(url, auth=auth, headers=headers)
response.json()
```

> Response Example - Get user and user group counts

```json
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
```

`GET "{manager-ip}/api/v3.1/tenants?name={tenant-name}"`

Retrieves a specific tenant.

### URI Parameters
* `tenant-name`: The name of the tenant to retrieve.

### Response
A `Tenant` resource.




## Create Tenant

> Request Example - Get user and user group counts

```shell
$ curl -X POST \
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    "http://<manager-ip>/api/v3.1/tenants/<new-tenant-name>"
```

```python
# Using Cloudify client
client.tenants.create(<new-tenant-name>)

# Using requests
url = 'http://<manager-ip>/api/v3.1/tenants/<new-tenant-name>'
response = requests.post(url, auth=auth, headers=headers)
response.json()
```

> Response Example - Get user and user group counts

```json
{
    "name": "<new-tenant-name>",
    "groups": 0,
    "users": 0
}
```

> Request Example - Get user and user group details


```shell
$ curl -X POST \
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    "http://<manager-ip>/api/v3.1/tenants/<new-tenant-name>?_get_data=true"
```

```python
# Using Cloudify client
client.tenants.create(<new-tenant-name>, _get_data=True)

# Using requests
url = 'http://<manager-ip>/api/v3.1/tenants/<new-tenant-name>?_get_data=true'
response = requests.post(url, auth=auth, headers=headers)
response.json()
```

> Response Example - Get user and user group details

```json
{
    "name": "<new-tenant-name>",
    "groups": {},
    "users": {}
}
```
`POST "{manager-ip}/api/v3.1/tenants/{new-tenant-name}"`

Creates a tenant.

### URI Parameters
* `new-tenant-name`: The name of the tenant to create.

### Response
A `Tenant` resource.





## Delete Tenant

> Request Example - Get user and user group counts

```shell
$ curl -X DELETE \
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    "http://<manager-ip>/api/v3.1/tenants/<tenant-name-to-delete>"
```

```python
# Using Cloudify client
client.tenants.delete(<tenant-name-to-delete>)

# Using requests
url = 'http://<manager-ip>/api/v3.1/tenants/<tenant-name-to-delete>'
response = requests.delete(url, auth=auth, headers=headers)
response.json()

```

> Response Example - Get user and user group counts

```json
{
    "name": "tenant-name-to-delete",
    "groups": 0,
    "users": 0
}
```

> Request Example - Get user and user group details

```shell
$ curl -X DELETE \
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    "http://<manager-ip>/api/v3.1/tenants/<tenant-name-to-delete>?_get_data=true"
```

```python
# Using Cloudify client
client.tenants.delete(<tenant-name-to-delete>, _get_data=True)

# Using requests
url = 'http://<manager-ip>/api/v3.1/tenants/<tenant-name-to-delete>?_get_data=true'
response = requests.delete(url, auth=auth, headers=headers)
response.json()

```

> Response Example - Get user and user group details

```json
{
    "name": "tenant-name-to-delete",
    "groups": {},
    "users": {}
}
```
`DELETE "{manager-ip}/api/v3.1/tenants/{tenant-name-to-delete}"`

Delete a tenant.

### URI Parameters
* `tenant-name-to-delete`: The name of the tenant to delete.

### Response
A `Tenant` resource.





## Add User to Tenant

> Request Example - Get user and user group counts

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    -d '{"username": <user-name>, "tenant_name": <tenant-name>, "role": <role_name>}' \
    "http://<manager-ip>/api/v3.1/tenants/users"
```

```python
# Using Cloudify client
client.tenants.add_user(<user-name>, <tenant-name>, <role>)

# Using requests
url = 'http://<manager-ip>/api/v3.1/tenants/users'
payload = {
    'tenant_name': <tenant-name>,
    'username': <user>,
    'role': <role_name>,
}
response = requests.get(url, auth=auth, headers=headers, json=payload)
response.json()
```

> Response Example - Get user and user group counts

```json
{
    "name": "<tenant-name>",
    "groups": 0,
    "users": 1
}
```

> Request Example - Get user and user group details

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    -d '{"username": <user-name>, "tenant_name": <tenant-name>, "role": <role_name>}' \
    "http://<manager-ip>/api/v3.1/tenants/users?_get_data=true"
```

```python
# Using Cloudify client
client.tenants.add_user(<user-name>, <tenant-name>, <role>)

# Using requests
url = 'http://<manager-ip>/api/v3.1/tenants/users?_get_data=true'
payload = {
    'tenant_name': <tenant-name>,
    'username': <user>,
    'role': <role_name>,
}
response = requests.get(url, auth=auth, headers=headers, json=payload, _get_data=True)
response.json()
```

> Response Example - Get user and user group details

```json
{
  "name": "<tenant-name>",
  "groups": {},
  "users": {
    "my-user": {
      "tenant-role": "<role>",
      "roles": [
        "<role>"
      ]
    }
  }
}
```

`PUT "{manager-ip}/api/v3.1/tenants/users"`

Add a user to a tenant.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username` | string | The user name to add to the tenant.
`tenant_name` | string | The name of the tenant to which to add the user.
`role_name` | string | (Optional) The name of the role assigned to the user in the tenant. If not passed the default tenant role will be used.

### Response
A `Tenant` resource.


## Update User in Tenant


> Request Example - Get user and user group counts

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json"
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    -d '{"username": <user-name>, "tenant_name": <tenant-name>, "role": <role_name>}' \
     "http://<manager-ip>/api/v3.1/tenants/users"
```

```python
# Using Cloudify client
client.tenants.update_user(<user-name>, <tenant-name>, <role_name>)

# Using requests
url = 'http://<manager-ip>/api/v3.1/tenants/users'
payload = {
    'tenant_name': <tenant-name>,
    'username': <user>,
    'role': <role_name>,
}
response = requests.patch(url, auth=auth, headers=headers, json=payload)
response.json()
```

> Response Example - Get user and user group counts

```json
{
    "name": "tenant-name",
    "groups": 0,
    "users": 1
}
```

> Request Example - Get user and user group details

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json"
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    -d '{"username": <user-name>, "tenant_name": <tenant-name>, "role": <role_name>}' \
     "http://<manager-ip>/api/v3.1/tenants/users?_get_data=true"
```

```python
# Using Cloudify client
client.tenants.update_user(<user-name>, <tenant-name>, <role_name>, _get_data=True)

# Using requests
url = 'http://<manager-ip>/api/v3.1/tenants/users?_get_data=true'
payload = {
    'tenant_name': <tenant-name>,
    'username': <user>,
    'role': <role_name>,
}
response = requests.patch(url, auth=auth, headers=headers, json=payload)
response.json()
```

> Response Example - Get user and user group details

```json
{
  "name": "<tenant-name>",
  "groups": {},
  "users": {
    "my-user": {
      "tenant-role": "<role>",
      "roles": [
        "<role>"
      ]
    }
  }
}
```
`PATCH "{manager-ip}/api/v3.1/tenants/users"`

Update a user in a tenant.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username` | string | The user name to remove from the tenant.
`tenant_name` | string | The tenant name to add the user into it.
`role_name` | string | The name of the role assigned to the user in the tenant. If not passed the default tenant role will be used.

### Response
A `Tenant` resource.


## Remove User from Tenant

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
# Using Cloudify client
client.tenants.remove_user(<user-name>, <tenant-name>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager-ip>/api/v3.1/tenants/users'
headers = {'Tenant': '<tenant-name>'}
payload = {
    'tenant_name': <tenant-name>,
    'username': <user>,
}
response = requests.delete(
    url,
    auth=HTTPBasicAuth(<user>, <password>),
    headers=headers,
    json=payload,
)
response.json()
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
# Using Cloudify client
client.tenants.add_user_group(<group-name>, <tenant-name>, <role>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager-ip>/api/v3.1/tenants/user-groups'
headers = {'Tenant': '<tenant-name>'}
payload = {
    'tenant_name': <tenant-name>,
    'group_name': <user>,
    'role': <role_name>,
}
response = requests.put(
    url,
    auth=HTTPBasicAuth(<user>, <password>),
    headers=headers,
    json=payload,
)
response.json()
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


## Update User-Group in Tenant


> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json"
    -H "Tenant: <tenant-name>" \
    -u <user>:<password> \
    -d '{"username": <user-name>, "group_name": <group-name>, "role": <role-name>}' \
     "http://<manager-ip>/api/v3.1/tenants/user-groups"
```

```python
# Using Cloudify client
client.tenants.update_user_group(<group-name>, <tenant-name>, <role-name>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager-ip>/api/v3.1/tenants/user-groups'
headers = {'Tenant': '<tenant-name>'}
payload = {
    'tenant_name': <tenant-name>,
    'group_name': <group-name>,
    'role': <role-name>,
}
response = requests.patch(
    url,
    auth=HTTPBasicAuth(<user>, <password>),
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example

```json
{
    "name": "tenant-name",
    "groups": 0,
    "users": 1
}
```

`PATCH "{manager-ip}/api/v3.1/tenants/user-groups"`

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
# Using Cloudify client
client.tenants.remove_user_group(<group-name>, <tenant-name>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager-ip>/api/v3.1/tenants/user-groups'
headers = {'Tenant': '<tenant-name>'}
payload = {
    'tenant_name': <tenant-name>,
    'group_name': <user>,
}
response = requests.delete(
    url,
    auth=HTTPBasicAuth(<user>, <password>),
    headers=headers,
    json=payload,
)
response.json()
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

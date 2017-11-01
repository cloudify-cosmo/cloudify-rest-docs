# User Groups

## The User Group Resource

<aside class="notice">
This section describes API features that are part of the Cloudify premium edition
</aside>

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
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
)
client.user_groups.list()

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/user-groups'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
)
```

> Response Example

```json
{
  "items": [
    {
      "ldap_dn": "ldap_group_dn",
      "tenants": 0,
      "name": "group_name",
      "users": 0
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

`GET "{manager_ip}/api/v3.1/user-groups"`

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
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
)
client.user_groups.get('<group_name>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/user-groups/<group_name>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
)
```

> Response Example

```json
{
  "ldap_dn": "ldap_group_dn",
  "tenants": 0,
  "name": "<group_name>",
  "users": 0
}
```

`GET "{manager_ip}/api/v3.1/user-groups/{group_name}"`

Retrieves a specific group.

### URI Parameters
* `group_name`: The name of the group to retrieve.

### Response
A `Group` resource.


## Create User Group

> Request Example

```shell
$ curl -X POST \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"group_name": <group_name>, "ldap_group_dn": <ldap_group_dn>}' \
    "http://<manager_ip>/api/v3.1/user-groups"
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
client.user_groups.create(
    group_name='<group_name>',
    ldap_group_dn='<ldap_group_dn>',
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/user-groups'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'group_name': '<group_name>',
    'ldap_group_dn': '<ldap_group_dn>',
}
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
  "ldap_dn": "<ldap_group_dn>",
  "tenants": 0,
  "name": "<group_name>",
  "users": 0
}
```

`POST -d '{"group_name": <group-name>, "ldap_group_dn": <ldap_group_dn>}' "{manager-ip}/api/v3.1/user-groups"`

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
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
)
client.user_groups.delete('<user_group_name_to_delete>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/user-groups/<user_group_name_to_delete>'
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
    "ldap_dn": "ldap_group_dn",
    "name": "<user_group_name_to_delete>",
    "tenants": 0,
    "users": 0
}
```

`DELETE "{manager_ip}/api/v3.1/user-groups/{user_group_name_to_delete}"`

Deletes a user group.

### URI Parameters
* `user_group_name_to_delete`: The name of the user group to delete.

### Response
A `Group` resource.





## Add User to Group

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"username": <username_to_add>, "group_name": <group_name>}' \
    "http://<manager_ip>/api/v3.1/user-groups/users"
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
client.user_groups.add_user('<username_to_add>', '<group_name>')
```

> Response Example

```json
{
  "ldap_dn": "ldap_group_dn",
  "tenants": 0,
  "name": "<group_name>",
  "users": 1
}
```

`PUT "{manager_ip}/api/v3.1/user-groups/users"`

Add a user to group.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username_to_add` | string | The name of the user to add to the group.
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
    -d '{"username": <username_to_remove>, "group_name": <group_name>}' \
    "http://<manager_ip>/api/v3.1/user-groups/users"
```

```python
# Python Client-
client.user_groups.remove_user(<username_to_remove>, <group_name>)
```

> Response Example

```json
{
  "ldap_dn": "ldap_group_dn",
  "tenants": 0,
  "name": "<group_name>",
  "users": 0
}
```

`DELETE "{manager-ip}/api/v3.1/user-groups/users"`

Delete a user from a group.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`username_to_remove` | string | The name of the user to remove from the group.
`group_name` | string | The name of the group from which to remove the user.

### Response
A `Group` resource.

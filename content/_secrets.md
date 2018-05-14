# Secrets

## The Secret Resource


A Secret resource is a key-value pair saved per tenant.
A user can ensure all secrets (such as credentials to IaaS environments, passwords, etc) are kept in a secured manner,
and adhere to isolation requirements between different tenants.



### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`created_at` | datetime | The time when the secret was created.
`key` | string | The secret's key, unique per tenant.
`updated_at` | datetime | The time the secret was last updated at.
`value` | string | The secret's value.
`visibility` | string | Defines who can see the secret. Can be private, tenant or global. **Supported for Cloudify Manager 4.3 and above.**
`is_hidden_value` | boolean| Determines who can see the value of the secret. If True, the value of the secret is only shown to the user that created the secret and to admins. (default: false). **Supported for Cloudify Manager 4.4 and above.**

## List Secrets

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/secrets"
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
client.secrets.list()

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/secrets'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
)
response.json()
```

> Response Example

```json
{
    "items": [
        {
            "created_at": "2017-11-24T10:42:29.756Z",
            "created_by": "admin",
            "key": "<secret_key>",
            "visibility": "tenant",
            "tenant_name": "default_tenant",
            "updated_at": "2017-11-24T10:42:29.756Z",
            "is_hidden_value": false
        }
    ],
    "metadata": {
        "pagination": {
            "offset": 0,
            "size": 0,
            "total": 1
        }
    }
}
```

`GET "{manager_ip}/api/v3.1/secrets"`

List all secrets.

### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Secret` resources without the secret's value.



## Get Secret

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/secrets/<secret_key>"
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
client.secrets.get(<secret_key>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/secrets/<secret_key>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
)
response.json()
```

> Response Example

```json
{
    "created_at": "2017-11-24T10:42:29.756Z",
    "created_by": "admin",
    "key": "<secret_key>",
    "private_resource": false,
    "visibility": "tenant",
    "tenant_name": "default_tenant",
    "updated_at": "2017-11-24T10:42:29.756Z",
    "value": "<secret_value>",
    "is_hidden_value": false
}
```

`GET "{manager_ip}/api/v3.1/secrets/{secret_key}"`

Retrieves a specific secret.

### URI Parameters
* `secret_key`: The key of the secret to retrieve.

### Response
A `Secret` resource.



## Create Secret

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"value": <new_secret_value>, "update_if_exists": false, "visibility": "<visibility>", "is_hidden_value": false}' \
    "http://<manager_ip>/api/v3.1/secrets/<new_secret_key>"
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
client.secrets.create(
    <new_secret_key>,
    <new_secret_value>,
    update_if_exists=False,
    visibility='<visibility>',
    is_hidden_value=False
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/secrets/<new_secret_key>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'value': '<new_secret_value>',
    'update_if_exists': False,
    'visibility': '<visibility>',
    'is_hidden_value': False
}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example

```json
{
    "created_at": "2017-11-24T10:42:29.756Z",
    "created_by": "admin",
    "key": "<new_secret_key>",
    "private_resource": false,
    "visibility": "tenant",
    "tenant_name": "default_tenant",
    "updated_at": "2017-11-24T10:42:29.756Z",
    "value": "<new_secret_value>",
    "is_hidden_value": false
}
```

`PUT -d '{"value": <new_secret_value>}' "{manager_ip}/api/v3.1/secrets/{new_secret_key}"`

Creates a secret.

### URI Parameters
* `new_secret_key`: The key of the secret to create.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`value` | string | The secret's value.
`update_if_exists` | boolean | Update value if secret already exists (optional, defaults to false).
`visibility` | string | Optional parameter, defines who can see the secret (default: tenant). **Supported for Cloudify Manager 4.3 and above.**
`is_hidden_value` | boolean| Optional parameter, determines who can see the value of the secret. If True, the value of the secret is only shown to the user that created the secret and to admins. (default: false). **Supported for Cloudify Manager 4.4 and above.**

Valid visibility values are:

* `private`: The resource is visible to the user that created the resource, the tenant’s managers and the system’s admins.
* `tenant`: The resource is visible to all users in the current tenant. (Default value)
* `global`: The resource is visible to all users in all tenants across the manager.

### Response
A `Secret` resource.



## Update Secret

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"value": <new_secret_value>, "visibility": "<visibility>", "is_hidden_value": false}' \
    "http://<manager_ip>/api/v3.1/secrets/<secret_key>"
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
client.secrets.update(<secret_key>, <new_secret_value>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/secrets/<secret_key>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {'value': '<new_secret_value>'}
response = requests.patch(
    url,
    auth=auth,
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example

```json
{
    "created_at": "2017-11-24T11:01:05.357Z",
    "created_by": "admin",
    "key": "<secret_key>",
    "private_resource": false,
    "visibility": "tenant",
    "tenant_name": "default_tenant",
    "updated_at": "2017-11-24T12:02:38.296Z",
    "value": "<new_secret_value>",
    "is_hidden_value": false
}
```

`PATCH -d '{"value": <new_secret_value>, "visibility": <visibility>, "is_hidden_value": <is_hidden_value>}' "{manager_ip}/api/v3.1/secrets/{secret_key}"`

Updates a secret.

### URI Parameters
* `secret_key`: The key of the secret to update.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`value` | string | The secret's new value.
`visibility` | string | Optional parameter, defines who can see the secret (default: tenant). **Supported for Cloudify Manager 4.3 and above.**
`is_hidden_value` | boolean| Optional parameter, determines who can see the value of the secret. If True, the value of the secret is only shown to the user that created the secret and to admins. (default: false). **Supported for Cloudify Manager 4.4 and above.**

### Response
A `Secret` resource.



## Delete Secret

> Request Example

```shell
$ curl -X DELETE \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/secrets/<secret_key>"
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
client.secrets.delete(<secret_key>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/secrets/<secret_key>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.delete(
    url,
    auth=auth,
    headers=headers,
)
response.json()
```

> Response Example

```json
{
    "created_at": "2017-11-24T11:01:05.357Z",
    "created_by": "admin",
    "key": "<secret_key>",
    "private_resource": false,
    "visibility": "tenant",
    "tenant_name": "default_tenant",
    "updated_at": "2017-11-24T12:05:30.190Z",
    "value": "<secret_value>",
    "is_hidden_value": false
}
```

`DELETE "{manager_ip}/api/v3.1/secrets/{secret_key}"`

Deletes a secret.

### URI Parameters
* `secret_key`: The key of the secret to delete.

### Response
A `Secret` resource.



## Set Global Secret

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/secrets/<secret_key>/set-global"
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
client.secrets.set_global(<secret_key>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/secrets/<secret_key>/set-global'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.patch(
    url,
    auth=auth,
    headers=headers,
)
response.json()
```

> Response Example

```json
{
    "created_at": "2017-11-24T12:10:49.789Z",
    "created_by": "admin",
    "key": "<secret_key>",
    "private_resource": false,
    "visibility": "global",
    "tenant_name": "default_tenant",
    "updated_at": "2017-11-24T12:11:16.495Z",
    "value": "<secret_value>",
    "is_hidden_value": false
}
```

`PATCH "{manager_ip}/api/v3.1/secrets/{secret_key}/set-global"`

Set the secret's visibility to global.
Will be deprecated soon. For Cloudify Manager 4.3 and above, use 'set-visibility'.

### URI Parameters
* `secret_key`: The key of the secret to update.


### Response
A `Secret` resource.



## Set Secret Visibility

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"visibility": "<visibility>"}' \
    "http://<manager-ip>/api/v3.1/secrets/<secret-key>/set-visibility"
```

```python
# Python Client
client.secrets.set_visibility('<secret-key>', '<visibility>')
```

> Response Example

```json
{
    "created_at": "2017-11-24T12:10:49.789Z",
    "created_by": "admin",
    "key": "<secret-key>",
    "private_resource": false,
    "visibility": "global",
    "tenant_name": "default_tenant",
    "updated_at": "2017-11-24T12:11:16.495Z",
    "value": "<secret-value>",
    "is_hidden_value": false
}
```

`PATCH "<manager-ip>/api/v3.1/secrets/{secret-key}/set-visibility"`

Update the visibility of the secret. **Supported for Cloudify Manager 4.3 and above.**

### URI Parameters
* `secret-key`: The key of the secret to update.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`visibility` | string | Defines who can see the secret. (Required)

Valid values are `tenant` or `global`.

### Response
A `Secret` resource.

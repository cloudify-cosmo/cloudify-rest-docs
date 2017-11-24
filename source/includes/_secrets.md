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
`resource_availability` | string | The availability of the resource.
                                   Can be private, tenant or global.

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

# Using request
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
            "resource_availability": "tenant",
            "tenant_name": "default_tenant",
            "updated_at": "2017-11-24T10:42:29.756Z"
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
    "resource_availability": "tenant",
    "tenant_name": "default_tenant",
    "updated_at": "2017-11-24T10:42:29.756Z",
    "value": "<secret_value>"
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
    -d '{"value": <new_secret_value>}' \
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
client.secrets.create(<new_secret_key>, <new_secret_value>)
```

> Response Example

```json
{
    "key": "key1",
    "value": "value1",
    "created_at": "2017-03-20T08:23:31.276Z",
    "updated_at": "2017-03-20T08:23:31.276Z",
    "permission": "creator",
    "tenant_name": "default_tenant",
    "created_by": "admin",
    "resource_availability": "tenant"
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

### Response
A `Secret` resource.



## Update Secret

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"value": <new_secret_value>}' \
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
```

> Response Example

```json
{
    "key": "key1",
    "value": "value1",
    "created_at": "2017-03-20T08:23:31.276Z",
    "updated_at": "2017-03-20T08:43:19.468Z",
    "permission": "creator",
    "tenant_name": "default_tenant",
    "created_by": "admin",
    "resource_availability": "tenant"
}
```

`PATCH -d '{"value": <new_secret_value>}' "{manager_ip}/api/v3.1/secrets/{secret_key}"`

Updates a secret.

### URI Parameters
* `secret_key`: The key of the secret to update.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`value` | string | The secret's new value.

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
```

> Response Example

```json
{
    "key": "key1",
    "value": "value1",
    "created_at": "2017-03-20T08:23:31.276Z",
    "updated_at": "2017-03-20T08:43:19.468Z",
    "permission": "creator",
    "tenant_name": "default_tenant",
    "created_by": "admin",
    "resource_availability": "tenant"
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
```

> Response Example

```json
{
    "key": "key1",
    "value": "value1",
    "created_at": "2017-03-20T08:23:31.276Z",
    "updated_at": "2017-03-20T08:43:19.468Z",
    "permission": "creator",
    "tenant_name": "default_tenant",
    "created_by": "admin",
    "resource_availability": "global"
}
```

`PATCH "{manager_ip}/api/v3.1/secrets/{secret_key}/set-global"`

Set the secret's availability to global.

### URI Parameters
* `secret_key`: The key of the secret to update.


### Response
A `Secret` resource.

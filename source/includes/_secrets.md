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
```

> Response Example

```json
{
 "items":
    [
        {
            "key": "key1",
            "created_at": "2017-03-20T08:23:31.276Z",
            "updated_at": "2017-03-20T08:43:19.468Z",
            "permission": "creator",
            "tenant_name": "default_tenant",
            "created_by": "admin",
            "resource_availability": "tenant"
        }
    ]
}
```

`GET "{manager-ip}/api/v3.1/secrets"`

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
    "http://<manager_ip>/api/v3.1/secrets/<secret-key>"
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
client.secrets.get(<secret-key>)
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

`GET "{manager-ip}/api/v3.1/secrets/{secret-key}"`

Retrieves a specific secret.

### URI Parameters
* `secret-key`: The key of the secret to retrieve.

### Response
A `Secret` resource.



## Create Secret

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"value": <new-secret-value>}' \
    "http://<manager-ip>/api/v3.1/secrets/<new-secret-key>"
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
client.secrets.create(<new-secret-key>, <new-secret-value>)
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

`PUT -d '{"value": <new-secret-value>}' "{manager-ip}/api/v3.1/secrets/{new-secret-key}"`

Creates a secret.

### URI Parameters
* `new-secret-key`: The key of the secret to create.

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
    -d '{"value": <new-value>}' \
    "http://<manager_ip>/api/v3.1/secrets/<secret-key>"
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
client.secrets.update(<secret-key>, <new-value>)
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

`PATCH -d '{"value": <new-value>}' "{manager-ip}/api/v3.1/secrets/{secret-key}"`

Updates a secret.

### URI Parameters
* `secret-key`: The key of the secret to update.

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
    "http://<manager_ip>/api/v3.1/secrets/<secret-key>"
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
client.secrets.delete(<secret-key>)
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

`DELETE "{manager-ip}/api/v3.1/secrets/{secret-key}"`

Deletes a secret.

### URI Parameters
* `secret-key`: The key of the secret to delete.

### Response
A `Secret` resource.



## Set Global Secret

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager-ip>/api/v3.1/secrets/<secret-key>/set-global"
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
client.secrets.set_global(<secret-key>)
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

`PATCH "{manager-ip}/api/v3.1/secrets/{secret-key}/set-global"`

Set the secret's availability to global.

### URI Parameters
* `secret-key`: The key of the secret to update.


### Response
A `Secret` resource.

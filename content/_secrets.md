# Secrets

## The Secret Resource

A Secret resource is a key-value pair saved per tenant.
A user can ensure all secrets (such as credentials to IaaS environments, passwords, etc) are kept in a secured manner,
and adhere to isolation requirements between different tenants.

### Attributes:

| Attribute          | Type     | Description                                                                                                                                                                                                           |
|--------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `key`              | string   | The secret's key, unique per tenant.                                                                                                                                                                                  |
| `value`            | string   | The secret's value.                                                                                                                                                                                                   |
| `schema`           | dict     | A JSON schema against which the secret will be validated.                                                                                                                                                             |
| `is_hidden_value`  | boolean  | Determines who can see the value of the secret. If True, the value of the secret is only shown to the user that created the secret and to admins. (default: false). **Supported for Cloudify Manager 4.4 and above.** |
| `visibility`       | string   | Defines who can see the secret. Can be private, tenant or global. **Supported for Cloudify Manager 4.3 and above.**                                                                                                   |
| `tenant_name`      | string   | The name of the tenant of the secret.                                                                                                                                                                                 |
| `provider_name`    | string   | The secret's provider name.                                                                                                                                                                                           |
| `provider_options` | dict     | The secret's provider options.                                                                                                                                                                                        |
| `created_by`       | string   | The author of the secret.                                                                                                                                                                                             |
| `created_at`       | datetime | The time when the secret was created.                                                                                                                                                                                 |
| `updated_at`       | datetime | The time the secret was last updated at.                                                                                                                                                                              |

## List Secrets

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    --cacert <path_to_ca_cert> \
    "https://<manager_ip>/api/v3.1/secrets"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient

client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
    cert='<path_to_ca_cert>',
)
client.secrets.list()

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
    verify='<path_to_ca_cert>',
)
response.json()
```

> Response Example

```json
{
    "metadata": {
        "pagination": {
            "total": 1,
            "size": 1000,
            "offset": 0
        },
        "filtered": null
    },
    "items": [
        {
            "key": "<secret_key>",
            "created_at": "2022-12-20T10:02:06.751Z",
            "updated_at": "2022-12-20T10:02:06.751Z",
            "resource_availability": "tenant",
            "visibility": "tenant",
            "tenant_name": "default_tenant",
            "created_by": "admin",
            "is_hidden_value": false,
            "provider_name": null,
            "provider_options": null
        }
    ]
}
```

`GET "{manager_ip}/api/v3.1/secrets"`

List all secrets.

### Response
| Field      | Type | Description                                              |
|------------|------|----------------------------------------------------------|
| `items`    | list | A list of `Secret` resources without the secret's value. |
| `metadata` | dict | Information about pagination result.                     |

## Get Secret

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    --cacert <path_to_ca_cert> \
    "https://<manager_ip>/api/v3.1/secrets/<secret_key>"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient

client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
    cert='<path_to_ca_cert>',
)
client.secrets.get('<secret_key>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets/<secret_key>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
    verify='<path_to_ca_cert>',
)
response.json()
```

> Response Example

```json
{
    "created_at": "2022-12-20T10:02:06.751Z",
    "visibility": "tenant",
    "value": "<secret_value>",
    "updated_at": "2022-12-20T10:02:06.751Z",
    "is_hidden_value": false,
    "schema": null,
    "provider_options": null,
    "key": "<secret_key>",
    "provider_name": null,
    "tenant_name": "default_tenant",
    "created_by": "admin",
    "resource_availability": "tenant",
    "private_resource": false
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
    --cacert <path_to_ca_cert> \
    -d '{"value": "<secret_value>", "update_if_exists": false, "visibility": "<visibility>", "is_hidden_value": false, "schema": {}, "provider": "<provider_name>", "provider_options": {}}' \
    "https://<manager_ip>/api/v3.1/secrets/<secret_key>"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient

client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
    cert='<path_to_ca_cert>',
)
client.secrets.create(
    '<secret_key>',
    '<secret_value>',
    update_if_exists=False,
    visibility='<visibility>',
    is_hidden_value=False,
    schema={},
    provider='<provider_name>',
    provider_options={},
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets/<secret_key>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'value': '<secret_value>',
    'update_if_exists': False,
    'visibility': '<visibility>',
    'is_hidden_value': False,
    'schema': {},
    'provider': '<provider_name>',
    'provider_options': {},
}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
    verify='<path_to_ca_cert>',
    json=payload,
)
response.json()
```

> Response Example

```json
{
    "created_at": "2022-12-20T11:01:12.406Z",
    "visibility": "tenant",
    "value": "<secret_value_encrypted>",
    "updated_at": "2022-12-20T11:01:12.406Z",
    "is_hidden_value": false,
    "schema": null,
    "provider_options": null,
    "key": "<secret_key>",
    "provider_name": null,
    "tenant_name": "default_tenant",
    "created_by": "admin",
    "resource_availability": "tenant",
    "private_resource": false
}
```

`PUT -d '{"value": "<secret_value>", "update_if_exists": false, "visibility": "<visibility>", "is_hidden_value": false, "schema": {}, "provider": "<provider_name>", "provider_options": {}}'`

Creates a secret.

### URI Parameters
* `new_secret_key`: The key of the secret to create.

### Request Body
| Property           | Type    | Description                                                                                                                                                                                                                               |
|--------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `value`            | string  | The secret's value.                                                                                                                                                                                                                       |
| `update_if_exists` | boolean | Update value if secret already exists (optional, defaults to false).                                                                                                                                                                      |
| `visibility`       | string  | Optional parameter, defines who can see the secret (default: tenant). **Supported for Cloudify Manager 4.3 and above.**                                                                                                                   |
| `is_hidden_value`  | boolean | Optional parameter, determines who can see the value of the secret. If True, the value of the secret is only shown to the user that created the secret and to admins. (default: false). **Supported for Cloudify Manager 4.4 and above.** |
| `schema`           | dict    | Optional parameter, defines how the secret should be validated.                                                                                                                                                                           |
| `provider`         | string  | Optional parameter, defines which provider should be used to get the secret's value.                                                                                                                                                      |
| `provider_options` | dict    | Optional parameter, defines additional options to get the secret's value via provider.                                                                                                                                                    |

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
    --cacert <path_to_ca_cert> \
    -d '{"value": "<secret_value>", "visibility": "<visibility>", "is_hidden_value": false, "creator": "<creator_name>", "provider": "<provider_name>", "provider_options": {}}' \
    "https://<manager_ip>/api/v3.1/secrets/<secret_key>"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient

client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
    cert='<path_to_ca_cert>',
)
client.secrets.update(
    '<secret_key>',
    '<secret_value>',
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets/<secret_key>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {'value': '<secret_value>'}
response = requests.patch(
    url,
    auth=auth,
    headers=headers,
    verify='<path_to_ca_cert>',
    json=payload,
)
response.json()
```

> Response Example

```json
{
    "created_at": "2022-12-20T11:01:12.406Z",
    "visibility": "tenant",
    "value": "<secret_value_encrypted>",
    "updated_at": "2022-12-20T11:38:08.072Z",
    "is_hidden_value": false,
    "schema": null,
    "provider_options": null,
    "key": "<secret_key>",
    "provider_name": null,
    "tenant_name": "default_tenant",
    "created_by": "admin",
    "resource_availability": "tenant",
    "private_resource": false
}
```

`PATCH -d '{"value": "<secret_value>", "visibility": "<visibility>", "is_hidden_value": false, "creator": "<creator_name>", "provider": "<provider_name>", "provider_options": {}}' "{manager_ip}/api/v3.1/secrets/{secret_key}"`

Updates a secret.

### URI Parameters
* `secret_key`: The key of the secret to update.

### Request Body
| Property           | Type    | Description                                                                                                                                                                                                                               |
|--------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `value`            | string  | The secret's new value.                                                                                                                                                                                                                   |
| `visibility`       | string  | Optional parameter, defines who can see the secret (default: tenant). **Supported for Cloudify Manager 4.3 and above.**                                                                                                                   |
| `is_hidden_value`  | boolean | Optional parameter, determines who can see the value of the secret. If True, the value of the secret is only shown to the user that created the secret and to admins. (default: false). **Supported for Cloudify Manager 4.4 and above.** |
| `creator`          | string  | The secret's owner (username).                                                                                                                                                                                                            |
| `provider`         | string  | Optional parameter, defines which provider should be used to get the secret's value.                                                                                                                                                      |
| `provider_options` | dict    | Optional parameter, defines additional options to get the secret's value via provider.                                                                                                                                                    |

### Response
A `Secret` resource.

## Delete Secret

> Request Example

```shell
$ curl -X DELETE \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    --cacert <path_to_ca_cert> \
    "https://<manager_ip>/api/v3.1/secrets/<secret_key>"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient

client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
    cert='<path_to_ca_cert>',
)
client.secrets.delete('<secret_key>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets/<secret_key>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
requests.delete(
    url,
    auth=auth,
    headers=headers,
    verify='<path_to_ca_cert>',
)
```

`DELETE "{manager_ip}/api/v3.1/secrets/{secret_key}"`

Deletes a secret.

### URI Parameters
* `secret_key`: The key of the secret to delete.

### Response
No content - HTTP code 204.

## Set Secret Visibility

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    --cacert <path_to_ca_cert> \
    -d '{"visibility": "<visibility>"}' \
    "https://<manager_ip>/api/v3.1/secrets/<secret-key>/set-visibility"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient

client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
    cert='<path_to_ca_cert>',
)
client.secrets.set_visibility(
    '<secret-key>',
    '<visibility>',
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets/<secret-key>/set-visibility'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {'visibility': '<visibility>'}
response = requests.patch(
    url,
    auth=auth,
    headers=headers,
    verify='<path_to_ca_cert>',
    json=payload,
)
response.json()
```

> Response Example

```json
{
    "created_at": "2022-12-20T10:59:08.673Z",
    "visibility": "global",
    "value": "<secret_value_encrypted>",
    "updated_at": "2022-12-20T16:50:29.232Z",
    "is_hidden_value": false,
    "schema": null,
    "provider_options": null,
    "key": "<secret_key>",
    "provider_name": null,
    "tenant_name": "default_tenant",
    "created_by": "admin",
    "resource_availability": "global",
    "private_resource": false
}
```

`PATCH "<manager_ip>/api/v3.1/secrets/{secret-key}/set-visibility"`

Update the visibility of the secret. **Supported for Cloudify Manager 4.3 and above.**

### URI Parameters
* `secret-key`: The key of the secret to update.

### Request Body

| Property     | Type   | Description                                |
|--------------|--------|--------------------------------------------|
| `visibility` | string | Defines who can see the secret. (Required) |

Valid values are `tenant` or `global`.

### Response
A `Secret` resource.

## Export Secrets

> Request Example

```shell
 $ curl -X GET \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    --cacert <path_to_ca_cert> \
    "https://<manager_ip>/api/v3.1/secrets/share/export?_passphrase=<passphrase>?non-encrypted=false"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient

client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
    cert='<path_to_ca_cert>',
)
client.secrets.export(
    _passphrase='<passphrase>',
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets/share/export'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
querystring = {'_passphrase': '<passphrase>'}
response = requests.get(
    url,
    auth=auth,
    headers=headers,
    verify='<path_to_ca_cert>',
    params=querystring,
)
response.json()
```

> Response Example

```json
[
    {
        "key": "<secret_key>",
        "value": "<secret_value_encrypted>",
        "visibility": "global",
        "tenant_name": "default_tenant",
        "is_hidden_value": false,
        "encrypted": true
    },
    {
        "key": "<secret_key>",
        "value": "<secret_value_encrypted>",
        "visibility": "global",
        "tenant_name": "default_tenant",
        "is_hidden_value": false,
        "encrypted": true
    },
    {
        "key": "<secret_key>",
        "value": "<secret_value_encrypted>",
        "visibility": "global",
        "tenant_name": "default_tenant",
        "is_hidden_value": false,
        "encrypted": true
    }
]
```

`GET "<manager_ip>/api/v3.1/secrets/share/export"`

Export secretes from the Manager to a file. **Supported for Cloudify Manager 5.0 and above.**

### URI Parameters
* `_passphrase`: The passphrase used to encrypt or secrets` values, must be 8 characters long.

### Response
A list of `Secret` resources.

## Import Secrets

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    --cacert <path_to_ca_cert> \
    -d '{"secrets_list": [{"key": "<secret_key>", "value": "<secret_value>", "visibility": "<visibility>", "tenant_name": "<tenant_name>", "is_hidden_value": false, "encrypted": false}], "tenant_map_dict": {"<tenant_name>": "<tenant_name>"}, "passphrase": "<passphrase>", "override_collisions": false}' \
    "https://<manager_ip>/api/v3.1/secrets/share/import"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient

client = CloudifyClient(
    host='<manager_ip>',
    username='<manager_username>',
    password='<manager_password>',
    tenant='<manager_tenant>',
    cert='<path_to_ca_cert>',
)
client.secrets.import_secrets(
    secrets_list=[
        {
            "key": "<secret_key>",
            "value": "<secret_value>",
            "visibility": "<visibility>",
            "tenant_name": "<tenant_name>",
            "is_hidden_value": False,
            "encrypted": False
        }
    ],
    tenant_map={
        '<tenant_name>': '<tenant_name>',
    },
    passphrase='<passphrase>',
    override_collisions=False,
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets/share/import'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'secrets_list': [
        {
            "key": "<secret_name>",
            "value": "<secret_value>",
            "visibility": "<visibility>",
            "tenant_name": "<tenant_name>",
            "is_hidden_value": False,
            "encrypted": False
        }
    ],
    'tenant_map_dict': {
        '<tenant_name>': '<tenant_name>',
    },
    'passphrase': '<passphrase>',
    'override_collisions': False,

}
response = requests.post(
    url,
    auth=auth,
    headers=headers,
    verify='<path_to_ca_cet>',
    json=payload,
)
response.json()
```

> Response Example

```json
{
    "colliding_secrets": {},
    "secrets_errors": {}
}
```

`POST "<manager_ip>/api/v3.1/secrets/share/import"`

Import secrets from a file to the Manager. **Supported for Cloudify Manager 5.0 and above.**

### Response
An import result in JSON format.

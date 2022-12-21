# Secrets Providers

## The Secrets Provider Resource


A Secrets Provider resource is a set of details and credentials required to get a secret value, saved per tenant.
A user can ensure all providers are kept in a secured manner,
and adhere to isolation requirements between different tenants.



### Attributes:

| Attribute               | Type     | Description                                                                                                           |
|-------------------------|----------|-----------------------------------------------------------------------------------------------------------------------|
| `id`                    | string   | The Secrets Provider's name, unique per tenant.                                                                       |
| `name`                  | string   | The Secrets Provider's name, unique per tenant.                                                                       |
| `type`                  | string   | The Secrets Provider's type.                                                                                          |
| `connection_parameters` | dict     | The Secrets Provider's connection parameters (e.g. host, username, password etc).                                     |
| `visibility`            | string   | Defines who can see the provider. Can be private, tenant or global. **Supported for Cloudify Manager 4.3 and above.** |
| `tenant_name`           | string   | The name of the tenant of the provider.                                                                               |
| `created_by`            | string   | The author of the provider.                                                                                           |
| `created_at`            | datetime | The time when the provider was created.                                                                               |
| `updated_at`            | datetime | The time the provider was last updated at.                                                                            |

## List Secrets Providers

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    --cacert <path_to_ca_cert> \
    "https://<manager_ip>/api/v3.1/secrets-providers"
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
client.secrets_providers.list()

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets-providers'
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
            "created_at": "2022-12-20T18:04:17.615Z",
            "id": "<provider_name>",
            "visibility": "tenant",
            "name": "<provider_name>",
            "type": "local",
            "connection_parameters": null,
            "updated_at": null,
            "tenant_name": "default_tenant",
            "created_by": "admin",
            "resource_availability": "tenant",
            "private_resource": false
        }
    ]
}
```

`GET "{manager_ip}/api/v3.1/secrets-providers"`

List all secrets providers.

### Response
| Field      | Type | Description                              |
|------------|------|------------------------------------------|
| `items`    | list | A list of `Secrets Provider` resources.  |
| `metadata` | dict | Information about pagination result.     |

## Get Secret Provider

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    --cacert <path_to_ca_cert> \
    "https://<manager_ip>/api/v3.1/secrets-providers/<provider_name>"
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
client.secrets_providers.get('<provider_name>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets-providers/<provider_name>'
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
    "created_at": "2022-12-20T18:04:17.615Z",
    "id": "<provider_name>",
    "visibility": "tenant",
    "name": "<provider_name>",
    "type": "local",
    "connection_parameters": null,
    "updated_at": null,
    "tenant_name": "default_tenant",
    "created_by": "admin",
    "resource_availability": "tenant",
    "private_resource": false
}
```

`GET "{manager_ip}/api/v3.1/secrets-provider/{provider_name}"`

Retrieves a specific provider.

### URI Parameters
* `provider_name`: The name of the provider to retrieve.

### Response
A `Secrets Provider` resource.

## Create Secrets Provider

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    --cacert <path_to_ca_cert> \
    -d '{"name": "<provider_name>", "type": "<provider_type>", "connection_parameters": {}, "visibility": "<visibility>"}' \
    "https://<manager_ip>/api/v3.1/secrets-providers"
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
client.secrets_providers.create(
    name='<provider_name>',
    _type='<provider_type>',
    connection_parameters={},
    visibility='<visibility>',
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets-providers'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'name': '<provider_name>',
    'type': '<provider_type>',
    'connection_parameters': {},
    'visibility': '<visibility>',
}
response = requests.put(
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
    "created_at": "2022-12-20T18:31:51.559Z",
    "id": "<provider_name>",
    "visibility": "tenant",
    "name": "<provider_name>",
    "type": "local",
    "connection_parameters": null,
    "updated_at": null,
    "tenant_name": "default_tenant",
    "created_by": "admin",
    "resource_availability": "tenant",
    "private_resource": false
}
```

`PUT -d '{"name": "<provider_name>", "type": "<provider_type>", "connection_parameters": {}, "visibility": "<visibility>"}'`

Creates a Secrets Provider.

### Request Body
| Property                | Type   | Description                                                                                                               |
|-------------------------|--------|---------------------------------------------------------------------------------------------------------------------------|
| `name`                  | string | The Secrets Provider's name.                                                                                              |
| `type`                  | string | The Secrets Provider's type.                                                                                              |
| `connection_parameters` | dict   | The Secrets Provider's connection parameters (e.g. host, username, password etc).                                         |
| `visibility`            | string | Optional parameter, defines who can see the provider (default: tenant). **Supported for Cloudify Manager 4.3 and above.** |

Valid type values are:

* `local`: Secrets stored in Manager's database.
* `vault`: Secrets stored in Vault service.
  * `connection_parameters`: `{"url": "<vault_url>", "token": "<vault_token>", "path": "<vault_path>"}`
* `cloudify`: Secrets stored in remote Manager.
  * `connection_parameters`: `{"host": "<manager_host>", "username": "<manager_username>", "password": "<manager_password>", "tenant": "<manager_tenant>"}`

Valid visibility values are:

* `private`: The resource is visible to the user that created the resource, the tenant’s managers and the system’s admins.
* `tenant`: The resource is visible to all users in the current tenant. (Default value)
* `global`: The resource is visible to all users in all tenants across the manager.

### Response
A `Secrets Provider` resource.

## Update Secrets Provider

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    --cacert <path_to_ca_cert> \
    -d '{"type": "<provider_type>", "connection_parameters": {}, "visibility": "<visibility>"}' \
    "https://<manager_ip>/api/v3.1/secrets-providers/<provider_name>"
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
client.secrets_providers.update(
    name='<provider_name>',
    _type='<provider_type>',
    connection_parameters={},
    visibility='<visibility>',
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets-providers/<provider_name>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'name': '<provider_name>',
    'type': '<provider_type>',
    'connection_parameters': {},
    'visibility': '<visibility>',
}
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
    "created_at": "2022-12-20T18:31:13.350Z",
    "id": "<provider_name>",
    "visibility": "global",
    "name": "<provider_name>",
    "type": "local",
    "connection_parameters": null,
    "updated_at": "2022-12-20T19:13:59.079Z",
    "tenant_name": "default_tenant",
    "created_by": "admin",
    "resource_availability": "global",
    "private_resource": false
}
```

`PATCH -d '{"type": "<provider_type>", "connection_parameters": {}, "visibility": "<visibility>"}' "{manager_ip}/api/v3.1/secrets-providers/{provider_name}"`

Updates a Secrets Provider.

### URI Parameters
* `provider_name`: The name of the provider to update.

### Response
A `Secrets Provider` resource.

## Delete Secret

> Request Example

```shell
$ curl -X DELETE \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    --cacert <path_to_ca_cert> \
    "https://<manager_ip>/api/v3.1/secrets-providers/<provider_name>"
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
client.secrets_providers.delete('<provider_name>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets-providers/<provider_name>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
requests.delete(
    url,
    auth=auth,
    headers=headers,
    verify='<path_to_ca_cert>',
)
```

`DELETE "{manager_ip}/api/v3.1/secrets-providers/{provider_name}"`

Deletes a Secrets Provider.

### URI Parameters
* `provider_name`: The name of the provider to delete.

### Response
No content - HTTP code 204.

## Test Secrets Provider

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    --cacert <path_to_ca_cert> \
    -d '{"name": "<provider_name>", "type": "<provider_type>", "connection_parameters": {}, "test": true}' \
    "https://<manager_ip>/api/v3.1/secrets-providers"
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
client.secrets_providers.create(
    name='<provider_name>',
    _type='<provider_type>',
    connection_parameters={},
    test=True,
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'https://<manager_ip>/api/v3.1/secrets-providers'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'name': '<provider_name>',
    'type': '<provider_type>',
    'connection_parameters': {},
    'test': True,
}
response = requests.put(
    url,
    auth=auth,
    headers=headers,
    verify='<path_to_ca_cert>',
    json=payload,
)
response.json()
```

`PUT -d '{"name": "<provider_name>", "type": "<provider_type>", "connection_parameters": {}, "test": true}'`

Test a Secrets Provider.

### Response
No content - HTTP code 200.

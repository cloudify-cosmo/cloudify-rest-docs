# Sites

**Supported for Cloudify Manager 5.0 and above.**

## The Site Resource

A Site represents a container with a (typically) limited number of nodes.
A site can be a mobile cell-tower, or it can be a small branch, or any other logical entity.
Sites may be associated with a location which will allow a map view (widget is not available yet) and more advanced capabilities in the future.
Sites may contain multiple deployments, which allows for easy grouping and filtering by site.


### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`name` | string | The site's name, unique per tenant.
`location` | string | The location of the site, expected format: "latitude, longitude" such as "32.071072, 34.787274".
`visibility` | string | Defines who can see the site. Can be private, tenant or global.
`tenant_name` | string | The name of the tenant that owns the site.
`created_at` | datetime | The time when the site was created.
`created_by` | string | The name of the user that created the site.


## List Sites

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/sites"
```

```python
# Using Cloudify client
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
        host='<manager_ip>',
        username='<manager_username>',
        password='<manager_password>',
        tenant='<manager_tenant>'
)
client.sites.list()

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/sites'
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
            "created_at": "2019-06-12T10:52:45.858Z",
            "created_by": "admin",
            "location": "41.8333925, -88.0121478",
            "name": "Chicago",
            "visibility": "tenant",
            "tenant_name": "default_tenant"
        },
        {
            "created_at": "2019-06-12T10:53:06.968Z",
            "created_by": "admin",
            "location": "25.7823404, -80.3695441",
            "name": "Chicago",
            "visibility": "tenant",
            "tenant_name": "default_tenant"
        },
        {
            "created_at": "2019-06-12T10:53:32.838Z",
            "created_by": "admin",
            "location": "32.080327, 34.767420",
            "name": "Tel-Aviv",
            "visibility": "tenant",
            "tenant_name": "default_tenant"
        }
    ],
    "metadata": {
        "pagination": {
            "offset": 0,
            "size": 1000,
            "total": 3
        }
    }
}
```

`GET "{manager_ip}/api/v3.1/sites"`

List all sites.

### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Site` resources.



## Get Site

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/sites/<site_name>"
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
client.sites.get(<site_name>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/sites/<site_name>'
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
    "created_at": "2019-06-12T10:53:32.838Z",
    "created_by": "admin",
    "location": "32.080327, 34.767420",
    "name": "Tel-Aviv",
    "visibility": "tenant",
    "tenant_name": "default_tenant"
}
```

`GET "{manager_ip}/api/v3.1/sites/{site_name}"`

Retrieves a specific site.

### URI Parameters
* `site_name`: The name of the site to retrieve.

### Response
A `Site` resource.



## Create Site

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"location": "<site_location>", "visibility": "<visibility>"}' \
    "http://<manager_ip>/api/v3.1/sites/<site_name>"
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
client.sites.create(
    '<site_name>',
    location='<site_location>',
    visibility='<visibility>'
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/sites/<site_name>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'name': '<site_name>',
    'location': '<site_location>',
    'visibility': '<visibility>'
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
    "created_at": "2019-06-13T12:38:37.747Z",
    "created_by": "admin",
    "name": "Tel-Aviv",
    "location": "32.080327, 34.767420",
    "visibility": "tenant",
    "tenant_name": "default_tenant"
}
```

`PUT -d '{"location": "<site_location>", "visibility": "<visibility>"}' "{manager_ip}/api/v3.1/sites/{site_name}"`

Creates a site.

### URI Parameters
* `site_name`: The name of the site to create.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`location` | string | Optional parameter, the location of the site, expected format: "latitude, longitude" such as "32.071072, 34.787274".
`visibility` | string | Optional parameter, defines who can see the site (default: tenant)

Valid visibility values are:

* `private`: The resource is visible to the user that created the resource, the tenant’s managers and the system’s admins.
* `tenant`: The resource is visible to all users in the current tenant. (Default value)
* `global`: The resource is visible to all users in all tenants across the manager.

### Response
A `Site` resource.



## Update Site

> Request Example

```shell
$ curl -X POST \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"new_name": "<site_new_name>", "location": "<site_location>", "visibility": "<visibility>"}' \
    "http://<manager_ip>/api/v3.1/sites/<site_name>"
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
client.sites.update(
    '<site_name>',
    location='<site_location>',
    visibility='<visibility>',
    new_name='<site_new_name>'
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/sites/<site_name>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {'new_name': '<site_new_name>', 'location': '<site_location>', 'visibility': '<visibility>'}
response = requests.post(
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
    "created_at": "2019-06-13T12:38:37.747Z",
    "created_by": "admin",
    "name": "Tel-Aviv",
    "location": "32.080327, 34.767420",
    "visibility": "tenant",
    "tenant_name": "default_tenant"
}
```

`POST -d '{"new_name": "<site_name>", "location": "<site_location>", "visibility": "<visibility>"}' "{manager_ip}/api/v3.1/sites/{site_name}"`

Updates a site.

### URI Parameters
* `site_name`: The name of the site to update.


### Request Body
Property | Type | Description
--------- | ------- | -----------
`new_name` | string | Optional parameter, the new name of the site
`location` | string | Optional parameter, the location of the site, expected format: "latitude, longitude" such as "32.071072, 34.787274".
`visibility` | string | Optional parameter, defines who can see the site

Valid visibility values are:

* `tenant`: The resource is visible to all users in the current tenant.
* `global`: The resource is visible to all users in all tenants across the manager.



### Response
A `Site` resource.



## Delete Site

> Request Example

```shell
$ curl -X DELETE \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/sites/<site_name>"
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
client.sites.delete(<site_name>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/sites/<site_name>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
requests.delete(
    url,
    auth=auth,
    headers=headers,
)
```

`DELETE "{manager_ip}/api/v3.1/sites/{site_name}"`

Deletes a site.

### URI Parameters
* `site_name`: The name of the site to delete.

### Response
No content - HTTP code 204.

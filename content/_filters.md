# Filters

## The Filter Resource


A Filter resource is a set of filter-rules that can be used to filter a list of objects, based on their labels.
Filter-rules can be of the following forms:

* `x=y`: All objects with the label `x:y`. 

* `x=[y,z]`: All objects with the label `x:y or x:z`.

* `x!=y`: All objects with the label `x:<any value other than y>`.  

* `x!=[w,z]`: All objects with the label `x:<any value other than y and z>`.

* `x is null`: All objects that don’t have the label `x:<any value>`.

* `x is not null`: All objects that have the label `x:<any value>`.



### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | The filter's ID, unique per tenant.
`value` | dict | The filter's rules. Currently, of the form {'labels': {'not_equal': {}, 'equal': {}, 'is_null': [], 'is_not_null': []}}
`labels_filters` | list | A list of the labels filters as strings.
`visibility` | string | Defines who can see the filter. Can be private, tenant or global.
`created_at` | datetime | The time when the filter was created.
`updated_at` | datetime | The time the filter was last updated at.

## List Filters

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/filters"
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
client.filters.list()

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/filters'
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
  "metadata": {
    "pagination": {
      "total": 1,
      "size": 1000,
      "offset": 0
    }
  },
  "items": [
    {
      "id": "gcp-tel-aviv",
      "visibility": "tenant",
      "created_at": "2021-01-24T14:48:48.429Z",
      "value": {
        "labels": {
          "equal": {
            "env": [
              "gcp"
            ],
            "location": [
              "tel-aviv"
            ]
          }
        }
      },
      "updated_at": "2021-01-24T14:48:48.429Z",
      "tenant_name": "default_tenant",
      "created_by": "admin",
      "resource_availability": "tenant",
      "private_resource": false,
      "labels_filters": [
        "env=gcp",
        "location=tel-aviv"
      ]
    }
  ]
}
```

`GET "{manager_ip}/api/v3.1/filters"`

List all filters.

### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Filter` resources.



## Get Filter

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/filters/<filter_id>"
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
client.filters.get(<filter_id>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/filters/<filter_id>'
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
  "id": "gcp-tel-aviv",
  "visibility": "tenant",
  "created_at": "2021-01-24T14:48:48.429Z",
  "value": {
    "labels": {
      "equal": {
        "env": [
          "gcp"
        ],
        "location": [
          "tel-aviv"
        ]
      }
    }
  },
  "updated_at": "2021-01-24T14:48:48.429Z",
  "tenant_name": "default_tenant",
  "created_by": "admin",
  "resource_availability": "tenant",
  "private_resource": false,
  "labels_filters": [
    "env=gcp",
    "location=tel-aviv"
  ]
}
```

`GET "{manager_ip}/api/v3.1/filters/{filter_id}"`

Retrieves a specific filter.

### URI Parameters
* `filter_id`: The ID of the filter to retrieve.

### Response
A `Filter` resource.



## Create Filter

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"filter_rules": <filter_rules_list>, "visibility": "<visibility>"}' \
    "http://<manager_ip>/api/v3.1/filters/<filter_id>"
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
client.filters.create(
    <new_filter_id>,
    <filter_rules_list>,
    <visibility>
)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/filters/<new_filter_id>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {
    'filter_rules': <filter_rules_list>,
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
  "id": "gcp-tel-aviv",
  "visibility": "tenant",
  "created_at": "2021-01-24T14:48:48.429Z",
  "value": {
    "labels": {
      "equal": {
        "env": [
          "gcp"
        ],
        "location": [
          "tel-aviv"
        ]
      }
    }
  },
  "updated_at": "2021-01-24T14:48:48.429Z",
  "tenant_name": "default_tenant",
  "created_by": "admin",
  "resource_availability": "tenant",
  "private_resource": false,
  "labels_filters": [
    "env=gcp",
    "location=tel-aviv"
  ]
}
```

`PUT -d '{"filter_rules": <filter_rules_list>, "visibility": <visibility>}' "{manager_ip}/api/v3.1/filters/{new_filter_id}"`

Creates a filter.

### URI Parameters
* `new_filter_id`: The ID of the filter to create.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`filter_rules` | list | The filter's rules list. E.g. `['env=aws', 'arch is null', 'location!=[london,tel-aviv]']`
`visibility` | string | Optional parameter, defines who can see the filter (default: tenant).

Valid visibility values are:

* `private`: The resource is visible to the user that created the resource, the tenant’s managers and the system’s admins.
* `tenant`: The resource is visible to all users in the current tenant. (Default value)
* `global`: The resource is visible to all users in all tenants across the manager.

### Response
A `Filter` resource.



## Update Filter

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"filter_rules": <new_filter_rules_list>, "visibility": "<visibility>"}' \
    "http://<manager_ip>/api/v3.1/filters/<filter_id>"
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
client.filters.update(<filter_id>, <new_filter_rules_list>, <new_visibility>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/filters/<filter_id>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
payload = {'filter_rules': '<new_filter_rules_list>', 'visibility': '<new_visibility>'}
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
  "id": "gcp-tel-aviv",
  "visibility": "tenant",
  "created_at": "2021-01-24T14:48:48.429Z",
  "value": {
    "labels": {
      "equal": {
        "env": [
          "gcp"
        ],
        "location": [
          "tel-aviv"
        ]
      }
    }
  },
  "updated_at": "2021-01-24T14:48:48.429Z",
  "tenant_name": "default_tenant",
  "created_by": "admin",
  "resource_availability": "tenant",
  "private_resource": false,
  "labels_filters": [
    "env=gcp",
    "location=tel-aviv"
  ]
}
```

`PATCH -d '{"filter_rules": <new_filter_rules_list>, "visibility": <new_visibility>}' "{manager_ip}/api/v3.1/filters/{filter_id}"`

Updates a filter.

### URI Parameters
* `filter_id`: The ID of the filter to update.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`filter_rules` | list | The new filter's rules list. E.g. `['env=aws', 'arch is null', 'location!=[london, tel-aviv]']`
`visibility` | string | Optional parameter, defines who can see the filter (default: tenant).

### Response
A `Filter` resource.



## Delete Filter

> Request Example

```shell
$ curl -X DELETE \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/filters/<filter_id>"
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
client.filters.delete(<filter_id>)

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/filters/<filter_id>'
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
requests.delete(
    url,
    auth=auth,
    headers=headers,
)
```

`DELETE "{manager_ip}/api/v3.1/filters/{filter_id}"`

Deletes a filter.

### URI Parameters
* `filter_id`: The ID of the filter to delete.

### Response
No content - HTTP code 204.

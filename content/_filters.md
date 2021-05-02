# Filters

## The Filter Resource

A Filter resource is a set of filter-rules that can be used to filter a list of resources, based on their labels and attributes.
A filter rule is a dictionary of the following form: 
```text
{
 "key": "<key>",
 "values": [<list of values>],
 "operator": "<LabelsOperator>" or "<AttrsOperator>",
 "type": "<FilterRuleType>"
}
```
`<LabelsOperator>` can be one of: "any_of", "not_any_of", "is_null", "is_not_null", or "is_not".

`<AttrsOperator>` can be one of: "any_of", "not_any_of", "contains", "not_contains", "starts_with", "ends_with", "is_not_empty".

`<FilterRuleType>` can be either "label" or "attribute". If "label" is provided, then the operator must be a `<LabelsOperator>`, and if "attribute" is provided, then 
the operator must be an `<AttrsOperator>`. 

E.g. filtering by the following filter rules, will return all deployments whose creator name starts with "alice" or "bob", 
and have the label `environment:aws` assigned to them.

```json
[
 {
  "key": "created_by",
  "values": ["alice", "bob"],
  "operator": "starts-with",
  "type": "attribute"
 },
 {
  "key": "environment",
  "values": ["aws"],
  "operator": "any_of",
  "type": "label"
 }
]
```

**Filters can be used currently for deployments and blueprints.**

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | The filter's ID, unique per tenant.
`value` | list | A list of the filter's filter-rules.
`labels_filter_rules` | list | A list of the filter's filter-rules of type `label`.
`attrs_filter_rules` | list | A list of the filter's filter-rules of type `attribute`.
`visibility` | string | Defines who can see the filter. Can be private, tenant or global.
`created_at` | datetime | The time when the filter was created.
`updated_at` | datetime | The time the filter was last updated at.
`tenant_name` | string | The name of the tenant that owns the filter.

## List Filters

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/filters/<resource>"
```

`<resource>` can be either `deployments` or `blueprints`.

```python
# Using Cloudify client
client.deployments_filters.list()
# Or
client.blueprints_filters.list()

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/filters/<resource>' # `<resource>` can be either `deployments` or `blueprints`
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
    },
    "filtered": null
  },
  "items": [
    {
      "id": "new_filter",
      "visibility": "tenant",
      "created_at": "2021-03-25T11:48:56.525Z",
      "value": [
        {
          "key": "os",
          "values": [
            "windows"
          ],
          "operator": "any_of",
          "type": "label"
        },
        {
          "key": "created_by",
          "values": [
            "bob"
          ],
          "operator": "starts_with",
          "type": "attribute"
        }
      ],
      "updated_at": "2021-03-25T11:48:56.525Z",
      "tenant_name": "default_tenant",
      "created_by": "admin",
      "resource_availability": "tenant",
      "private_resource": false,
      "labels_filter_rules": [
        {
          "key": "os",
          "values": [
            "windows"
          ],
          "operator": "any_of",
          "type": "label"
        }
      ],
      "attrs_filter_rules": [
        {
          "key": "created_by",
          "values": [
            "bob"
          ],
          "operator": "starts_with",
          "type": "attribute"
        }
      ]
    }
  ]
}
```

`GET "{manager_ip}/api/v3.1/filters/<resource>"`

List all filters of a resource. Resource can be either deployments of blueprints.

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
    "http://<manager_ip>/api/v3.1/filters/<resource>/<filter_id>"
```

`<resource>` can be either `deployments` or `blueprints`.

```python
# Using Cloudify client
client.deployments_filters.get('<filter_id>')
# Or
client.blueprints_filters.get('<filter_id>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/filters/<resource>/<filter_id>' # `<resource>` can be either `deployments` or `blueprints`
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
  "id": "new_filter",
  "visibility": "tenant",
  "created_at": "2021-03-25T11:48:56.525Z",
  "value": [
    {
      "key": "os",
      "values": [
        "windows"
      ],
      "operator": "any_of",
      "type": "label"
    },
    {
      "key": "created_by",
      "values": [
        "bob"
      ],
      "operator": "starts_with",
      "type": "attribute"
    }
  ],
  "updated_at": "2021-03-25T11:48:56.525Z",
  "tenant_name": "default_tenant",
  "created_by": "admin",
  "resource_availability": "tenant",
  "private_resource": false,
  "labels_filter_rules": [
    {
      "key": "os",
      "values": [
        "windows"
      ],
      "operator": "any_of",
      "type": "label"
    }
  ],
  "attrs_filter_rules": [
    {
      "key": "created_by",
      "values": [
        "bob"
      ],
      "operator": "starts_with",
      "type": "attribute"
    }
  ]
}
```

`GET "{manager_ip}/api/v3.1/filters/<resource>/{filter_id}"`

Retrieves a specific resource's filter. Resource can be either deployments of blueprints. 

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
    "http://<manager_ip>/api/v3.1/filters/<resource>/<filter_id>"
```

`<resource>` can be either `deployments` or `blueprints`.

```python
# Using Cloudify client
client.deployments_filters.create(filter_id="<the new filter's id>", 
                                  filter_rules=[...], 
                                  visibility="<the filter's visibility>")
# Or
client.blueprints_filters.create(filter_id="<the new filter's id>", 
                                 filter_rules=[...], 
                                 visibility="<the filter's visibility>")

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/filters/<resource>/<filter_id>' # `<resource>` can be either `deployments` or `blueprints`
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {
    'Content-Type': 'application/json',
    'Tenant': '<manager-tenant>',
}
payload = {
    'filter_rules': [...],
    'visibility': "<the filter's visibility>"
}
response = requests.put(
    url,
    auth=auth,
    headers=headers,
    json=payload
)
response.json()
```

> Response Example

```json
{
  "id": "new_filter",
  "visibility": "tenant",
  "created_at": "2021-03-25T12:10:24.607Z",
  "value": [
    {
      "key": "created_by",
      "values": [
        "admin"
      ],
      "operator": "any_of",
      "type": "attribute"
    }
  ],
  "updated_at": "2021-03-25T12:10:24.607Z",
  "tenant_name": "default_tenant",
  "created_by": "admin",
  "resource_availability": "tenant",
  "private_resource": false,
  "labels_filter_rules": [
    
  ],
  "attrs_filter_rules": [
    {
      "key": "created_by",
      "values": [
        "admin"
      ],
      "operator": "any_of",
      "type": "attribute"
    }
  ]
}
```

`PUT -d '{"filter_rules": <filter_rules_list>, "visibility": <visibility>}' "{manager_ip}/api/v3.1/filters/<resource>/{filter_id}"`

Creates a resource's filter. Resource can be either deployments of blueprints.

### URI Parameters
* `filter_id`: The ID of the filter to create.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`filter_rules` | list | The filter's rules list as described above. 
`visibility` | string | Optional parameter, defines who can see the filter (default: tenant).

Valid visibility values are:

* `private`: The filter is visible to the user that created the filter, the tenant’s managers and the system’s admins.
* `tenant`: The filter is visible to all users in the current tenant. (Default value)
* `global`: The filter is visible to all users in all tenants across the manager.

### Response
A `Filter` resource.


## Update Filter

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    -d '{"filter_rules": <new_filter_rules_list>, "visibility": "<new_visibility>"}' \
    "http://<manager_ip>/api/v3.1/filters/<resource>/<filter_id>"
```

`<resource>` can be either `deployments` or `blueprints`.

```python
# Using Cloudify client
client.deployments_filters.update(filter_id="<the updated filer's ID>", 
                                  new_filter_rules=[...], 
                                  new_visibility="<the new filter's visibility>")
# Or
client.blueprints_filters.update(filter_id="<the updated filer's ID>", 
                                 new_filter_rules=[...], 
                                 new_visibility="<the new filter's visibility>")

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/filters/<resource>/<filter_id>' # `<resource>` can be either `deployments` or `blueprints`
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {
    'Content-Type': 'application/json',
    'Tenant': '<manager_tenant>',
}
payload = {
    'filter_rules': [...],
    'visibility': "<the new filter's visibility>"
}
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
  "id": "filter1",
  "visibility": "tenant",
  "created_at": "2021-03-25T12:10:24.607Z",
  "value": [
    {
      "key": "created_by",
      "values": [
        "bob"
      ],
      "operator": "any_of",
      "type": "attribute"
    }
  ],
  "updated_at": "2021-03-25T12:41:03.350Z",
  "tenant_name": "default_tenant",
  "created_by": "admin",
  "resource_availability": "tenant",
  "private_resource": false,
  "labels_filter_rules": [
    
  ],
  "attrs_filter_rules": [
    {
      "key": "created_by",
      "values": [
        "bob"
      ],
      "operator": "any_of",
      "type": "attribute"
    }
  ]
}
```

`PATCH -d '{"filter_rules": <new_filter_rules_list>, "visibility": <new_visibility>}' "{manager_ip}/api/v3.1/filters/<resource>/{filter_id}"`

Updates a resource's filter. Resource can be either deployments of blueprints.

### URI Parameters
* `filter_id`: The ID of the filter to update.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`filter_rules` | list | The new filter's rules list as described above.
`visibility` | string | Optional parameter, defines who can see the filter (default: tenant).

### Response
A `Filter` resource.


## Delete Filter

> Request Example

```shell
$ curl -X DELETE \
    -H "Tenant: <manager_tenant>" \
    -u <manager_username>:<manager_password> \
    "http://<manager_ip>/api/v3.1/filters/<resource>/<filter_id>"
```

`<resource>` can be either `deployments` or `blueprints`.

```python
# Using Cloudify client
client.deployments_filters.delete('<filter_id>')
# Or
client.blueprints_filters.delete('<filter_id>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager_ip>/api/v3.1/filters/<resource>/<filter_id>' # `<resource>` can be either `deployments` or `blueprints`
auth = HTTPBasicAuth('<manager_username>', '<manager_password>')
headers = {'Tenant': '<manager_tenant>'}
requests.delete(
    url,
    auth=auth,
    headers=headers,
)
```

`DELETE "{manager_ip}/api/v3.1/filters/<resource>/{filter_id}"`

Deletes a resource's filter. Resource can be either deployments of blueprints

### URI Parameters
* `filter_id`: The ID of the filter to delete.

### Response
No content - HTTP code 204.

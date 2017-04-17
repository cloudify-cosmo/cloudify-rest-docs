# Cloudify REST API V3

> Basic usage

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-pasword> \
    "http://<manager-ip>/api/v3/<endpoint>"
```

```python
# Using ClodifyClient
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
    host='<manager-ip>',
    username='<manager-username>',
    password='<manager-password>',
    tenant='<manager-tenant>')

# Using requests
import requests
from requests.auth import HTTPBasicAuth

url = 'http://<manager-ip>/api/v3/<endpoint>'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers)
response.json()
```

Welcome to Cloudify's REST API Documentation!

The base URI for the v3 REST API is: `/api/v3`.

<aside class="notice">
This section describes various API features that apply to all resources
</aside>

Starting from Cloudify 4.0.0, all communication to the server requires:

 * Authentication using user credentials.
 * Tenant name, representing the scope of the request.

Every Cloudify Manager has a default tenant, called `default_tenant`.
The `default_tenant` tenant is created during bootstrap.

In addition to the `default_tenant`, every Cloudify Manager includes a bootstrap Admin.
The bootstrap Admin is the Admin user that created during the bootstrap.

In addition to the user credentials, every request must also specify a tenant in the header.

In the case of using the Cloudify community edition or if you have not created any new tenant,
you can use the `default_tenant` as the tenant for the request.

### Parameters
* `<manager-ip>`: Replace with the IP of your Cloudify Manager
* `<manager-username>`: Replace with a username for the Cloudify Manager instance username
* `<manager-password>`: Replace with the password for the user specified in <manager-username>
* `<manager-tenant>`: Replace with the tenant on which to perform the request

## Response Fields Filtering (Projection)

> Request Example (receive only the `id` and `created_at` fields)

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-api>/api/v3/blueprints?_include=id,created_at"
```

```python
# Using ClodifyClient
blueprints = client.blueprints.list(_include=['id','created_at'])
for blueprint in blueprints:
  print blueprint

# Using requests
url = 'http://<manager-ip>/api/v3/blueprints'
querystring = {'_include': 'id,created_at'}
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring)
response.json()
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/blueprints",
  "method": "GET",
  "data": {_include='id,created_at'},
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> Response Example

```json
{
  "items": [
    {
      "created_at": "2017-04-17T12:12:36.626Z",
      "id": "hello-world"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 1,
      "offset": 0,
      "size": 1
    }
  }
}
```


You can choose to have only specific fields in the response by using the  `_include` query parameter.

The parameter value is a comma separated list of fields to include in the response, e.g. `_include=field1,field2,field3`

Note that specified field names must be part of the resource schema, otherwise an error is raised.



## Query Filtering (Selection)

> Request Example (requesting only blueprints which `id` is _my_blueprint1_ or _my_blueprint2_)

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-pasword> \
    "http://<manager-ip>/api/v3/blueprints?_include=id,created_at&id=my-blueprint-1&id=my-blueprint-2"
```

```python
# Using ClodifyClient
blueprints = client.blueprints.list(
    _include=['id','created_at'],
    id=['my-blueprint-1', 'my-blueprint-2'],
)
for blueprint in blueprints:
    print blueprint

# Using requests
url = "http://<manager-ip>/api/v2.1/blueprints"
headers = {'Tenant': '<manager-tenant>'}
querystring = {
    '_include': 'id,created_at',
    'id': ['my-blueprint-1', 'my-blueprint-2'],
}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
response.json()
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/blueprints?id=my_blueprint1&id=my_blueprint2&_include=id%2Ccreated_at",
  "method": "GET",
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> Response Example

```json
{
  "items": [
    {
      "created_at": "2017-04-17T12:34:52.911Z",
      "id": "my-blueprint-1"
    },
    {
      "created_at": "2017-04-17T12:34:57.256Z",
      "id": "my-blueprint-2"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 2,
      "offset": 0,
      "size": 2
    }
  }
}
```


You can make your query more specific by using filters.

Filters are query parameters where the key is a field name and the value is a field value, e.g. `id=my-specific-id`

Filters also accept multiple values (OR) by using multiple parameters of the same key, e.g. `id=my-specific-id&id=another-id`

<aside class="warning">
<strong>_include</strong>, <strong>_sort</strong>, <strong>_size</strong>, <strong>_offset</strong> and <strong>_range</strong> are reserved keywords and cannot be used as filters.
</aside>

## Sorting

> Request Example #1 (sort deployments by `id` descending)

```shell
$ curl -X GET "<manager-ip>/api/v2.1/deployments?_sort=-id&_include=blueprint_id,id"
```

```python
# Python Requests-
url = "http://<manager-ip>/api/v2.1/deployments"
querystring = {"_sort":"-id","_include":"blueprint_id,id"}
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/deployments?_sort=-id&_include=blueprint_id%2Cid",
  "method": "GET",
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> Response Example #1

```json
{
  "items": [
    {
      "id": "hello1",
      "blueprint_id": "hello-world"
    },
    {
      "id": "dep4",
      "blueprint_id": "my_blueprint2"
    },
    {
      "id": "dep3",
      "blueprint_id": "my_blueprint1"
    },
    {
      "id": "dep2",
      "blueprint_id": "my_blueprint2"
    },
    {
      "id": "dep1",
      "blueprint_id": "my_blueprint1"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 5,
      "offset": 0,
      "size": 10000
    }
  }
}
```

> Request Example #2 (sort deployments by `blueprint_id` ascending and `id` descending)

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/deployments?_sort=blueprint_id&_sort=-id&_include=blueprint_id,id"
```

```python
# Python Requests-
url = "http://<manager-ip>/api/v2.1/deployments"
querystring = {"_sort":"blueprint_id,-id","_include":"blueprint_id,id"}
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/deployments?_sort=blueprint_id&_sort=-id&_include=blueprint_id%2Cid",
  "method": "GET",
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> Response Example #2

```json
{
  "items": [
    {
      "id": "hello1",
      "blueprint_id": "hello-world"
    },
    {
      "id": "dep3",
      "blueprint_id": "my_blueprint1"
    },
    {
      "id": "dep1",
      "blueprint_id": "my_blueprint1"
    },
    {
      "id": "dep4",
      "blueprint_id": "my_blueprint2"
    },
    {
      "id": "dep2",
      "blueprint_id": "my_blueprint2"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 5,
      "offset": 0,
      "size": 10000
    }
  }
}
```

Sort resources by using the `_sort` query parameter, e.g. `_sort=id`

The default sort order is ascending; to make it descending, prefix the field with a minus sign, e.g. `_sort=-id`  (example #1)

Sorting also works on multiple fields by using multiple `_sort` parameters, where the sort sequence corresponds to the
order of `_sort` parameters in the request (example #2).

## Pagination

> Request Example (skip `1` resource, get `size` of `4`)

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/events?_size=4&_offset=1&_include=@timestamp"
```

```python
# Python Requests
url = "http://<manager-ip>/api/v2.1/events"
querystring = {"_size":"4","_offset":"1","_include":"@timestamp"}
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/events?_size=4&_offset=1&_include=%40timestamp",
  "method": "GET",
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> Response Example

```json
{
  "items": [
  {
    "@timestamp": "2015-12-01T15:05:36.692Z"
  },
  {
    "@timestamp": "2015-12-01T15:05:37.493Z"
  },
  {
    "@timestamp": "2015-12-01T15:03:57.911Z"
  },
  {
    "@timestamp": "2015-12-01T15:03:58.025Z"
  }
  ],
  "metadata": {
    "pagination": {
      "total": 171,
      "offset": 1,
      "size": 4
    }
  }
}
```

If the response includes too many items for the client to handle at once, use pagination to get only a subset of the
results, defined by two parameters:

* `_size` (default: 10000) the max size of the result subset to receive.
* `_offset` (default: 0) the number of resources to skip, i.e. `_offset=1` means you skip the first resource.

\* both parameters are optional.

The response metadata returns the requested parameters, and a `total` field which indicates the size of the full set.

## Authentication

Authentication headers should be added to every request sent to a secured manager.<br>
Any header can be used, as long as it's support by one of the manager's authentication providers.
The default manager configuration supports basic HTTP authentication (examples #1, #2) and tokens (example #3).<br>
Valid credentials do not affect the returned response, but invalid credentials return a "User Unauthorized" error.

> Request Example #1 (Get the server’s status, authenticate with username and password)

```shell
$ curl -X GET "<manager-ip>/api/v2.1/status"
```

```python
# Python Client-
client.manager.get_status()

# Python Requests-
url = "http://<manager-ip>/api/v2.1/status"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/status",
  "method": "GET",
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> Response Example #1

```json
{
   "status":"running",
   "services":[
      {
         "display_name":"Celery Management",
         "instances":[
            {
               "Id": "cloudify-mgmtworker.service",
               "Description":"Cloudify Management Worker Service",
               "LoadState":"loaded",
               "state":"running"
            },
         ]
      },
      ...
   ]
}
```

> Request Example #2 (Get a token, authenticate with username and password)

```shell
$ curl -u 'MY_USERNAME':'MY_PASSWORD' "<manager-ip>/api/v2.1/token"
```

> Response Example #2

```json
{
   "value":"eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ1MDAzMjI0MiwiaWF0IjoxNDUwMDMxNjQyfQ.eyJ1c2VybmFtZSI6ImF"
}
```
> Request Example #3 (Get all the blueprints, authenticate with a token)

```shell
$ curl -H 'Authentication-Token:MY_TOKEN' "<manager-ip>/api/v2.1/blueprints"
```

> Response Example #3

```json
{
   "items":[
      {
         "main_file_name":"openstack-blueprint.yaml",
         "description":"This Blueprint installs a nodecellar application on an openstack environment",
         "created_at":"2015-12-13 19:00:03.160167",
         "updated_at":"2015-12-13 19:00:03.160167",
         "plan":{
            "relationships":{
               "cloudify.openstack.server_connected_to_port":{
                                 "name":"cloudify.openstack.server_connected_to_port",
               ...
               }
            }
         }
      }
   ]
}
```

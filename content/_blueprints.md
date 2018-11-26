# Blueprints

## The Blueprint Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`created_at` | datetime | The time the blueprint was uploaded to the manager.
`description` | string | The blueprint's description.
`id` | string | A unique identifier for the blueprint.
`main_file_name` | string | The blueprint's main file name.
`plan` | dict | The parsed result of the blueprint.
`updated_at` | datetime | The last time the blueprint was updated.


## Get Blueprint

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/blueprints?id=<blueprint-id>&_include=id"
```

```python
# Using CloudifyClient
client.blueprints.get(blueprint_id='<blueprint-id>')

# Using requests
url = 'http://<manager-ip>/api/v3.1/blueprints'
headers = {'Tenant': '<manager-tenant>'}
querystring = {
    'id': '<blueprint-id>',
    '_include': 'id',
}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
response.json()
```

> Response Example

```json
{
  "items": [
    {
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

`GET "{manager-ip}/api/v3.1/blueprints?id={blueprint-id}"`

Gets a specific blueprint.

### URI Parameters
* `blueprint-id`: The id of the blueprint to retrieve.

### Response
A `Blueprint` resource.


## Upload Blueprint

> Request Example

```shell
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>?application_file_name=<blueprint-id>.yaml&blueprint_archive_url=https://url/to/archive/master.zip&visibility=<visibility>"
```

```python
# Using CloudifyClient
client.blueprints._upload(
    blueprint_id='<blueprint-id>',
    archive_location='https://url/to/archive/master.zip',
    application_file_name='<blueprint-id>.yaml',
    visibility='<visibility>'
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>'
headers = {'Tenant': '<manager-tenant>'}
querystring = {
    'application_file_name': '<blueprint-id>.yaml',
    'blueprint_archive_url': 'https://url/to/archive/master.zip',
    'visibility': '<visibility>'
}
response = requests.put(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
response.json()
```

> Response Example

```json
{
  "main_file_name": "singlehost-blueprint.yaml",
  "description": "This blueprint installs a simple web server on the manager VM using Cloudify's script plugin.\n",
  "tenant_name": "default_tenant",
  "created_at": "2017-04-19T10:56:06.267Z",
  "updated_at": "2017-04-19T10:56:06.267Z",
  "created_by": "admin",
  "private_resource": false,
  "visibility": "tenant",
  "plan": {
    ...
  },
  "id": "hello-world"
}
```

`PUT "{manager-ip}/api/v3.1/blueprints/{blueprint-id}?application_file_name={blueprint-id}.yaml&blueprint_archive_url=https://url/to/archive/master.zip&visibility=<visibility>"`

Uploads a blueprint to Cloudify's manager.
The call expects an "application/octet-stream" content type where the content is a zip/tar.gz/bz2 archive.
It is possible to upload a blueprint from a URL by specifying the URL in the `blueprint_archive_url` request body property.


### URI Parameters
* `blueprint-id`: The id of the uploaded blueprint.

### Request Body
Property | Type | Description
-------- | ---- | -----------
`application_file_name` | string | The main blueprint file name in the blueprint's archive.
`blueprint_archive_url` | string | A URL the blueprint to be uploaded should be downloaded from by the manager.
`visibility` | string | Optional parameter, defines who can see the blueprint (default: tenant). **Supported for Cloudify Manager 4.3 and above.**

Valid visibility values are:

* `private`: The resource is visible to the user that created the resource, the tenant’s managers and the system’s admins.
* `tenant`: The resource is visible to all users in the current tenant. (Default value)
* `global`: The resource is visible to all users in all tenants across the manager.

### Response
A `Blueprint` resource.

## List Blueprints

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/blueprints?_include=id"
```

```python
# Using CloudifyClient
blueprints = client.blueprints.list(_include=['id'])
for blueprint in blueprints:
    print blueprint

# Using requests
url = "http://<manager-ip>/api/v3.1/blueprints"
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_include': 'id'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
response.json()
```

> Response Example

```json
{
  "items": [
    {
      "id": "hello-world"
    },
    {
      "id": "hello-world-2"
    },
    {
      "id": "hello-world-3"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 3,
      "offset": 0,
      "size": 3
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/blueprints"`

Lists all blueprints.

### Response

Field | Type | Description
----- | ---- | -----------
`items` | list | A list of `Blueprint` resources.


## Delete Blueprint

> Request Example

```shell
$ curl -X DELETE \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/blueprints/<blueprint-id>?force=false"
```

```python
# Using CloudifyClient
client.blueprints.delete(blueprint_id='<blueprint-id>', force=False)

# Using requests
url = 'http://<manager-ip>/ap/v3.1/blueprints/<blueprint-id>?force=false'
headers = {'Tenant': '<manager-tenant>'}
response = requests.delete(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
)
response.json()
```

> Response Example

```json
{
  "tenant_name": "default_tenant",
  "created_at": "2017-04-19T13:35:13.971Z",
  "updated_at": "2017-04-19T13:35:13.971Z",
  "created_by": "admin",
  "private_resource": false,
  "visibility": "tenant",
  "plan": {
    ...
  },
  "id": "hello-world"
}
```

`DELETE "{manager-ip}/api/v3.1/blueprints/{blueprint-id}"`

Deletes a specific blueprint.

### URI Parameters
Property | Type | Description
--------- | ------- | -----------
`blueprint_id` | string | The id of the blueprint to delete.
`force` | bool | Delete the blueprint, even if there are blueprints that are currently using it. **Supported for Cloudify Manager 4.5.5 and above.**

### Response
A `Blueprint` resource.


## Download Blueprint
Downloads a specific blueprint as an archive.

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>/archive" > <blueprint-archive-filename>.tar.gz
```

```python
# Using CloudifyClient
client.blueprints.download(blueprint_id='<blueprint-id>')

# Using requests
url = 'http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>/archive'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
)
with open('<blueprint-archive-filename>.tar.gz', 'wb') as blueprint_archive:
    blueprint_archive.write(response.content)
```

`GET "{manager-ip}/api/v3.1/blueprints/{blueprint-id}/archive"`

### URI Parameters
* `blueprint-id`: The id of the blueprint to download.

### Response
The blueprint as an archive using an `application/octet-stream` content type.


## Set Global Blueprint

> Request Example

```shell
$ curl -X PATCH -H "Content-Type: application/json" -H "tenant: <tenant-name>"
    -u user:password "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>/set-global"
```

```python
# Python Client
client.blueprints.set_global('<blueprint-id>')
```

> Response Example

```json
{
  "main_file_name": "singlehost-blueprint.yaml",
  "description": "This blueprint installs a simple web server on the manager VM using Cloudify's script plugin.\n",
  "tenant_name": "default_tenant",
  "created_at": "2017-04-19T10:56:06.267Z",
  "updated_at": "2017-04-19T10:56:06.267Z",
  "created_by": "admin",
  "private_resource": false,
  "visibility": "global",
  "plan": {
    ...
  },
  "id": "hello-world"
}
```

`PATCH "{manager-ip}/api/v3.1/blueprints/{blueprint-id}/set-global"`

Set the blueprint's visibility to global.
Will be deprecated soon. For Cloudify Manager 4.3 and above, use 'set-visibility'.

### URI Parameters
* `blueprint-id`: The id of the blueprint to update.

### Response
A `Blueprint` resource.


## Set Blueprint Visibility

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"visibility": "<visibility>"}' \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>/set-visibility"
```

```python
# Python Client
client.blueprints.set_visibility('<blueprint-id>', '<visibility>')
```

> Response Example

```json
{
  "main_file_name": "singlehost-blueprint.yaml",
  "description": "This blueprint installs a simple web server on the manager VM using Cloudify's script plugin.\n",
  "tenant_name": "default_tenant",
  "created_at": "2017-04-19T10:56:06.267Z",
  "updated_at": "2017-04-19T10:56:06.267Z",
  "created_by": "admin",
  "private_resource": false,
  "visibility": "global",
  "plan": {
    ...
  },
  "id": "hello-world"
}
```

`PATCH "<manager-ip>/api/v3.1/blueprints/{blueprint-id}/set-visibility"`

Update the visibility of the blueprint. **Supported for Cloudify Manager 4.3 and above.**

### URI Parameters
* `blueprint-id`: The id of the blueprint to update.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`visibility` | string | Defines who can see the blueprint. (Required)

Valid values are `tenant` or `global`.

### Response
A `Blueprint` resource.

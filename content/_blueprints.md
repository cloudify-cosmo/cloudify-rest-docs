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
`labels` | list | A list of the deployment's labels. **Supported for Cloudify Manager 5.3 and above.**


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
# create blueprint from blueprint_archive_url
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>?application_file_name=<blueprint-id>.yaml&visibility=<visibility>&blueprint_archive_url=https://url/to/archive/master.zip&labels=<key1>=<val1>,<key2>=<val2>"

# create blueprint from uploaded archive
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>?application_file_name=<blueprint-id>.yaml&visibility=<visibility>&labels=<key1>=<val1>,<key2>=<val2>" -T <blueprint_archive>.tar.gz
```

```python
# Using CloudifyClient, uploading a zip file
client.blueprints.publish_archive(
    blueprint_id='<blueprint-id>',
    archive_location='https://url/to/archive/master.zip',
    blueprint_filename='<blueprint-id>.yaml',
    visibility='<visibility>',
    labels=[{'<key1>': '<val1>'}, ...]
)
# Using CloudifyClient, uploading a directory
# (will be tar'ed on the fly)
client.blueprints.upload(
    'path/to/blueprint.yaml',
    '<blueprint-id>',
    visibility='<visibility>',
    labels=[{'<key1>': '<val1>'}, ...]
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>'
headers = {'Tenant': '<manager-tenant>'}
querystring = {
    'application_file_name': '<blueprint-id>.yaml',
    'blueprint_archive_url': 'https://url/to/archive/master.zip',
    'visibility': '<visibility>',
    'labels': '<key1>=<val1>,<key2>=<val2>,...'
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
  "created_at": "2021-03-25T15:51:30.526Z",
  "updated_at": "2021-03-25T15:51:30.526Z",
  "created_by": "admin",
  "private_resource": false,
  "visibility": "tenant",
  "plan": {
    ...
  },
  "labels": [
    ...
  ],
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

## Validate Blueprint

> Request Example

```shell
# validate a blueprint at blueprint_archive_url
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>/validate?application_file_name=blueprint.yaml&visibility=<visibility>&blueprint_archive_url=https://url/to/archive/master.zip"

# validate a  blueprint from uploaded archive
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>/validate?application_file_name=blueprint.yaml&visibility=<visibility>" -T <blueprint_archive>.tar.gz
```

```python
# Using CloudifyClient
client.blueprints.validate(
    'path/to/blueprint.yaml',
    '<blueprint-id>',
    visibility='<visibility>'
)

# Using requests
url = 'http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>/validate'
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
```

`PUT "{manager-ip}/api/v3.1/blueprints/{blueprint-id}/validate?application_file_name={blueprint-id}.yaml&blueprint_archive_url=https://url/to/archive/master.zip&visibility=<visibility>"`

Validates a blueprint with Cloudify's manager.
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
`204 NO CONTENT` HTTP status and no body at all if uploaded blueprint and `blueprint-id` were valid.
`400 BAD REQUEST` HTTP status and a body containing description of the cause of the error otherwise.

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
url = 'http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>?force=false'
headers = {'Tenant': '<manager-tenant>'}
requests.delete(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
)
```

`DELETE "{manager-ip}/api/v3.1/blueprints/{blueprint-id}"`

Deletes a specific blueprint.

### URI Parameters
Property | Type | Description
--------- | ------- | -----------
`blueprint_id` | string | The id of the blueprint to delete.
`force` | bool | Delete the blueprint, even if there are blueprints that are currently using it. **Supported for Cloudify Manager 4.5.5 and above.**

### Response
No content - HTTP code 204.


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
  "created_at": "2021-03-25T15:51:30.526Z",
  "updated_at": "2021-03-25T15:51:30.526Z",
  "created_by": "admin",
  "private_resource": false,
  "visibility": "global",
  "plan": {
    ...
  },
  "labels": [
    ...
  ],
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
  "created_at": "2021-03-25T15:51:30.526Z",
  "updated_at": "2021-03-25T15:51:30.526Z",
  "created_by": "admin",
  "private_resource": false,
  "visibility": "global",
  "plan": {
    ...
  },
  "labels": [
    ...
  ],
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


## Update (add / delete) Blueprint Labels

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"labels": [{"<key1>": "<val1>"}, {"<key2>": "<val2>"}]}' \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>"
```

```python
# Python Client
client.blueprints.update(
blueprint_id='<deployment-id>', 
update_dict={'labels': [{'<key1>': '<val1>', '<key2>': '<val2>'}]}
)
```

> Response Example

```json
{
  "main_file_name": "singlehost-blueprint.yaml",
  "description": "This blueprint installs a simple web server on the manager VM using Cloudify's script plugin.\n",
  "tenant_name": "default_tenant",
  "created_at": "2021-03-25T15:51:30.526Z",
  "updated_at": "2021-03-25T16:04:20.496Z",
  "created_by": "admin",
  "private_resource": false,
  "visibility": "global",
  "plan": {
    ...
  },
  "labels": [
   {
      "key": "<key1>",
      "value": "<val1>",
      "created_at": "2021-03-25T16:04:20.486Z",
      "creator_id": 0
    },
    {
      "key": "<key2>",
      "value": "<val2>",
      "created_at": "2021-03-25T16:04:20.486Z",
      "creator_id": 0
    }
  ],
  "id": "hello-world"
}

```

`PATCH "<manager-ip>/api/v3.1/blueprints/{blueprint-id}"`

Update the blueprint's labels. **Supported for Cloudify Manager 5.3 and above.**

### URI Parameters
* `blueprint-id`: The id of the blueprint to update.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`labels` | list | A list of the new deployment's labels (required).


### Response
A `Blueprint` resource.


## Get all Blueprints' Labels' Keys

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/labels/blueprints"
```

```python
# Python Client
client.blueprints_labels.list_keys()
```

> Response Example

```json
{
  "metadata": {
    "pagination": {
      "total": 2,
      "size": 1000,
      "offset": 0
    }
  },
  "items": [
    "key1",
    "key2"
  ]
}

```

`GET "<manager-ip>/api/v3.1/labels/blueprints"`

Get all blueprints' labels' keys in the specified tenant. **Supported for Cloudify Manager 5.3 and above.**

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of all blueprints' labels' keys.


## Get All Blueprints' Labels' Values For a Specified Key

> Request Example

```shell
$ curl -X GET \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/labels/blueprints/<label-key>"
```

```python
# Python Client
client.blueprints_labels.list_key_values(label_key='<label-key>')
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
    "val1"
  ]
}

```

`GET "<manager-ip>/api/v3.1/labels/blueprints/<label-key>"`

Get all blueprints' labels' values for the specified key. **Supported for Cloudify Manager 5.3 and above.**

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of all blueprints' labels' values associated with the specified key.

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
`requirements` | dict | Description of the blueprint deploy requirements.
`updated_at` | datetime | The last time the blueprint was updated.
`labels` | list | A list of the deployment's labels.


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
    -F 'params={"blueprint_archive_url": "http://url/to/archive.zip", application_file_name": "<filename>.yaml", "visibility": "<visibility>"}' \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>"

# create blueprint from a .tgz archive, with additional parameters
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -F blueprint_archive=@<blueprint_archive>.tar.gz \
    -F 'params={"application_file_name": "<filename>.yaml", "visibility": "<visibility>", "labels": [{"key": "<label key>", "value": "<label value>"}]}' \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>"
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

`PUT "{manager-ip}/api/v3.1/blueprints/{blueprint-id}"`

Uploads a blueprint to Cloudify's manager.
The call expects a `multipart/form-data`-encoded request body, containing the fields `blueprint_archive` - a zip or tgz of the blueprint, and `params` - a JSON-encoded field containing blueprint metadata.
The "params" field may contain the keys `application_file_name`, `visibility`, `labels`, and `async_upload`.
It is also possible to upload a blueprint from a URL by specifying the URL in the `blueprint_archive_url` key in the `params` field.


### URI Parameters
* `blueprint-id`: The id of the uploaded blueprint.

### Request Body

The request body must be `multipart/form-data`.

Property | Type | Description
`blueprint_archive` | binary | The contents of a zip or tgz-compressed archive of the blueprint directory.
`params` | string | JSON-encoded object containing additional parameters. This field may contain the other parameters listed below.
`blueprint_archive_url` | string | A URL the blueprint to be uploaded should be downloaded from by the manager. May be provided as a key in the `params` field, or as a field in the querystring.
`application_file_name` | string | The main blueprint file name in the blueprint's archive. May be provided as a key in the `params` field, or as a field in the querystring.
`visibility` | string | Optional parameter, defines who can see the blueprint (default: tenant). May be provided as a key in the `params` field.
`async_upload` | boolean | Optional parameter, setting it to True means the REST service won't wait for the upload workflow to complete, allowing a batch upload (default: False). May be provided as a key in the `params` field. **Supported for Cloudify Manager 5.2 and above.**
`labels` | list | Labels to apply to the blueprint - a list of objects containing the keys `key` and `value`. May be provided as a key in the `params` field.

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
    -F 'params={"blueprint_archive_url": "http://url/to/archive.zip", application_file_name": "<filename>.yaml", "visibility": "<visibility>"}' \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>/validate"

# validate a  blueprint from uploaded archive
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -F blueprint_archive=@<blueprint_archive>.tar.gz \
    -F 'params={"application_file_name": "<filename>.yaml", "visibility": "<visibility>"}' \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>"
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

`PUT "{manager-ip}/api/v3.1/blueprints/{blueprint-id}/validate"`

Validates a blueprint with Cloudify's manager.
The call expects an "application/octet-stream" content type where the content is a zip/tar.gz/bz2 archive.
It is possible to upload a blueprint from a URL by specifying the URL in the `blueprint_archive_url` request body property.


### URI Parameters
* `blueprint-id`: The id of the uploaded blueprint.

### Request Body
The request body is the same as in the Blueprint Upload endpoint.

### Response
An `Execution` resource, representing the `upload_blueprint` workflow execution that will validate the blueprint.
Users should follow that execution to completion, and examine its status, error, and logs, to see if the blueprint
validated successfully, and if not - what are the invalid parts.

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


## Set Blueprint's Icon

> Request Example

```shell
# Update blueprint's icon with <icon_image>.png
$ curl -X PATCH \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -T <icon_image>.png \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>/icon"

# Remove blueprint's icon
$ curl -X PATCH \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/blueprints/<blueprint-id>/icon"
```

```python
# Python Client: Update blueprint'e icon with PNG file located at <icon_path>
client.blueprints.upload_icon('<blueprint-id>', '<icon_path>')


# Python Client: Remove blueprint'e icon
client.blueprints.remove_icon('<blueprint-id>')
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

`PATCH "<manager-ip>/api/v3.1/blueprints/{blueprint-id}/icon"`

Set blueprint's icon if icon file is uploaded along the request or remove it otherwise.
**Supported for Cloudify Manager 6.3 and above.**

### URI Parameters
* `blueprint-id`: The id of the blueprint to update.

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

Update the blueprint's labels.

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

Get all blueprints' labels' keys in the specified tenant.

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

Get all blueprints' labels' values for the specified key.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of all blueprints' labels' values associated with the specified key.

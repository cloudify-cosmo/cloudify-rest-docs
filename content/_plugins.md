# Plugins

## The Plugin Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`archive_name` | string | The plugin archive file name.
`distribution_release` | string | The OS distribution release name the plugin was compiled on. 'None' in-case the plugin is cross platform.
`distribution_version` | string | The OS distribution version the plugin was compiled on. 'None' in-case the plugin is cross platform.
`distribution` | string | The OS distribution the plugin was compiled on. 'None' in-case the plugin is cross platform.
`excluded_wheels` | list | a list of wheels that were excluded from the plugin package.
`id` | string | The ID assigned to the plugin upon upload.
`package_name` | string | The python package name.
`package_source` | string | The python package source, i.e git, pip etc.
`package_version` | string | The python package version.
`supported_platform` | string | The supported platform for the plugin package, 'any' if the plugin is compatible with all platforms.
`supported_py_versions` | list | a list of python platforms supported by the plugin.
`tenant_name` | string | The name of the tenant that owns the plugin.
`title` | string | The plugin title used e.g. in UI topology view.
`uploaded_at` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The time and date the plugin was uploaded on to the Cloudify-Manager.
`wheels` | list | A list of wheels contained in the plugin package.


## List Plugins

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/plugins?_include=id"
```

```python
# Using CloudifyClient
plugins = client.plugins.list(_include=['id'])
for plugin in plugins:
    print plugin

# Using requests
url = 'http://<manager-ip>/api/v3.1/plugins'
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
      "id": "ecea687a-b7dc-4d02-909d-0400aa23df27"
    },
    {
      "id": "f10a4970-6cfa-4b24-9cab-f85db93204e0"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 2,
      "offset": 0,
      "size": 0
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/plugins"`

Lists all plugins.

### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Plugin` resources.
`metadata` | dict | Metadata relevant to the list response.


## Get Plugin

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/plugins/<plugin-id>?_include=id"
```

```python
# Using CloudifyClient
client.plugins.get(plugin_id='<plugin-id'>', _include=['id'])

# Using requests
url = 'http://<manager-ip>/api/v3.1/plugins/<plugin-id>'
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
  "id": "ecea687a-b7dc-4d02-909d-0400aa23df27"
}
```

`GET "{manager-ip}/api/v3.1/plugins/{plugin-id}"`

Gets a plugin.

### URI Parameters
* `plugin-id`: The id of the plugin.

### Response
A `Plugin` resource.


## Delete Plugin

> Request Example

```shell
$ curl -X DELETE \
    --header "Content-Type: application/json" \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"force": false}' \
    "http://<manager-ip>/api/v3.1/plugins/<plugin-id>?_include=id"
```

```python
# Using CloudifyClient
client.plugins.delete(plugin_id='<plugin-id>')

# Using requests
url = 'http://<manager-ip>/api/v3.1/plugins/<plugin-id>'
headers = {
    'Content-Type': 'application/json',
    'Tenant': '<manager-tenant>',
}
querystring = {'_include': 'id'}
payload = {'force': False}
response = requests.delete(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
    json=payload,
)
response.json()
```

`DELETE "{manager-ip}/api/v3.1/plugins/{plugin-id}"`

Deletes a plugin from the Cloudify-Manager.

### URI Parameters
* `plugin-id`: The id of the plugin.

### Request Body
Property | Default | Description
---------|---------|-------------
`force`  |  false  | Specifies whether to force plugin deletion even if there are deployments that currently use it.

### Response
The deleted `Plugin` resource.


## Upload Plugin

> Request Example

```shell
$ curl -X POST \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/plugins?plugin_archive_url=http://url/to/archive.wgn&title=<title>&_include=id&visibility=<visibility>"
```

```python
# Using CloudifyClient
client.plugins.upload(plugin_path='http://url/to/archive.wgn',
                      plugin_title='My Plugin',
                      visibility='<visibility>')

# Using requests
url = 'http://<manager-ip>/api/v3.1/plugins'
headers = {'Tenant': '<manager-tenant>'}
querystring = {
    'plugin_archive_url': 'http://url/to/archive.wgn',
    'title': 'My Plugin',
    '_include': 'id',
    'visibility': '<visibility>'
}
response = requests.post(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
response.json()
```

> Example Response

```json
{
  "id": "d80542f4-ec0c-4438-8a29-54cb9a904114"
}
```

`POST "{manager-ip}/api/v3.1/plugins"`

Upload a plugin

### Request Body
Property | Type | Description
--------- | ------- | -----------
`plugin_path` | string | The plugin archive local path.
`plugin_archive_url` | string | A URL of the plugin archive to be uploaded. The plugin will be downloaded by the manager.
`title` | string | The plugin title, used e.g. in UI topology view (this is an optional parameter).
`visibility` | string | Optional parameter, defines who can see the plugin (default: tenant). **Supported for Cloudify Manager 4.3 and above.**

Valid visibility values are:

* `private`: The resource is visible to the user that created the resource, the tenant’s managers and the system’s admins.
* `tenant`: The resource is visible to all users in the current tenant. (Default value)
* `global`: The resource is visible to all users in all tenants across the manager.

### Response
The new uploaded `Plugin` resource.


## Download Plugin

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/plugins/<plugin-id>/archive" > <plugin-archive-filename>.wgn
```

```python
# Using CloudifyClient
client.plugins.download(
   plugin_id='<plugin-id>',
   output_file='<plugin-archive-filename>',
)

# Using Requests
url = 'http://<manager-ip>/api/v3.1/plugins/<plugin-id>/archive'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
)
with open('<plugin-archive-filename>.wgn', 'wb') as plugin_archive:
    plugin_archive.write(response.content)
```

`GET "{manager-ip}/api/v3.1/plugins/{plugin-id}/archive"`

Downloads a plugin.

### URI Parameters
* `plugin-id`: The id of the plugin.

### Response
The requested plugin archive.


## Set Global Plugin

> Request Example

```shell
$ curl -X PATCH -H "Content-Type: application/json" -H "tenant: <tenant-name>"
    -u user:password "http://<manager-ip>/api/v3.1/plugins/<plugin-id>/set-global"
```

```python
# Python Client
client.plugins.set_global(<plugin-id>)
```

> Response Example

```json
{
  "distribution_release": "core",
  "supported_py_versions": [
    "py27"
  ],
  "uploaded_at": "2017-10-19T14:19:39.727Z",
  "archive_name": "cloudify_openstack_plugin-2.0.1-py27-none-linux_x86_64-centos-Core.wgn",
  "package_name": "cloudify-openstack-plugin",
  "distribution_version": "7.0.1406",
  "tenant_name": "default_tenant",
  "excluded_wheels": [

  ],
  "created_by": "admin",
  "distribution": "centos",
  "package_source": "https://github.com/cloudify-cosmo/cloudify-openstack-plugin/archive/master.tar.gz",
  "private_resource": false,
  "visibility": "global",
  "supported_platform": "linux_x86_64",
  "package_version": "2.0.1",
  "wheels": [
    "keystoneauth1-2.19.0-py2.py3-none-any.whl",
    "python_novaclient-7.0.0-py2.py3-none-any.whl",
     ...
  ],
  "id": "c7f6757e-b48d-4c26-ab91-cfc8c1e4851c"
}
```

`PATCH "{manager-ip}/api/v3.1/plugins/{plugin-id}/set-global"`

Set the plugin's visibility to global.
Will be deprecated soon. For Cloudify Manager 4.3 and above, use 'set-visibility'.

### URI Parameters
* `plugin-id`: The id of the plugin to update.


### Response
A `Plugin` resource.


## Set Plugin Visibility

> Request Example

```shell
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"visibility": "<visibility>"}' \
    "http://<manager-ip>/api/v3.1/plugins/<plugin-id>/set-visibility"
```

```python
# Python Client
client.plugins.set_visibility('<plugin-id>', '<visibility>')
```

> Response Example

```json
{
  "distribution_release": "core",
  "supported_py_versions": [
    "py27"
  ],
  "uploaded_at": "2017-10-19T14:19:39.727Z",
  "archive_name": "cloudify_openstack_plugin-2.0.1-py27-none-linux_x86_64-centos-Core.wgn",
  "package_name": "cloudify-openstack-plugin",
  "distribution_version": "7.0.1406",
  "tenant_name": "default_tenant",
  "excluded_wheels": [

  ],
  "created_by": "admin",
  "distribution": "centos",
  "package_source": "https://github.com/cloudify-cosmo/cloudify-openstack-plugin/archive/master.tar.gz",
  "private_resource": false,
  "visibility": "global",
  "supported_platform": "linux_x86_64",
  "package_version": "2.0.1",
  "wheels": [
    "keystoneauth1-2.19.0-py2.py3-none-any.whl",
    "python_novaclient-7.0.0-py2.py3-none-any.whl",
     ...
  ],
  "id": "c7f6757e-b48d-4c26-ab91-cfc8c1e4851c"
}
```

`PATCH "<manager-ip>/api/v3.1/plugins/{plugin-id}/set-visibility"`

Update the visibility of the plugin. **Supported for Cloudify Manager 4.3 and above.**

### URI Parameters
* `plugin-id`: The id of the plugin to update.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`visibility` | string | Defines who can see the plugin. (Required)

Valid values are `tenant` or `global`.

### Response
A `Plugin` resource.

## The Plugins Update Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | A unique identifier for the plugins update.
`state` | string | The state of this update ("updating", "executing_workflow", "finalizing", "successful", "failed", or "no_changes_required").
`blueprint_id` | string | The id of the blueprint that its deployments will get their plugins updated.
`temp_blueprint_id` | string | The id of the temporary internal blueprint created for the purpose of this plugins update.
`execution_id` | string | The id of the plugins update execution.
`deployments_to_update` | list | A list of deployment IDs that are updated in this plugins update.
`forced` | bool | Whether or not this plugins update was executed regardless of other active/failed plugins updates.
`created_at` | datetime | The time when the plugins update was started.
`created_by` | string | The name of the user that started the plugins update.
`tenant_name` | string | The name of the tenant the plugins update belongs to.
`visibility` | string | The visibility of the plugins update.
`private_resource` | boolean | Is the plugins update private.
`resource_availability` | string | The availability of the plugins update.

## Update Plugins

> Request Example

```shell
$ curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"force": "<force>"}' \
    "<manager-ip>/api/v3.1/plugins-updates/<blueprint-id>/update/initiate"
```

```python
# Python Client
client.plugins_update.update_plugins(blueprint_id="<blueprint_id>", force="<force>")
```

> Response Example

```json
{
 "forced": false,
 "blueprint_id": "baddd86fb-864b-483e-a98a-d53e2b728ccd",
 "tenant_name": "default_tenant",
 "created_at": "2019-07-10T07:24:40.520Z",
 "visibility": "tenant",
 "private_resource": false,
 "state": "executing_workflow",
 "temp_blueprint_id": "bbf4b172-3b21-460c-aed8-4f55b55f3b4f",
 "created_by": "admin",
 "deployments_to_update": [
    "dd7b03fb3-8f92-404c-8ddd-d81bd6a2bc9b"
 ],
 "resource_availability": "tenant",
 "id": "ce63a9d6-726b-4ff2-a267-f953af5dc32d",
 "execution_id": "8ec77e89-b418-4472-9b44-fe9d7a7fe163"
}

```

`PUT "<manager-ip>/api/v3.1/plugins-updates/<blueprint-id>/update/initiate"`

Update the plugins for that blueprint's deployments. **Supported for Cloudify Manager 5.0.0 and above.**

### URI Parameters
* `blueprint-id`: The id of the blueprint that its deployments will get their plugins updated.

### Request Body

Property | Type | Description
--------- | ------- | -----------
`force` | boolean | Specifies whether to force the plugin update regardless of other active/failed plugins updates state.


### Response
A `Plugins Update` resource.

## Get Plugins-Update

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/plugins-updates/<plugins-update-id>?_include=id"
```

```python
# Using CloudifyClient
plugins_update = client.plugins_update.get(plugins_update_id=plugins_update_id)
```

> Response Example

```json
{
 "forced": false,
 "blueprint_id": "baddd86fb-864b-483e-a98a-d53e2b728ccd",
 "tenant_name": "default_tenant",
 "created_at": "2019-07-10T07:24:40.520Z",
 "visibility": "tenant",
 "private_resource": false,
 "state": "executing_workflow",
 "temp_blueprint_id": "bbf4b172-3b21-460c-aed8-4f55b55f3b4f",
 "created_by": "admin",
 "deployments_to_update": [
    "dd7b03fb3-8f92-404c-8ddd-d81bd6a2bc9b"
 ],
 "resource_availability": "tenant",
 "id": "ce63a9d6-726b-4ff2-a267-f953af5dc32d",
 "execution_id": "8ec77e89-b418-4472-9b44-fe9d7a7fe163"
}

```

`GET "<manager-ip>/api/v3.1/plugins-updates/<plugins-update-id>"`

Get a plugins update. **Supported for Cloudify Manager 5.0.0 and above.**

### Response
A `Plugins Update` resource.

## List Plugins Updates

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/plugins-updates?_include=id"
```

```python
# Using CloudifyClient
plugins_updates = client.plugins_update.list(
        sort=sort_by,
        is_descending=descending,
        _all_tenants=all_tenants,
        _search=search,
        _offset=pagination_offset,
        _size=pagination_size,
        plugins_update_id=plugins_update_id
    )
```

> Response Example

```json
{
  "items": [
    {
      "id": "update1",
      ...
    },
    {
      "id": "update2",
      ...
    },
    {
      "id": "update3",
      ...
    }
  ],
  "metadata": {
    "pagination": {
      "total": 3,
      "offset": 0,
      "size": 0
    }
  }
}
```

`GET "{manager-ip}/api/v3.1/plugins-updates"`

Lists the plugins updates. **Supported for Cloudify Manager 5.0.0 and above.**

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Plugins Update` resources.

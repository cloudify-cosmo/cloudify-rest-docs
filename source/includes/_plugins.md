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
    "http://<manager-ip>/api/v3.1/plugins?plugin_archive_url=http://url/to/archive.wgn&_include=id"
```

```python
# Using CloudifyClient
client.plugins.upload(plugin_path='http://url/to/archive.wgn')

# Using requests
url = 'http://<manager-ip>/api/v3.1/plugins'
headers = {'Tenant': '<manager-tenant>'}
querystring = {
    'plugin_archive_url': 'http://url/to/archive.wgn',
    '_include': 'id',
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

Upload a plugins

### Request Body
Property | Type | Description
--------- | ------- | -----------
`plugin_path` | string | The plugin archive local path.
`plugin_archive_url` | string | A URL of the plugin archive to be uploaded. The plugin will be downloaded by the manager.

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
  "resource_availability": "global",
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

Set the plugin's availability to global.

### URI Parameters
* `plugin-id`: The id of the plugin to update.


### Response
A `Plugin` resource.

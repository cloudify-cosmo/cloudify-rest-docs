# Plugins

## The Plugin Resource

> `Note`

```python
# include this code when using cloudify REST client-
from cloudify_rest_client import CloudifyClient
client = CloudifyClient('<manager-ip>')

# import the requests module when using Requests in python-
import requests
```

```html
CloudifyJS, the JavaScript client, is available at https://github.com/cloudify-cosmo/cloudify-js
```

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | The ID assigned to the plugin upon upload.
`package_name` | string | The python package name.
`archive_name` | string | The plugin archive file name.
`package_source` | string | The python package source, i.e git, pip etc.
`package_version` | string | The python package version.
`supported_platform` | string | The supported platform for the plugin package, 'any' if the plugin is compatible with all platforms.
`distribution` | string | The OS distribution the plugin was compiled on. 'None' in-case the plugin is cross platform.
`distribution_version` | string | The OS distribution version the plugin was compiled on. 'None' in-case the plugin is cross platform.
`distribution_release` | string | The OS distribution release name the plugin was compiled on. 'None' in-case the plugin is cross platform.
`wheels` | list | A list of wheels contained in the plugin package.
`excluded_wheels` | list | a list of wheels that were excluded from the plugin package.
`supported_py_versions` | list | a list of python platforms supported by the plugin.
`uploaded_at` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The time and date the plugin was uploaded on to the Cloudify-Manager.


## Get Plugin

> Request Example

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/plugins/0e56d421-ddf9-4fc3-ade5-95ba1de96366"
```

```python
# Python Client-
print client.plugins.get(plugin_id='0e56d421-ddf9-4fc3-ade5-95ba1de96366')

# Python Requests-
url = "http://<manager-ip>/api/v2.1/plugins/0e56d421-ddf9-4fc3-ade5-95ba1de96366"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/plugins/0e56d421-ddf9-4fc3-ade5-95ba1de96366",
  "method": "GET",
  "headers": {
    "content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
<script>
    var client = new window.CloudifyClient({'endpoint': 'http://<manager-ip>/api/v2.1'});
    client.plugins.get( { plugin_id_id : <plugin-id> } );
</script>
```

> Response Example

```json
{
	"archive_name":"cloudify_script_plugin-1.2-py27-none-any-none-none.wgn",
	"package_name":"cloudify-script-plugin",
	"package_version":"1.2",
	"supported_platform":"any",
	"package_source":"cloudify-script-plugin==1.2",
	"distribution":null,
	"distribution_version":null,
	"distribution_release":null,
	"supported_py_versions":["py27"],
	"uploaded_at":"2015-12-06 11:32:46.799188",
	"id":"0e56d421-ddf9-4fc3-ade5-95ba1de96366",
	"wheels":["bottle-0.12.7-py2-none-any.whl",
			  "requests-2.7.0-py2.py3-none-any.whl",
			  "proxy_tools-0.1.0-py2-none-any.whl",
			  "cloudify_plugins_common-3.2.1-py2-none-any.whl"],
    "excluded_wheels":[]
}
```

`GET "{manager-ip}/api/v2.1/plugins/{plugin-id}"`

Gets a plugin.

### URI Parameters
* `plugin-id`: The id of the plugin.

### Response
A `Plugin` resource.


## Delete Plugin

> Request Example

```shell
$ curl -X DELETE "http://<manager-ip>/api/v2.1/plugins/0e56d421-ddf9-4fc3-ade5-95ba1de96366"
```

```python
# Python Client-
client.plugins.delete(plugin_id='<plugin-id>')

# Python Requests-
url = "http://<manager-ip>/api/v2.1/plugins/<plugin-id>"
headers = {'content-type': "application/json"}
response = requests.request("DELETE", url, headers=headers)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/plugins/<plugin-id>",
  "method": "DELETE",
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
<script>
    var client = new window.CloudifyClient({'endpoint': 'http://<manager-ip>/api/v2.1'});
    client.plugins.delete( { plugin_id_id : <plugin-id> } );
</script>
```

`DELETE "{manager-ip}/api/v2.1/plugins/{plugin-id}"`

Deletes a plugin from the Cloudify-Manager.

### URI Parameters
* `plugin-id`: The id of the plugin.

### Response
The deleted `Plugin` resource.


## List Plugins

> Request Example

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/plugins"
```

```python
# Python Client-
plugins = client.plugins.list()
for plugin in plugins:
    print plugin

# Python Requests-
url = "http://<manager-ip>/api/v2.1/plugins"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/plugins",
  "method": "GET",
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
<script>
    var client = new window.CloudifyClient({'endpoint': 'http://<manager-ip>/api/v2.1'});
    client.plugins.list(function(err, response, body){
                var plugins = body.items;
    });
</script>
```

`GET "{manager-ip}/api/v2.1/plugins"`

Lists all plugins.

### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Plugin` resources.
`metadata` | dict | Metadata relevant to the list response.


## Upload Plugin

> Request Example

```shell
$ curl -X PUT "http://<manager-ip>/api/v2.1/plugins/<plugin-id>?plugin_archive_url=https://url/to/archive.zip"
```

```python
# Python Client-
client.plugins.upload(plugin_path='https://url/to/archive.zip')

# Python Requests-
url = "http://<manager-ip>/api/v2.1/plugins/<plugin-ip>"
querystring = {"plugin_archive_url":"https://url/to/archive.zip"}
headers = {'content-type': "application/json"}
response = requests.request("PUT", url, headers=headers, params=querystring)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/plugins/<plugin-id>?plugin_archive_url=
         https%3A%2F%2Furl%2Fto%2Farchive.zip",
  "method": "PUT",
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
<script>
    var client = new window.CloudifyClient({'endpoint': 'http://<manager-ip>/api/v2.1'});
    client.plugins.upload('https://url/to/archive.zip');
</script>
```

`POST "{manager-ip}/api/v2.1/plugins/{plugin-id}"`

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
$ curl -X GET "http://<manager-ip>/api/v2.1/plugins/<plugin-id>/archive"
```

```python
# Python Client-
client.plugins.download(plugin_id='<plugin-id>')

# Pyhton Requests-
url = "http://<manager-ip>/api/v2.1/plugins/<plugin-id>/archive"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/plugins/<plugin-id>/archive",
  "method": "GET",
  "headers": {
    "content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
<script>
    var client = new window.CloudifyClient({'endpoint': 'http://<manager-ip>/api/v2.1'});
    client.plugins.download('<plugin-id>');
</script>
```

`GET "{manager-ip}/api/v2.1/plugins/{plugin-id}/archive"`

Downloads a plugin.

### URI Parameters
* `plugin-id`: The id of the plugin.

### Response
The requested plugin archive.

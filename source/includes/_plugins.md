# Managed-Plugins

## The Managed-Plugin Resource

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


## Get Managed-Plugin

> Request Example

```shell
$ curl -XGET http://localhost/api/v2/plugins/0e56d421-ddf9-4fc3-ade5-95ba1de96366
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

`GET /api/v2/plugin/{managed-plugin-id}`

Gets a managed-plugin.

### URI Parameters
* managed-plugin-id: The id of the managed-plugin.

### Response
A `Plugin` resource.


## Delete Managed-Plugin
`DELETE /api/v2/plugin/{managed-plugin-id}`

Deletes a managed-plugin from the Cloudify-Manager.

### URI Parameters
* managed-plugin-id: The id of the managed-plugin.

### Response
The deleted `Plugin` resource.


## List Managed-Plugins
`GET /api/v2/plugins`

Lists all managed-plugins.

### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Plugin` resources.
`metadata` | dict | Metadata relevant to the list response.


## Upload Managed-Plugin
`POST /api/v2/plugins`

Upload a managed-plugins

### Request Body
Property | Type | Description
--------- | ------- | -----------
`plugin_path` | string | The plugin archive local path.
`plugin_archive_url` | string | A URL of the plugin archive to be uploaded. The plugin will be downloaded by the manager.

### Response
The new uploaded `Plugin` resource.


## Download Managed-Plugin
`GET /api/v2/plugins/{managed-plugin-id}/archive`

Downloads a managed-plugin.

### URI Parameters
* managed-plugin-id: The id of the managed-plugin.

### Response
The requested plugin archive.

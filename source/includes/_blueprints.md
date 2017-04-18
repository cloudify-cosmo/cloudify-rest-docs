# Blueprints

## The Blueprint Resource

> `Note`

```python
# include this code when using cloudify python client-
from cloudify_rest_client import CloudifyClient
client = CloudifyClient('<manager-ip>')

# include this code when using python requests-
import requests
```

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | A unique identifier for the blueprint.
`description` | string | The blueprint's description.
`main_file_name` | string | The blueprint's main file name.
`plan` | dict | The parsed result of the blueprint.
`created_at` | datetime | The time the blueprint was uploaded to the manager.
`updated_at` | datetime | The last time the blueprint was updated.


## Get Blueprint

> Request Example

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/blueprints?id=hello-world"
```

```python
# Python Client-
client.blueprints.get(blueprint_id='hello-world')

# Python Requests-
querystring = {"id":"hello-world"}
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
```

> Response Example

```json
{
  "updated_at": "2015-11-08 11:11:36.039194",
  "created_at": "2015-11-08 11:11:36.039194",
  "main_file_name": "singlehost-blueprint.yaml",
  "description": "Deploys a simple Python HTTP server on an existing machine.",
  "id": "hello-world",
  "plan": {
    "relationships": {},
    "inputs": {},
    "deployment_plugins_to_install": [],
    "policy_types": {},
    "outputs": {},
    "version": {},
    "workflow_plugins_to_install": {},
    "groups": {},
    "workflows": {},
    "nodes": [],
    "policy_triggers": {}
  }
}
```

`GET "{manager-ip}/api/v2.1/blueprints?id={blueprint-id}"`

Gets a specific blueprint.

### URI Parameters
* `blueprint-id`: The id of the blueprint to retrieve.

### Response
A `Blueprint` resource.


## Upload Blueprint

> Request Example

```shell
$ curl -X PUT "http://<manager-ip>/api/v2.1/blueprints/<blueprint-id>?application_file_name=<blueprint-id>.yaml&
blueprint_archive_url=https://url/to/archive/master.zip"
```

```python
# Python Client-
client.blueprints._upload(archive_location='https://url/to/archive/master.zip',
                          blueprint_id='<blueprint-id>',application_file_name='<blueprint-id>.yaml')

# Python Requests-
url = "http://<manager-ip>/api/v2.1/blueprints/<blueprint-id>"
querystring = {"application_file_name":"<blueprint-id>.yaml",
               "blueprint_archive_url":"https://url/to/archive/master.zip"}
headers = {'content-type': "application/json"}
response = requests.request("PUT", url, headers=headers, params=querystring)
print(response.text)
```

`PUT "{manager-ip}/api/v2.1/blueprints/{blueprint-id}?application_file_name={blueprint-id}.yaml&
blueprint_archive_url=https://url/to/archive/master.zip"`

Uploads a blueprint to Cloudify's manager.
The call expects an "application/octet-stream" content type where the content is a zip/tar.gz/bz2 archive.
It is possible to upload a blueprint from a URL by specifying the URL in the `blueprint_archive_url` request body property.


### URI Parameters
* `blueprint-id`: The id of the uploaded blueprint.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`application_file_name` | string | The main blueprint file name in the blueprint's archive.
`blueprint_archive_url` | string | A URL the blueprint to be uploaded should be downloaded from by the manager.

### Response
A `Blueprint` resource.

## List Blueprints

> Request Example

```shell
$ curl -X GET "<manager-ip>/api/v2.1/blueprints?_include=id,created_at"
```

```python
# Python Client-
blueprints = client.blueprints.list(_include=['id','created_at'])
for blueprint in blueprints:
  print blueprint

# Python Requests-
url = "http://<manager-ip>/api/v2.1/blueprints"
querystring = {"_include":"id,created_at"}
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
```

`GET "{manager-ip}/api/v2.1/blueprints"`

Lists all blueprints.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Blueprint` resources.


## Delete Blueprint

> Request Example

```shell
$ curl -X DELETE "<manager-ip>/blueprints/<blueprint-id>"
```

```python
# Python Client-
client.blueprints.delete(blueprint_id='<blueprint-id>')

# Python Requests-
url = "http://<manager-ip>/blueprints/<blueprint-id>"
headers = {'content-type': "application/json"}
response = requests.request("DELETE", url, headers=headers)
print(response.text)
```

`DELETE "{manager-ip}/api/v2.1/blueprints/{blueprint-id}"`

Deletes a specific blueprint.


### URI Parameters
* `blueprint-id`: The id of the blueprint to delete.

### Response
A `Blueprint` resource.


## Download Blueprint
Downloads a specific blueprint as an archive.

> Request Example

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/blueprints/<blueprint-id>/archive"
```

```python
# Python Client-
client.blueprints.download(blueprint_id='<blueprint-id>')

# Python Requests-
url = "http://<manager-ip>/api/v2.1/blueprints/<blueprint-id>/archive"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
```

`GET "{manager-ip}/api/v2.1/blueprints/{blueprint-id}/archive"`

### URI Parameters
* `blueprint-id`: The id of the blueprint to download.

### Response
The blueprint as an archive using an `application/octet-stream` content type.

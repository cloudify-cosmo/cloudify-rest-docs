# Snapshots

## The Snapshot Resource

> `Note`

```python
# include this code when using cloudify python client-
from cloudify_rest_client import CloudifyClient
client = CloudifyClient('<manager-ip>')

# include this code when using python requests-
import requests
```

```html
CloudifyJS, the JavaScript client, is available at https://github.com/cloudify-cosmo/cloudify-js
```

### Attributes:


Attribute | Type | Description
--------- | ------- | -------
`id` | string | A unique identifier of the snapshot.
`created_at` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The time the snapshot was uploaded to or created on the manager.
`status` | string | Status of the snapshot. One of created/failed/uploading/uploaded.
`error` | string | Message of an error if snapshot creation failed.

## List Snapshots

> Request Example

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/snapshots"
```

```python
# Python Client-
snapshots = client.snapshots.list()
for snapshot in snapshots:
    print snapshot

# Python Requests-
url = "http://<manager-ip>/api/v2.1/snapshots"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/snapshots",
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
    client.snapshots.list(function(err, response, body){
              var snapshots = body.items;
  });
</script>
```

> Response Example

```json
{
    "items": [
        {
            "created_at": "2015-12-04 13:34:45.080009",
            "error": "",
            "id": "snapshot1",
            "status": "created"
        },
        {
            "created_at": "2015-12-04 13:35:04.972249",
            "error": "",
            "id": "snapshot2",
            "status": "created"
        }
    ],
    "metadata": {
        "pagination": {
            "offset": 0,
            "size": 10000,
            "total": 2
        }
    }
}
```

`GET "{manager-ip}/api/v2.1/snapshots"`

Lists all snapshots.


### Response

Attribute | Type | Description
--------- | ------- | -------
`items` | list | A list of [Snapshot](#the-snapshot-resource) resources.


## Create Snapshot

> Requests Example

```shell
$ curl -X PUT "http://<manager-ip>/api/v2.1/snapshots/<snapshot-id>"
```

```python
# Python Client-
client.snapshots.create(snapshot_id='<snapshot-id>')

# Python Requests-
url = "http://<manager-ip>/api/v2.1/snapshots/<snapshot-id>"
headers = {'content-type': "application/json"}
response = requests.request("PUT", url, headers=headers)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/snapshots/<snapshot-id>",
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
    client.snapshots.create('<snapshot-id>');
</script>
```

`PUT "{manager-ip}/api/v2.1/snapshots/{snapshot-id}"`

Creates a new snapshot.

### URI Parameters
* `snapshot-id`: The id of the new snapshot.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`include_metrics` | string | Specifies whether metrics stored in InfluxDB should be included in the created snapshot. It defaults to false.
`include_credentials` | string | Specifies whether agent SSH keys (including those specified in uploaded blueprints) should be included in the created snapshot. It defaults to false.

### Response
An [Execution](#the-execution-resource) resource representing the create snapshot workflow execution.


## Delete Snapshot

> Requests Example

```shell
$ curl -X DELETE "http://<manager-ip>/api/v2.1/snapshots/<snapshot-id>"
```

```python
# Python Client-
client.snapshots.delete(snapshot_id='<snapshot-id>')

# Python Requests-
url = "http://<manager-ip>/api/v2.1/snapshots/<snapshot-id>"
headers = {'content-type': "application/json"}
response = requests.request("DELETE", url, headers=headers)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/snapshots/<snapshot-id>",
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
    client.snapshots.delete('<snapshot-id>');
</script>
```

`DELETE "{manager-ip}/api/v2.1/snapshots/{snapshot-id}"`

Deletes an existing snapshot.

### URI Parameters
* `snapshot-id`: The id of the snapshot to be deleted.

### Response
An empty [Snapshot](#the-snapshot-resource) resource, with one non-empty field (its id).

## Restore Snapshot
`POST "{manager-ip}/api/v2.1/snapshots/{snapshot-id}/restore"`

Restores the specified snapshot on the manager.

### URI Parameters
* `snapshot-id`: The id of the snapshot to be restored.

### Request Body
Property | Default | Description
---------|---------|-------------
`force`  |  false  | Specifies whether to force restoring the snapshot on a manager that already contains blueprints/deployments.
`recreate_deployments_envs` | true | Specifies whether deployment environments should be created for restored deployments.

### Response
An [Execution](#the-execution-resource) resource representing the restore snapshot workflow execution.


## Download Snapshot
`GET "{manager-ip}/api/v2.1/snapshots/{snapshot-id}/archive"`

Downloads an existing snapshot.

### URI Parameters
* `snapshot-id`: The id of the snapshot to be downloaded.

### Response
A streamed response (content type `application/octet-stream`), which is a zip archive containing the snapshot data.

## Upload Snapshot
`PUT "{manager-ip}/api/v2.1/snapshots/{snapshot-id}/archive"`

Uploads a snapshot to the Cloudify Manager.
The call expects a `application/octet-stream` content type where the content is a zip archive.
It is possible to upload a snapshot from a URL by specifying the URL in the `snapshot_archive_url` request body property.

### URI Parameters
* `snapshot-id`: The id of the snapshot to be uploaded.

### Request Body
Property | Type | Description
---------|---------|-------------
`snapshot_archive_url` | string | Optional parameter specifying a url to a snapshot that will be uploaded to the manager.

### Response
A [Snapshot](#the-snapshot-resource) resource.

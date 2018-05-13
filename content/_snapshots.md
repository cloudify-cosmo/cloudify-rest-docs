# Snapshots

## The Snapshot Resource

### Attributes:


Attribute | Type | Description
--------- | ------- | -------
`id` | string | A unique identifier of the snapshot.
`created_at` | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | The time the snapshot was uploaded to or created on the manager.
`status` | string | Status of the snapshot. One of created/failed/uploading/uploaded.
`error` | string | Message of an error if snapshot creation failed.

## List Snapshots
`GET /api/v2/snapshots`

Lists all snapshots.

> Request Example

```shell
$ curl -XGET http://localhost/api/v2/snapshots
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

### Response

Attribute | Type | Description
--------- | ------- | -------
`items` | list | A list of [Snapshot](#the-snapshot-resource) resources.


## Create Snapshot
`PUT /api/v2/snapshots/{snapshot-id}`

Creates a new snapshot.

### URI Parameters
* snapshot-id: The id of the new snapshot.

### Request Body
Property | Type | Description
--------- | ------- | -----------
`include_metrics` | string | Specifies whether metrics stored in InfluxDB should be included in the created snapshot. It defaults to false.
`include_credentials` | string | Specifies whether agent SSH keys (including those specified in uploaded blueprints) should be included in the created snapshot. It defaults to false.

### Response
An [Execution](#the-execution-resource) resource representing the create snapshot workflow execution.


## Delete Snapshot
`DELETE /api/v2/snapshots/{snapshot-id}`

Deletes an existing snapshot.

### URI Parameters
* snapshot-id: The id of the snapshot to be deleted.

### Response
An empty [Snapshot](#the-snapshot-resource) resource, with one non-empty field (its id).

## Restore Snapshot
`POST /api/v2/snapshots/{snapshot-id}/restore`

Restores the specified snapshot on the manager.

### URI Parameters
* snapshot-id: The id of the snapshot to be restored.

### Request Body
Property | Default | Description
---------|---------|-------------
`force`  |  false  | Specifies whether to force restoring the snapshot on a manager that already contains blueprints/deployments.
`recreate_deployments_envs` | true | Specifies whether deployment environments should be created for restored deployments.

### Response
An [Execution](#the-execution-resource) resource representing the restore snapshot workflow execution.


## Download Snapshot
`GET /api/v2/snapshots/{snapshot-id}/archive`

Downloads an existing snapshot.

### URI Parameters
* snapshot-id: The id of the snapshot to be downloaded.

### Response
A streamed response (content type `application/octet-stream`), which is a zip archive containing the snapshot data.

## Upload Snapshot
`PUT /api/v2/snapshots/{snapshot-id}/archive`

Uploads a snapshot to the Cloudify Manager.
The call expects a `application/octet-stream` content type where the content is a zip archive.
It is possible to upload a snapshot from a URL by specifying the URL in the `snapshot_archive_url` request body property.

### URI Parameters
* snapshot-id: The id of the snapshot to be uploaded.

### Request Body
Property | Type | Description
---------|---------|-------------
`snapshot_archive_url` | string | Optional parameter specifying a url to a snapshot that will be uploaded to the manager.

### Response
A [Snapshot](#the-snapshot-resource) resource.

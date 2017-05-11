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

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3/snapshots?_include=id"
```

```python
# Using CloudifyClient
snapshots = client.snapshots.list(_include=['id'])
for snapshot in snapshots:
    print snapshot

# Using requests
url = 'http://<manager-ip>/api/v3/snapshots'
headers = {'Tenant': 'default_tenant'}
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
      "id": "snapshot1"
    },
    {
      "id": "snapshot2"
    },
    {
      "id": "snapshot3"
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

`GET "{manager-ip}/api/v3/snapshots"`

Lists all snapshots.


### Response

Attribute | Type | Description
--------- | ------- | -------
`items` | list | A list of [Snapshot](#the-snapshot-resource) resources.


## Create Snapshot

> Requests Example

```shell
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3/snapshots/<snapshot-id>"
```

```python
# Using CloudifyClient
client.snapshots.create(
    snapshot_id='<snapshot-id>',
    include_metrics=False,
    include_credentials=False,
)


# Using requests
url = 'http://<manager-ip>/api/v3/snapshots/<snapshot-id>'
headers = {
    'Content-Type': 'application/json',
    'Tenant': 'default_tenant',
}
payload = {}
response = requests.put(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    json=payload,
)
response.json()
```

> Response Example

```json
{
  "status": "pending",
  "parameters": {
    "include_metrics": false,
    "config": {
      "postgresql_db_name": "cloudify_db",
      "default_tenant_name": "default_tenant",
      "postgresql_bin_path": "/usr/pgsql-9.5/bin/",
      "failed_status": "failed",
      "postgresql_username": "cloudify",
      "db_port": 9200,
      "postgresql_password": "cloudify",
      "created_status": "created",
      "db_address": "localhost",
      "file_server_root": "/opt/manager/resources",
      "postgresql_host": "localhost"
    },
    "include_credentials": true,
    "snapshot_id": "snapshot4"
  },
  "is_system_workflow": true,
  "blueprint_id": null,
  "tenant_name": "default_tenant",
  "created_at": "2017-05-11T16:16:45.948Z",
  "created_by": "admin",
  "private_resource": false,
  "workflow_id": "create_snapshot",
  "error": "",
  "deployment_id": null,
  "id": "bb9cd6df-7acd-4649-9fc1-fe062759cde8"
}
```

`PUT "{manager-ip}/api/v3/snapshots/{snapshot-id}"`

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
$ curl -X DELETE \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3/snapshots/<snapshot-id>"
```

```python
# Using CloudifyClient
client.snapshots.delete(snapshot_id='<snapshot-id>')

# Using requests
url = 'http://<manager-ip>/api/v3/snapshots/<snapshot-id>'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
)
response.json()
```

> Example Response

```json
{
  "status": "uploaded",
  "tenant_name": "default_tenant",
  "created_at": "2017-05-11T17:04:22.989Z",
  "created_by": "admin",
  "private_resource": false,
  "error": "",
  "id": "snapshot4"
}
```

`DELETE "{manager-ip}/api/v3/snapshots/{snapshot-id}"`

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

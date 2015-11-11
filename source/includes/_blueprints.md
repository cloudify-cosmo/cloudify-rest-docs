# Blueprints

## The Blueprint Resource

> Blueprint JSON Structure

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

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
id | string | A unique identifier for the blueprint.
description | string | The blueprint's description.
main_file_name | string | The blueprint's main file name.
plan | dict | The parsed result of the blueprint.
created_at | datetime | The time the blueprint was uploaded to the manager.
updated_at | datetime | The last time the blueprint was updated.


## Upload Blueprint
`PUT /api/v2/blueprints/{blueprint-id}`

Uploads a blueprint to Cloudify's manager.
The call expects an "application/octet-stream" content type where the content is a zip/tar.gz/bz2 archive.
It is possible to upload a blueprint from a URL by specifying the URL in the `blueprint_archive_url` request body property.


### URI Parameters
* `blueprint-id`: The id of the uploaded blueprint.

### Request Body
Property | Type | Description
--------- | ------- | -----------
application_file_name | string | The main blueprint file name in the blueprint's archive.
blueprint_archive_url | string | A URL the blueprint to be uploaded should be downloaded from by the manager.

### Response
A `Blueprint` resource.

## List Blueprints
`GET /api/v2/blueprints`

Lists all blueprints.

### Response

Field | Type | Description
--------- | ------- | -------
items | list | A list of `Blueprint` resources.


## Get Blueprint
`GET /api/v2/blueprints/{blueprint-id}`

Gets a specific blueprint.


### URI Parameters
* blueprint-id: The id of the blueprint to retrieve.

### Response
A `Blueprint` resource.

## Delete Blueprint
`DELETE /api/v2/blueprints/{blueprint-id}`

Deletes a specific blueprint.


### URI Parameters
* blueprint-id: The id of the blueprint to delete.

### Response
A `Blueprint` resource.


## Download Blueprint
Downloads a specific blueprint as an archive.

`GET /api/v2/blueprints/{blueprint-id}/archive`

### URI Parameters
* blueprint-id: The id of the blueprint to download.

### Response
The blueprint as an archive using an `application/octet-stream` content type.

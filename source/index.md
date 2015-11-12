---
title: Cloudify REST API Documentation

toc_footers:
  - <a href='http://docs.getcloudify.org'>Cloudify Documentation</a>

language_tabs:
  - shell

includes:
  - blueprints
  - deployments
  - nodes
  - node_instances
  - executions
  - events
  - plugins
  - snapshots
  - manager
  - deployment_modification
  - errors

search: true
---

# Cloudify REST API V2
Welcome to Cloudify's REST API Documentation!

The base URI for the v2 REST API is: `/api/v2`.

## Filter Response Fields

> Request Example

```shell
curl -XGET http://localhost/api/v2/blueprints?_include=id,created_at
```

> Response Example

```json
{
  "items": [
    {
      "created_at": "2015-11-11 13:11:40.324698",
      "id": "hello-world"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 1,
      "offset": null,
      "size": 10000
    }
  }
}
```

In order to include only certain fields in a response the `_include` query parameter can be used for specifying the fields to include in the response. The `_include` query parameter accepts a comma separated list of fields to include in the response. Specified field names should be a part of the queried resource structure otherwise an error is raised.

<aside class="notice">
  The "_include" query parameter can be used with all endpoints.
</aside>


## Data Filtering

## Pagination

## Sorting

## Authentication

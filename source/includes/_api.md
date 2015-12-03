# Cloudify REST API V2
Welcome to Cloudify's REST API Documentation!

The base URI for the v2 REST API is: `/api/v2`.

<aside class="notice">
This section describes various API features that apply to all resources
</aside>

## Response Fields Filtering (Projection)

> Request Example (receive only the `id` and `created_at` fields)

```shell
$ curl -XGET http://localhost/api/v2/blueprints?_include=id,created_at
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

You can choose to have only specific fields in the response by using the  `_include` query parameter.

The parameter value is a comma separated list of fields to include in the response, e.g. `_include=field1,field2,field3`

Note that specified field names must be part of the resource schema, otherwise an error is raised.



## Query Filtering (Selection)

> Request Example (requesting only blueprints which `id` is _my_blueprint1_ or _my_blueprint2_)

```shell
$ curl -XGET http://localhost/api/v2/blueprints?id=my_blueprint1&id=my_blueprint2&_include=id,created_at
```

> Response Example

```json
{
  "items": [
    {
      "created_at": "2015-12-02 11:27:48.527776",
      "id": "my_blueprint2"
    },
    {
      "created_at": "2015-12-02 11:23:01.939131",
      "id": "my_blueprint1"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 2,
      "offset": 0,
      "size": 10000
    }
  }
}
```

You can make your query more specific by using filters.

Filters are query parameters where the key is a field name and the value is a field value, e.g. `id=my-specific-id`

Filters also accept multiple values (OR) by using multiple parameters of the same key, e.g. `id=my-specific-id&id=another-id`

<aside class="warning">
<strong>_include</strong>, <strong>_sort</strong>, <strong>_size</strong>, <strong>_offset</strong> and <strong>_range</strong> are reserved keywords and cannot be used as filters.
</aside>

## Sorting

> Request Example (sort deployments by `id` descending)

```shell
$ curl -XGET http://localhost/api/v2/deployments?_sort=-id&_include=blueprint_id,id
```

> Response Example

```json
{
  "items": [
    {
      "id": "hello1",
      "blueprint_id": "hello-world"
    },
    {
      "id": "dep4",
      "blueprint_id": "my_blueprint2"
    },
    {
      "id": "dep3",
      "blueprint_id": "my_blueprint1"
    },
    {
      "id": "dep2",
      "blueprint_id": "my_blueprint2"
    },
    {
      "id": "dep1",
      "blueprint_id": "my_blueprint1"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 5,
      "offset": 0,
      "size": 10000
    }
  }
}
```

> Request Example #2 (sort deployments by `blueprint_id` ascending and `id` descending)

```shell
$ curl -XGET http://localhost/api/v2/deployments?_sort=blueprint_id&_sort=-id&_include=blueprint_id,id
```

> Response Example #2

```json
{
  "items": [
    {
      "id": "hello1",
      "blueprint_id": "hello-world"
    },
    {
      "id": "dep3",
      "blueprint_id": "my_blueprint1"
    },
    {
      "id": "dep1",
      "blueprint_id": "my_blueprint1"
    },
    {
      "id": "dep4",
      "blueprint_id": "my_blueprint2"
    },
    {
      "id": "dep2",
      "blueprint_id": "my_blueprint2"
    }
  ],
  "metadata": {
    "pagination": {
      "total": 5,
      "offset": 0,
      "size": 10000
    }
  }
}
```

You can sort resources by using the `_sort` query parameter, e.g. `_sort=id`

The default sort order is ascending; to make it descending, prefix the field with a minus sign, e.g. `_sort=-id`

Sorting also works on multiple fields by using multiple `_sort` parameters, where the sort sequence corresponds to the order of `_sort` parameters in the request.

## Pagination

> Request example (skip `1` resource, get `size` of `4`)

```shell
$ curl -XGET http://localhost/api/v2/events?_size=4&_offset=1&_include=@timestamp
```

> Request response

```json
{
  "items": [
  {
    "@timestamp": "2015-12-01T15:05:36.692Z"
  },
  {
    "@timestamp": "2015-12-01T15:05:37.493Z"
  },
  {
    "@timestamp": "2015-12-01T15:03:57.911Z"
  },
  {
    "@timestamp": "2015-12-01T15:03:58.025Z"
  }
  ],
  "metadata": {
    "pagination": {
      "total": 171,
      "offset": 1,
      "size": 4
    }
  }
}
```

You can receive a subset of your query by using two parameters:

* `_size` (default: 10000) the max size of the result subset you'd receive.
* `_offset` (default: 0) the number of resources to skip, i.e. `_offset=1` means you skip the first resource.

\* both parameters are optional.

The response metadata returns your requested parameters, and a `total` field which indicates the size of the full set.

## Authentication

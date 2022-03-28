# Searches

The `/searches/<resource>` endpoint is used to get a filtered list of resources based on their
labels and certain attributes or constraints.


## Resources

| Resource         | Pre-created filter | Attributes which can be used to filter by                                                      | Filter by label    |
|------------------|--------------------|------------------------------------------------------------------------------------------------|--------------------|
| `blueprints`     | blueprints filter  | id, state, tenant_name, created_by                                                             | yes                |
| `secrets`        |                    | key                                                                                            | no                 |
| `deployments`    | deployments filter | blueprint_id, created_by, site_name, schedules, tenant_name, display_name, installation_status | yes                |
| `nodes`          |                    | id, type                                                                                       | no                 |
| `node-types`     |                    | id, type                                                                                       | no                 |
| `node-instances` |                    | id                                                                                             | no                 |
| `workflows`      | deployments filter | —                                                                                              | deployment's label |

## Filtering rules

Filtering can be done by specifying a pre-created filter ID (for some resources) or by providing
a list of filter rules.


A filter rule is a dictionary of the following form:
```text
{
 "key": "<key>",
 "values": [<list of values>],
 "operator": "<LabelsOperator>" or "<AttrsOperator>",
 "type": "<FilterRuleType>"
}
```
`<LabelsOperator>` can be one of: "any_of", "not_any_of", "is_null" or "is_not_null".

`<AttrsOperator>` can be one of: "any_of", "not_any_of", "contains", "not_contains", "starts_with", "ends_with", "is_not_empty".

`<FilterRuleType>` can be one of: "label" or "attribute". If "label" is provided, then the operator must be a `<LabelsOperator>`, and if "attribute" is provided, then
the operator must be an `<AttrsOperator>`.

E.g. filtering by the following filter rules, will return all items of a resource whose creator name starts with _alice_ or _bob_,
and have the label `environment:aws` assigned to them.

```json
[
 {
  "key": "created_by",
  "values": ["alice", "bob"],
  "operator": "starts-with",
  "type": "attribute"
 },
 {
  "key": "environment",
  "values": ["aws"],
  "operator": "any_of",
  "type": "label"
 }
]
```


## Constraints

Alternatively `constraints` dictionary can be used instead of `filter_rules` and `filter_id` to
search for the resources matching given constraints.  If you want to know more about the
constraints, visit [this Cloudify Documentation section](https://docs.cloudify.co/latest/developer/blueprints/spec-inputs/#constraints).

The following constraints can be used to find the blueprints, which have at least these two labels
set (_environment=k8s_ and _tier=staging_) and IDs containing the string _cellar_ and ending
with _app_ (e.g. _wine_cellar_app_).

```json
{
  "labels": [
    {"environment": "k8s"},
    {"tier": "staging"}
  ],
  "name_pattern": {
    "ends_with": "app",
    "contains": "cellar"
  }
}
```


## Additional features

Additionally, a query string can be used to filter out specific resources.  In case of blueprints
and workflows the  `_search` field name is being used to filter these by `id`.  It is slightly more
complicated for deployments.  Two fields can be used: `_search` (to find deployments by `id`)
and `_search_name` (to find deployments by their `display_name`).  The resulting set of deployments
will be the union of both sub-sets.

> Request Example

```shell
$ curl -X POST \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"filter_rules": <a list of filter rules as described above>}' \
    "http://<manager-ip>/api/v3.1/searches/<resource>?_include=id"
```

`<resource>` can be either `blueprints`, `deployments` or `workflows`.

```python
# Using CloudifyClient
deployments = client.deployments.list(filter_rules=[...])
# Or
blueprints = client.blueprints.list(constraints={...})

# Using requests
url = 'http://<manager-ip>/api/v3.1/searches/<resource>' # `<resource>` can be either `blueprints`, `deployments` or `workflows`
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_include': 'id'}
payload = {'constraints': {...}}
response = requests.post(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
    json=payload
)
response.json()

```


## Response

> Response Example

```json
{
  "items": [
    {
      "id": "resource1"
    },
    {
      "id": "resource2"
    },
    {
      "id": "resource3"
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

`POST "{manager-ip}/api/v3.1/searches/<resource>"`

Get a filtered list of resource's items. Resource can be either blueprints, deployments or workflows.

Field | Type | Description
--------- | ------- | -------
`items` | list | A filtered list of resource's items.

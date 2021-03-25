# Searches

The `/searches/<resource>` endpoint is used to get a filtered list of a resource (currently, deployments or blueprints) 
based on its labels and certain attributes.
Deployments can be filtered by the following attributes: `blueprint_id`, `created_by`, `site_name`, and `schedules`.
Blueprints can be filtered by the attribute `created_by`. 

Filtering can be done by specifying a pre-created filter ID, or by providing a list of filter rules. 
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

E.g. filtering by the following filter rules, will return all items of a resource whose creator name starts with "alice" or "bob", 
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

> Request Example

```shell
$ curl -X POST \
    -H "Content-Type: application/json" \
    -H "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    -d '{"filter_rules": <a list of filter rules as described above>}' \
    "http://<manager-ip>/api/v3.1/searches/<resource>?_include=id"
```

`<resource>` can be either `deployments` or `blueprints`.

```python
# Using CloudifyClient
deployments = client.deployments.list(filter_rules=[...])
# Or
blueprints = client.blueprints.list(filter_rules=[...])

# Using requests
url = 'http://<manager-ip>/api/v3.1/searches/<resource>' # `<resource>` can be either `deployments` or `blueprints`
headers = {'Tenant': '<manager-tenant>'}
querystring = {'_include': 'id'}
payload = {'filter_rules': [...]}
response = requests.post(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
    json=payload
)
response.json()

```

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

Get a filtered list of resource's items. Resource can be either deployments of blueprints.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A filtered list of resource's items. 

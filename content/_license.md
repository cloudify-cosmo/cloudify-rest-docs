# License
**Supported for Cloudify Manager 4.6 and above.**

## The License Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | A unique identifier for the license.
`customer_id` | string | The id of the customer the license was issued for.
`expiration_date` | datetime | The expiration date of the license.
`license_edition` | string | The edition of the license (Spire/ Premium)
`trial` | boolean | true if the license is a trial license.
`cloudify_version` | string | The maximal Cloudify version the license is valid for
`capabilities` | object | A list of capabilities the license supports.
`expired` | boolean | true if the license has expired.


## Upload License

> Request Example

```shell
$ curl -X PUT \
    --header "Tenant: <manager-tenant>" \
    --header "Content-Type: application/json" \
    -u <manager-username>:<manager-password> \
    --data-binary @/<license_path>
    "<manager-ip>/api/v3.1/license"
```

```python
# Using CloudifyClient
license = client.license.upload(license_path)

# Using requests
url = 'http://<manager-ip>/api/v3.1/license'
headers = {'Tenant': '<manager-tenant>',
           'Content-Type': 'application/json'}
response = requests.put(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers
)
```

> Response Example

```json
{
"expiration_date": "2018-11-24T00:00:00.000Z",
"cloudify_version": "4.6",
"license_edition": "Spire",
"capabilities": [
    "Mock1",
     "Mock2"
     ],
"trial": false,
"customer_id": "CloudifyMock",
"expired": true
}
```

`PUT "{manager-ip}/api/v3.1/license"`

Upload a license.

### Response

A `License` resource.


## List License

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "<manager-ip>/api/v3.1/license"
```

```python
# Using CloudifyClient
license = client.license.list()

# Using requests
url = 'http://<manager-ip>/api/v3.1/license'
headers = {'Tenant': '<manager-tenant>'
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers
)
```

> Response Example

```json
{
   "items":[
      {
         "expiration_date":"2018-11-24T00:00:00.000Z",
         "cloudify_version":"4.6",
         "license_edition":"Spire",
         "capabilities":[
            "Mock1",
            "Mock2"
         ],
         "trial":false,
         "customer_id":"CloudifyMock",
         "expired":true
      }
   ],
   "metadata":{
      "pagination":{
         "total":1,
         "offset":0,
         "size":1000
      }
   }
}
```

`GET "{manager-ip}/api/v3.1/license"`

List license.

### Response

Field | Type | Description
--------- | ------- | -------
`items` | list | A `License` resource.
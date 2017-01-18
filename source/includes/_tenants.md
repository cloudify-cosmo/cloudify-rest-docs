# Tenants

## The Tenant Resource

<aside class="notice">
This section describes API features that are part of the Cloudify premium edition
</aside>

> `Note`

```python
# include this code when using cloudify python client-
from cloudify_rest_client import CloudifyClient
client = CloudifyClient(
        host='<manager-ip>',
        username='<manager-username>',
        password='<manager-password>',
        tenant='<manager-tenant>')
```

```html

```

The Tenant resource is a logical component that represents a closed environment with its own resources.


### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | integer | Auto increment, unique identifier for the tenant.
`name` | string | The blueprint's description.


## Get Tenant

> Request Example

```shell
$ curl -X GET --header "tenant: default_tenant" -u user:password "http://<manager-ip>/api/v3/tenants/{tenant-name}"
```

```python
# Python Client-
client.tenants.get('default_tenant')
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': 'default_tenant'
}

var settings = {
  "url": "http://<manager-ip>/api/v3/tenants/{tenant-name}",
  "method": "GET",
  "headers": headers
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
obsolete
```

> Response Example

```json
{
    "name": "default_tenant",
    "groups": [],
    "users": ["admin"]
}
```

`GET "{manager-ip}/api/v3/tenants?name={tenant-name}"`

Retrieves a specific tenant.

### URI Parameters
* `tenant-name`: The name of the tenant to retrieve.

### Response
A `Tenant` resource.





## List Tenants

> Request Example

```shell
$ curl -X GET --header "tenant: default_tenant" -u user:password "http://<manager-ip>/api/v3/tenants"
```

```python
# Python Client-
client.tenants.list()
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': 'default_tenant'
}

var settings = {
  "url": "http://<manager-ip>/api/v3/tenants",
  "method": "GET",
  "headers": headers
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
obsolete
```

> Response Example

```json
{
 "items":
    [
        {
            "name": "default_tenant",
            "groups": [],
            "users": ["admin"]
        }
    ]
}
```

`GET "{manager-ip}/api/v3/tenants"`

List all tenants.

### Response
Field | Type | Description
--------- | ------- | -------
`items` | list | A list of `Tenant` resources.



## Create Tenant

> Request Example

```shell
$ curl -X POST -H "Content-Type: application/json" -H "tenant: <tenant-name>" -u user:password "http://<manager-ip>/api/v3/tenants/<new-tenant-name>"
```

```python
# Python Client-
client.tenants.create(<new-tenant-name>)
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/tenants/<new-tenant-name>",
  "method": "POST",
  "headers": headers
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
obsolete
```

> Response Example

```json
{
    "name": "new_tenant",
    "groups": [],
    "users": []
}
```

`POST "{manager-ip}/api/v3/tenants/{new-tenant-name}"`

Creates a tenant.

### URI Parameters
* `new-tenant-name`: The name of the tenant to create.

### Response
A `Tenant` resource.





## Delete Tenant

> Request Example

```shell
$ curl -X DELETE -H "Content-Type: application/json" -H "tenant: <tenant-name>" -u ser:password "http://<manager-ip>/api/v3/tenants/<tenant-name-to-delete>"
```

```python
# Python Client-
client.tenants.delete(<tenant-name>)
```

```javascript
var headers = {
   'content-type': 'application/json',
   'authorization': 'Basic ' + new Buffer(username + ':' + password).toString('base64'),
   'tenant': <tenant-name>
}

var settings = {
  "url": "http://<manager-ip>/api/v3/tenants/<tenant-name-to-delete>",
  "method": "DELETE",
  "headers": headers
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```html
obsolete
```

> Response Example

```json
{

    "name": "tenant-name",
    "groups": [],
    "users": []
}
```

`DELETE "{manager-ip}/api/v3/tenants/{tenant-name-to-delete}"`

Delete a tenant.

### URI Parameters
* `tenant-name-to-delete`: The name of the tenant to delete.

### Response
A `Tenant` resource.
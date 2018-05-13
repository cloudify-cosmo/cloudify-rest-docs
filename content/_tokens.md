# Tokens

## The Tokens Resource

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
`value` | string | The value of the token


## Get Token

> Request Example

```shell
$ curl -X GET "http://<manager-ip>/api/v2.1/tokens"
```

```python
# Python Client-
client.tokens.get()

# Python Requests-
url = "http://<manager-ip>/api/v2.1/tokens"
headers = {'content-type': "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.text)
```

```javascript
var settings = {
  "crossDomain": true,
  "url": "http://<manager-ip>/api/v2.1/tokens",
  "method": "GET",
  "headers": {"content-type": "application/json"}
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> Response Example

```json
{
	"value":"reltkwe5lk645jp0jdvsr345gkllsre"
}
```

`GET "{manager-ip}/api/v2.1/tokens"`

Gets a token.

### Response
A `Token` resource.
# Tokens

## The Tokens Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`role` | string | The role associated with the token (`admin` or `user`)
`value` | string | The value of the token


## Get Token

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/tokens"
```

```javascript
var request = require('request-promise');

async function login(host, username, password, tenant){
    var tokens = await request(
        {
           method: 'GET',
           url: host + "/api/v3.1/tokens",
           auth: { username: username, password: password},
           headers: {'Tenant': tenant},
           strictSSL: false
        }
    );
    return tokens;
}

async function main() {

    var token = JSON.parse(
        await login("<manager-ip>", "<manager-username>",
                    "<manager-password>", "<manager-tenant>")
    );

    console.log(token);
}

main();
```

```python
# Using CloudifyClient
client.tokens.get()

# Using requests
url = 'http://<manager-ip>/api/v3.1/tokens'
headers = {'Tenant': '<manager-tenant>'}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
)
response.json()
```

> Response Example

```json
{
  "role": "admin",
  "value": "WyIwIiwiZjRmNTUzMWRmYmFmZGZmNTlkNTkyZGY2MjMxYzkyNTEiXQ.C_YU9Q.IhQMlnXZIaCtWUUHH_CzHP4-Bg4"
}
```

`GET "{manager-ip}/api/v3.1/tokens"`

Gets a token.

### Response
A `Token` resource.

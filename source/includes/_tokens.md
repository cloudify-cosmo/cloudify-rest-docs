# Tokens

## The Tokens Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`value` | string | The value of the token
`role` | string | The role associated with the token (`admin` or `user`)


## Get Token

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3/tokens"
```

```python
# Using CloudifyClient
client.tokens.get()

# Using requests
url = 'http://<manager-ip>/api/v3/tokens'
headers = {'Tenant': 'default_tenant'}
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

`GET "{manager-ip}/api/v3/tokens"`

Gets a token.

### Response
A `Token` resource.

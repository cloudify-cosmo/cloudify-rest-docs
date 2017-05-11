# Tokens

## The Tokens Resource

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

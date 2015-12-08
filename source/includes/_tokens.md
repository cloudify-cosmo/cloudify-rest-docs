# Tokens

## The Tokens Resource

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`value` | string | The value of the token


## Get Token

> Request Example

```shell
$ curl -XGET http://localhost/api/v2/tokens
```

> Response Example

```json
{
	"value":"reltkwe5lk645jp0jdvsr345gkllsre"
}
```

`GET /api/v2/tokens`

Gets a token.

### Response
A `Token` resource.
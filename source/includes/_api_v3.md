# Cloudify REST API V3.0

> `Every request requires user credentials and a tenant to be specified.`

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
obsolete
```

Cloudify 4.0.0 introduced REST API V3.0.

The base URI for the v3.0 REST API is: `/api/v3.0`.

Starting from Cloudify 4.0.0, all communication to the server requires:
 * Authentication using user credentials.
 * Tenant name, representing the scope of the request.

Every Cloudify Manger has a default tenant, called `default_tenant`.
The `default_tenant` tenant is created during bootstrap.

In addition to the `default_tenant`, every Cloudify Manager includes a bootstrap Admin.
The bootstrap Admin is the Admin user that created during the bootstrap.

In addition to the user credentials, every request must also specify a tenant in the header.

In the case of using the Cloudify community edition or if you have not created any new tenant,
you can use the `default_tenant` as the tenant for the request.

### Parameters ###
* `<manager-ip>`: Replace with the IP of your Cloudify Manager
* `<manager-username>`: Replace with a username for the Cloudify Manager instance username
* `<manager-password>`: Replace with the password for the user specified in <manager-username>
* `<manager-tenant>`: Replace with the tenant on which to perform the request
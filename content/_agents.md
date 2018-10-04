# Agents

**Supported for Cloudify Manager 4.5 and above.**

## The Agents Resource

This resource represents a Cloudify Agent, and is used for examining the details
of installed agents.

### Attributes:

Attribute | Type | Description
--------- | ------- | -------
`id` | string | Unique identifier of the node instance that installed the agent
`host_id` | string | Unique identifier of the node instance that the agent is installed on. Identical to `id` except for deployment proxy agents.
`ip` | string | IP of the host the agent is installed on
`install_methods` | string | The agent's install_method (remote/plugin/init_script/provided)
`system` | string | Description of the OS the agent is installed on (the linux distribution name, or "windows")
`version` | string | Cloudify version of the agent software
`node` | string | ID of the node that installed the agent
`deployment` | string | ID of the deployment that installed the agent

## List agents

> Request Example

```shell
$ curl -X GET \
    --header "Tenant: <manager-tenant>" \
    -u <manager-username>:<manager-password> \
    "http://<manager-ip>/api/v3.1/agents?node_ids=<node_1>&node_ids=<node_2>"
```

```python
# Using CloudifyClient
client.agents.list(node_ids=['node_1', 'node_2'])

# Using requests
url = 'http://<manager-ip>/api/v3.1/agents'
headers = {'Tenant': '<manager-tenant>'}
querystring = {
    'node_ids': ['node_1', 'node_2']
}
response = requests.get(
    url,
    auth=HTTPBasicAuth('<manager-username>', '<manager-password>'),
    headers=headers,
    params=querystring,
)
response.json()
```
> Response Example
```json
{
    "items": [
        {
            "node": "x",
            "ip": "127.0.0.1",
            "system": "centos core",
            "install_method": "remote",
            "version": "4.5.0",
            "deployment": "d4",
            "host_id": "x_asa5b3",
            "id": "x_asa5b3"
        }
    ],
    "metadata": {
        "pagination": {
            "total": 1,
            "offset": 0,
            "size": 1
        }
    }
}
```

Gets the list of installed agents.

### URI Parameters

For additional filtering of the agents list, the following parameters can be provided:

<aside class="notice">
Those are the same parameters as accepted by the `cfy agents validate` and `cfy agents install` method, and their respective workflows. Therefore it is possible to first filter the agents, examine the list of agents to be worked on, and only then validate and upgrade them.
</aside>

* `deployment_id`: the agent deployment ID
* `node_ids`: the agent node ID (can be provided multiple times)
* `node_instance_ids`: the agent node instance ID (can be provided multiple times)
* `install_method`: the agent install method (can be provided multiple times)

### Response
A list of `Agent` resources.

#!/usr/bin/python
import os
import json
endpoint_ips = os.environ['ENDPOINT_LIST']
print(endpoint_ips)
endpoint_array = []
for ip in endpoint_ips.split(","):
    endpoint = { "Name": "endpoint-"+str(ip),    "URL": "tcp://{}:2375".format(str(ip))  }
    endpoint_array.append(endpoint)
with open("/config_flags/endpoints.json","w+") as fd:
        json.dump(endpoint_array, fd)



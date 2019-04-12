#!/usr/bin/python
import os
import json

endpoint_ips = os.environ['ENDPOINT_LIST']
endpoint_file = "/vol1/endpoints.json"
endpoint_array = []

for ip in endpoint_ips.split(","):
    endpoint = { "Name": "endpoint-"+str(ip),    "URL": "tcp://{}:2375".format(str(ip))  }
    endpoint_array.append(endpoint)

if os.path.exists(endpoint_file):
    os.remove(endpoint_file)
with open(endpoint_file,"w+") as fd:
    json.dump(endpoint_array, fd)



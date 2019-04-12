#!/usr/bin/python

import json
import sys
endpoint_file = "/opt/portainer/vol1/endpoints.json"
new_endpoint = "{" + '"Name": "endpoint-{0}",    "URL": "tcp://{0}:2375"'.format(str(sys.argv[1])) + "}"
with open(endpoint_file, "r+") as fd:
    old_data = fd.read().strip()
    old_data = old_data.replace("[", "")
    old_data = old_data.replace("]", "")
    new_data = "[" + old_data + ", " + new_endpoint + "]"
    fd.seek(0, 0)
    fd.truncate(0) 
    fd.seek(0, 0)
    fd.write(new_data)
    

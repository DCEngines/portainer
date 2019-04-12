#!/bin/sh
set -x
echo "copying custom files..."
cp /tmp/create_endpointjson.py /vol1/
cp /tmp/templates.json /vol1/
cp /tmp/add_endpoint.py /vol1/

ls -ltr /vol1/create_endpointjson.py
ls -ltr /vol1/templates.json
ls -ltr /vol1/add_endpoint.py

echo "Creating json file for endpoint list..."
/vol1/create_endpointjson.py
echo "Running portainer binary file..."
/portainer $@



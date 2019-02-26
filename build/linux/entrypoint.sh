#!/bin/sh
set -x
echo "Creating json file for endpoint list..."
/config_flags/create_endpointjson.py
echo "Running portainer binary file..."
/portainer $@



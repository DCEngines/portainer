FROM portainer/base

COPY dist /

VOLUME /data

COPY build/linux/create_endpointjson.py /tmp/
COPY build/linux/templates.json /tmp/
COPY build/linux/entrypoint.sh /entrypoint/
COPY build/linux/add_endpoint.py /tmp/
RUN chmod 755 /entrypoint/entrypoint.sh
RUN chmod 755 /tmp/create_endpointjson.py

WORKDIR /

EXPOSE 9000


ENTRYPOINT ["/entrypoint/entrypoint.sh"]

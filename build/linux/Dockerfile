FROM portainer/base

COPY dist /

VOLUME /data

COPY build/linux/create_endpointjson.py /config_flags/
COPY build/linux/templates.json /config_flags/
COPY build/linux/entrypoint.sh /config_flags/

RUN chmod 755 /config_flags/entrypoint.sh
RUN chmod 755 /config_flags/create_endpointjson.py

WORKDIR /

EXPOSE 9000


ENTRYPOINT ["/config_flags/entrypoint.sh"]

FROM ubuntu:24.10

WORKDIR /config

COPY . .

RUN chmod +x env_exporter.sh

CMD [ "./env_exporter.sh" ]

FROM registry.gitlab.com/nomadic-labs/tezos/bare:amd64-rafoo-normalize-rpc-filter-docker
COPY *.json /sandbox/
RUN sudo chown -R tezos:nogroup /sandbox
EXPOSE 8732
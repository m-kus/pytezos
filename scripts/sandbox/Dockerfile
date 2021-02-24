FROM registry.gitlab.com/nomadic-labs/tezos/bare:amd64-docker-for-all
RUN tezos-node config init --data-dir /home/tezos/sandbox --network sandbox --expected-pow 0 --connections 0 --rpc-addr 0.0.0.0:8732
RUN tezos-node identity generate "0" --data-dir /home/tezos/sandbox
COPY --chown=tezos:nogroup sandbox.json /home/tezos/sandbox/
COPY --chown=tezos:nogroup parameters.json /home/tezos/sandbox/
ENTRYPOINT ["tezos-node", "run", \
    "--data-dir=/home/tezos/sandbox", \
    "--synchronisation-threshold=0", \
    "--sandbox=/home/tezos/sandbox/sandbox.json"]
EXPOSE 8732
FROM python:3.7-slim-buster

ARG NB_USER
ARG NB_UID

USER root

RUN apt update && \
    apt install -y build-essential pkg-config libsodium-dev libsecp256k1-dev libgmp-dev && \
    rm -rf /var/lib/apt/lists/*
RUN pip install notebook jupyter-client

ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

COPY *.ipynb ${HOME}/
RUN chown -R ${NB_USER}:${NB_USER} ${HOME}/

WORKDIR ${HOME}
USER ${USER}

RUN pip install --user pytezos

EXPOSE 8888
ENTRYPOINT []
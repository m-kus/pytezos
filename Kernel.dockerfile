FROM python:3.11-slim-buster

RUN apt update && \
    apt install -y build-essential pkg-config libsodium-dev libsecp256k1-dev libgmp-dev make curl git && \
    rm -rf /var/lib/apt/lists/*
RUN pip install poetry
RUN useradd -ms /bin/bash jupyter

RUN mkdir /home/jupyter/michelson-kernel
RUN mkdir /home/jupyter/notebooks
COPY Makefile pyproject.toml poetry.lock README.md /home/jupyter/michelson-kernel/
# We want to copy our code at the last layer but not to break poetry's "packages" section
RUN mkdir -p /home/jupyter/michelson-kernel/src/michelson_kernel && \
    touch /home/jupyter/michelson-kernel/src/michelson_kernel/__init__.py && \ 
    mkdir -p /home/jupyter/michelson-kernel/src/pytezos && \
    touch /home/jupyter/michelson-kernel/src/pytezos/__init__.py

WORKDIR /home/jupyter/michelson-kernel
RUN poetry config virtualenvs.in-project true
RUN make install DEV=0

COPY . /home/jupyter/michelson-kernel/
RUN chown -R jupyter /home/jupyter/

USER jupyter
RUN make install-kernel

WORKDIR /home/jupyter/notebooks
EXPOSE 8888
ENTRYPOINT [ "/home/jupyter/michelson-kernel/.venv/bin/jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--no-browser", "--no-mathjax" ]

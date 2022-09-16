FROM python:3.10-alpine3.16 AS compile-image
RUN apk add --update --no-cache \
		build-base \
		git \
		gmp-dev \
		libffi-dev \
		libressl-dev \
		libsodium \
		libsodium-dev \
    && mkdir -p /opt/pytezos/src/pytezos \
    && touch /opt/pytezos/src/pytezos/__init__.py \
    && mkdir -p /opt/pytezos/src/michelson_kernel \
    && touch /opt/pytezos/src/michelson_kernel/__init__.py
WORKDIR /opt/pytezos
ENV PATH="/opt/pytezos/bin:$PATH"
ENV PYTHON_PATH="/opt/pytezos/src:$PATH"

COPY pyproject.toml requirements.txt README.md /opt/pytezos/

RUN /usr/local/bin/pip install \
		--prefix /opt/pytezos \
		--no-cache-dir \
		--disable-pip-version-check \
		--no-deps \
		-r /opt/pytezos/requirements.txt -e . \
	&& rm -r /opt/pytezos/src/michelson_kernel /opt/pytezos/bin/michelson-kernel

FROM python:3.10-alpine3.16 AS build-image
RUN apk --no-cache add \
		binutils \
		gmp-dev \
		gmp \
		libsodium-dev \
	&& adduser -D pytezos

USER pytezos
ENV PATH="/opt/pytezos/bin:$PATH"
ENV PYTHONPATH="/home/pytezos:/home/pytezos/src:/opt/pytezos/src:/opt/pytezos/lib/python3.10/site-packages:$PYTHONPATH"
WORKDIR /home/pytezos/
ENTRYPOINT [ "pytezos" ]

COPY --chown=pytezos --from=compile-image /opt/pytezos /opt/pytezos
COPY --chown=pytezos . /opt/pytezos
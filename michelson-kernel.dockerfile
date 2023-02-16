FROM python:3.11-alpine3.17 AS compile-image
RUN apk add --update --no-cache \
	build-base \
	libtool \
	autoconf \
	automake \
	python3-dev \
	libffi-dev \
	gmp-dev \
	libsodium-dev \
	libsecp256k1-dev

RUN mkdir /tmp/secp256k1 \
	&& cd /tmp \
	&& wget https://github.com/bitcoin-core/secp256k1/archive/refs/tags/v0.2.0.tar.gz -O /tmp/secp256k1.tar.gz \
	&& tar -xzf /tmp/secp256k1.tar.gz -C /tmp/secp256k1 --strip-components=1 \
	&& cd /tmp/secp256k1 \
	&& ./autogen.sh \
	&& ./configure

RUN python -m venv --without-pip --system-site-packages /opt/pytezos \
    && mkdir -p /opt/pytezos/src/pytezos/ \
    && touch /opt/pytezos/src/pytezos/__init__.py \
    && mkdir -p /opt/pytezos/src/michelson_kernel/ \
    && touch /opt/pytezos/src/michelson_kernel/__init__.py
WORKDIR /opt/pytezos
ENV PATH="/opt/pytezos/bin:$PATH"
ENV PYTHON_PATH="/opt/pytezos/src:$PATH"

COPY pyproject.toml requirements.txt README.md /opt/pytezos/

RUN /usr/local/bin/pip install --prefix /opt/pytezos --no-cache-dir --disable-pip-version-check --no-deps -r /opt/pytezos/requirements.txt -e .

FROM python:3.11-alpine3.17 AS build-image
RUN apk add --update --no-cache \
	binutils \
	gmp-dev \
	libsodium-dev \
	libsecp256k1-dev

RUN adduser -D pytezos
USER pytezos
ENV PATH="/opt/pytezos/bin:$PATH"
ENV PYTHONPATH="/home/pytezos:/home/pytezos/src:/opt/pytezos/src:/opt/pytezos/lib/python3.11/site-packages:$PYTHONPATH"
WORKDIR /home/pytezos/
ENTRYPOINT [ "/opt/pytezos/bin/jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--no-browser", "--no-mathjax" ]
EXPOSE 8888

COPY --chown=pytezos --from=compile-image /opt/pytezos /opt/pytezos
COPY --chown=pytezos . /opt/pytezos

RUN michelson-kernel install

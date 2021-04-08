ARG POETRY=1.0.5
ARG PENDULUM=2.1.0
ARG PYTEST=5.4

FROM python:3-alpine AS build
ARG POETRY
COPY . /pytezos
RUN apk update \
	&& apk --no-cache add --virtual build-deps \
	    build-base \
		libffi-dev \
		libressl-dev \
	&& pip3 install cryptography==3.3.2 poetry==$POETRY \
	&& cd /pytezos && poetry build


FROM python:3-alpine
ARG POETRY
ARG PENDULUM
ARG PYTEST
COPY --from=build /pytezos/dist/*.whl /tmp/pytezos/
RUN apk update \
	&& apk --no-cache add --virtual build-deps \
		build-base \
		autoconf \
		automake \
		git \
		gmp-dev \
		isl \
		libatomic \
		libffi-dev \
		libgomp \
		libressl-dev \
		libtool \
		make \
		mpfr4 \
		mpc1 \
		musl-dev \
		openssl \
	&& apk --no-cache add \
		binutils \
		libsodium-dev \
		gmp \
	&& git clone https://github.com/bitcoin-core/secp256k1.git /tmp/secp256k1 && cd /tmp/secp256k1 \
	&& ./autogen.sh \
	&& ./configure \
	&& make install \
	&& cd / && rm -rf /tmp/secp256k1 \
	&& pip3 install --no-cache-dir cryptography==3.3.2 poetry==$POETRY pytest~=$PYTEST \
	&& pip3 install --no-build-isolation --no-cache-dir pendulum==$PENDULUM \
	&& pip3 install --no-cache-dir /tmp/pytezos/*.whl && rm -rf /tmp/pytezos \
	&& pip3 uninstall --yes poetry \
	&& rm -rf ~/.cache/pip && apk del py-pip \
	&& apk del build-deps \
	&& rm -f /sbin/apk && rm -rf /etc/apk && rm -rf /lib/apk && rm -rf /usr/share/apk && rm -rf /var/lib/apk
RUN mkdir /home/jupyter/notebooks

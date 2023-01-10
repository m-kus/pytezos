ARG POETRY=1.3.2
ARG PYTEST=5.4

FROM python:3.8-alpine3.13 AS build
ARG POETRY
COPY . /pytezos
RUN apk update \
	&& apk --no-cache add --virtual build-deps \
	    build-base \
		libffi-dev \
		libressl-dev \
	&& pip3 install cryptography==3.3.2 poetry==$POETRY \
	&& cd /pytezos && poetry build


FROM python:3.8-alpine3.13
ARG POETRY
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
		zeromq-dev \
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
	&& pip3 install --upgrade pip setuptools wheel \
	&& pip3 install --no-cache-dir cryptography==3.3.2 poetry==$POETRY pytest~=$PYTEST \
	&& pip3 install --no-cache-dir /tmp/pytezos/*.whl && rm -rf /tmp/pytezos \
	&& pip3 uninstall --yes poetry \
	&& rm -rf ~/.cache/pip && apk del py-pip \
	&& apk del build-deps \
	&& rm -f /sbin/apk && rm -rf /etc/apk && rm -rf /lib/apk && rm -rf /usr/share/apk && rm -rf /var/lib/apk

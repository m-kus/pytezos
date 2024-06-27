FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    libsecp256k1-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Use virtual environment to preserve system libraries
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/python -m pip install --upgrade "pytezos==3.13.1"
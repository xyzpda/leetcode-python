FROM python:3.8.7-buster

#alias
RUN alias ll="ls -l"

RUN apt-get update \
   && apt-get install -y --no-install-recommends \
   lsb-release \
   && apt-get -y clean \
   && rm -rf /var/lib/apt/lists/*


FROM ubuntu:latest

RUN apt update && apt install -y \
    alsa-utils \
    nano \
    curl \
    git \
    && apt clean

RUN mkdir -p /mnt/music

CMD ["bash"]

FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    wget xz-utils bzip2 ca-certificates \
    libgtk-3-0 libdbus-glib-1-2 libxt6 libx11-xcb1 libasound2 libxcomposite1 libxdamage1 \
    libxrandr2 libpangocairo-1.0-0 libpango-1.0-0 libcups2 libxss1 libgconf-2-4 libnss3 \
    libxshmfence1 libxcb1 libatk1.0-0 libatk-bridge2.0-0 libdrm2 libgbm1 libnspr4 libxrender1 \
    libxfixes3 libegl1 libgl1 libdbus-1-3 --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN wget -O /tmp/firefox.tar.xz "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" && \
    tar -xf /tmp/firefox.tar.xz -C /opt && \
    rm /tmp/firefox.tar.xz && \
    ln -sf /opt/firefox/firefox /usr/local/bin/firefox

RUN mkdir /screenshots

WORKDIR /screenshots

CMD ["firefox", "--headless", "--screenshot", "/screenshots/screenshot.png", "https://www.mozilla.org"]

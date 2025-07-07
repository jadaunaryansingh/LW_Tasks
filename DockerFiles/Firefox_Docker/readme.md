# Firefox Headless Screenshot Docker

## Build image

```bash
docker build -t firefox-headless-screenshot .

Run container (mount folder for screenshots)

mkdir -p ~/screenshots
docker run --rm -v ~/screenshots:/screenshots firefox-headless-screenshot

Screenshot saved at ~/screenshots/screenshot.png.
To screenshot a different URL or file name

docker run --rm -v ~/screenshots:/screenshots firefox-headless-screenshot firefox --headless --screenshot /screenshots/custom.png https://example.com

If Firefox fails sandbox errors, add --no-sandbox flag

firefox --no-sandbox --headless --screenshot /screenshots/screenshot.png http


# 🔊 Ubuntu Docker Image with Sound Card Access

This Docker image is based on **Ubuntu** and provides audio support using `alsa-utils`.  
It enables testing sound playback inside containers by mapping your host's sound devices.

---

## 🧰 Tools Included

- `alsa-utils` (for `aplay`, `arecord`)
- `curl`
- `nano`
- `git`

---

## 🛠 Dockerfile Used

```Dockerfile
FROM ubuntu:latest

RUN apt update && apt install -y \
    alsa-utils \
    curl \
    nano \
    git \
    && apt clean

RUN mkdir -p /mnt/music

CMD ["bash"]
```

---

## 🔧 Build the Docker Image

```bash
sudo docker build -t ubuntu-sound .
```

---

## 🔊 Run with Sound Card Access

```bash
sudo docker run -it --rm \
  --device /dev/snd \
  --group-add audio \
  -v ~/Music:/mnt/music \
  ubuntu-sound
```

---

## 🎵 Play Audio Inside Container

```bash
aplay -l                             # List sound cards
aplay /mnt/music/Front_Center.wav   # Play test sound
```

To make sure the test sound file exists:

```bash
cp /usr/share/sounds/alsa/Front_Center.wav ~/Music/
```

---

## 👨‍💻 Author

Built with ❤️ by **Aryan Singh Jadaun**  
LinuxWorld Intern | Docker • DevOps • AI Enthusiast 🚀

FROM linuxserver/ffmpeg:latest
MAINTAINER stefenauris@proton.me
COPY RTMPS.py /app
RUN apt update && apt install -y python3
EXPOSE 443
CMD python3 RTMPS.py

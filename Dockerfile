FROM linuxserver/ffmpeg:latest
LABEL MAINTAINER="stefenauris@proton.me"
RUN apt update && apt install -y python3
EXPOSE 443 1935
COPY RTMPS.py /app
ENTRYPOINT [ "python3", "/app/RTMPS.py" ] 

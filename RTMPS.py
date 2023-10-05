# source: https://zomro.com/blog/faq/213-kak-zapustit-kruglosutochnuju-transljaciju-youtube-na-linux
import os

dirname = "/mnt/"

key = os.environ["rtmps_key"]
brate = os.environ["bitrate"]

while True:
    files = os.listdir(dirname)
    for f in files:
        if ".mp4" in f:
            cmd = "ffmpeg -threads 3 -re -i " + '"' + dirname + f + '"' + " -bufsize 6000k -maxrate 4500k -b:v " + brate + \
                " -c:v libx264 -movflags +faststart -preset ultrafast -crf 24 -g 60 -f flv " + key
            print(cmd)
            os.system(cmd)

# source: https://zomro.com/blog/faq/213-kak-zapustit-kruglosutochnuju-transljaciju-youtube-na-linux
import os

dirname = "/mnt/"

key = 'rtmp://a.rtmp.youtube.com/live2/0xx0-xxxx-x000-x0x0-xxxx'

while True:
    files = os.listdir(dirname)
    for f in files:
        if ".mp4" in f:
            cmd = "ffmpeg -threads 3  -re -i " + dirname + f + \
                " -c:v libx264 -preset ultrafast -crf 24 -g 3 -f flv " + key
            print(cmd)
            os.system(cmd)

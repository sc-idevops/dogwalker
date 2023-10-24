# Dog Walker

I created this simple project to help a friend keep a stream of music going to Youtube 24/7. The name for the project is inspired by his record label called [Walking Dog.](https://www.thewalkingdog.net/)

# How to Use

1. [Download and install Docker Desktop for Windows.](https://docs.docker.com/desktop/install/windows-install/)
1. Download this repository and unzip it into a folder. Click the green *CODE* button and choose download zip.
1. Copy the .env.example to .env and make the modifications needed. At minimum you need to change these two:
    - DATA_DIR is the directory that has all of your video files that you want to stream in.
    - rtmps_key is the URL you stream to on youtube. This is found in Youtube Studio. Click *GO LIVE* and copy the Stream key. Paste it over the *0xx0-xxxx-x000-x0x0-xxxx* in the example so the formatting stays the same. Note that this is a secret value, and by keeping it in the .env file it stays safe.
1. execute the build.ps1 script in Powershell, or just run the following commands in a terminal:
    - docker compose build
        - This step only has to be done the first time, or if you make any changes to the code or env file.
    - docker compose up -d
        - This command actually starts the program. It will run forever until you stop it in docker or run *docker compose down*
1. You can stop the program by using docker desktop to kill the container or by running *docker compose down* in a powershell in the directory you put the program.

## Development Overview

General idea is the docker container contains a simple python script that uses ffmpeg to stream the mp4 files to youtube.

Copy the .env.example file to .env and modify to suit your bandwidth, location of files, and streaming key.

### Development Considerations
- [x] Consider storing the streamer key in a secret instead of hard coded into the python file (or you can put it into the env file...)
    - key is now safely stored in the .env file or can be specified on runtime as rtmps_key
- [ ] Randomly select a song to play, or an album instead of playing linearly. 
- [x] Configure the ffmpeg command to check/escape special characters that might exist in filenames.
- [ ] Allow music files to be stored in subfolders, and recursively search through all directories.

### Assumptions
- The docker container should restart if it disconnects from youtube (maybe)
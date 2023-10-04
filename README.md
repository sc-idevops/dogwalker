# Dog Walker

I created this simple project to help a friend keep a stream of music going to Youtube 24/7. The name for the project is inspired by his record label called [Walking Dog.](https://www.thewalkingdog.net/)

## Docker

General idea is the docker container contains a simple python script that uses ffmpeg to stream the mp4 files to youtube.


## Considerations
- [x] Consider storing the streamer key in a secret instead of hard coded into the python file (or you can put it into the env file...)
    - key is now safely stored in the .env file or can be specified on runtime as rtmps_key
- [ ] Randomly select a song to play, or an album instead of playing linearly. 
- [x] Configure the ffmpeg command to check/escape special characters that might exist in filenames.

## Assumptions
- The docker container should crash if it disconnects from youtube and automatically restart
- I hope docker desktop makes it easy to run this once you point it to the directory of music and give it the creds
- Does the python script recurse into subdirectories to find music?
    - unfortunately not yet, that will have to be addressed. 

If it ends up not being this simple I'll feel very silly :)
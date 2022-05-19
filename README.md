# Instant-ngp helper
This is a helper for using [instant-ngp](https://github.com/NVlabs/instant-ngp).
## How to use
First install:

- Visual Studio 2019 (Desktop development with C++)
- Cuda 11.6
- Python 3.9 or 3.10
- git

Then clone this repository and run install.py in command prompt. Then close the command prompt.
```
python install.py
```
Put your video file in the instant-ngp-helper\instant-ngp\tmp directory, or if you have images put make a new folder in the instant-ngp-helper\instant-ngp\tmp directory called "images". Then start a new cmd instance, and run run.py. 
```
python run.py
```
Here you can select to run colmap with input images, an input video, run instant-ngp NeRF, or delete everything from the /tmp directory.
You will still need to confirm colmap in the command prompt.

import os
from os import listdir
from os.path import isfile, join
import run

cwd = str(os.getcwd())
path1 = cwd+'\\instant-ngp\\tmp'
path0 = cwd+'\\instant-ngp'
abab=run.aabb

videos = [f for f in listdir(path1) if isfile(join(path1, f))]
videostr = ''.join(videos)
os.chdir(path1)
command = 'python "'+path0+'\\scripts\\colmap2nerf.py" --video_in "'+videostr+'" --video_fps 2 --run_colmap --aabb_scale ' +abab
os.system(command)
print("done")

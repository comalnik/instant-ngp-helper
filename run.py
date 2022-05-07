import os
import shutil
import glob
from os import listdir
from os.path import isfile, join
print("Start the frame extraction process and run instant-ngp...")
os.system('pause')
os.system("pip install numpy")
os.system("pip install opencv-python")
cwd = str(os.getcwd())
path1 = cwd+'\\instant-ngp\\tmp'
path0 = cwd+'\\instant-ngp'
videos = [f for f in listdir(path1) if isfile(join(path1, f))]
videostr = ''.join(videos)
os.chdir(path1)
command = 'python "'+path0+'\\scripts\\colmap2nerf.py" --video_in "'+videostr+'" --video_fps 2 --run_colmap --aabb_scale 16'
os.system(command)
os.chdir(path0)
run = '"'+cwd+'\\instant-ngp\\build\\testbed" --scene tmp'
os.system(run)


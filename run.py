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
aabb = input("Enter custom aabb_scale (default-16): ")
ap1 = 16
if 16 > int(aabb) > 0:
    ap1 = aabb
command = 'python '+path0+'\\scripts\\colmap2nerf.py --video_in '+videostr+' --video_fps 2 --run_colmap --aabb_scale '+ap1
os.system(command)
os.chdir(path0)
run = cwd+'\\instant-ngp\\build\\testbed --scene tmp'
os.system(run)
x = input("Do you want to delete all files in instant-ngp\tmp folder [Y]es/[N]o: ")
xu = x.upper()
if xu == str('Y'):
    folder = path4
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('failed to delete files')

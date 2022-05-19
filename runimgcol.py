import os
import run

cwd = str(os.getcwd())
path1 = cwd+'\\instant-ngp\\tmp'
path0 = cwd+'\\instant-ngp'
imgstr = cwd+'\\instant-ngp\\tmp\\images'
abab=run.aabb

os.chdir(path1)
command = 'python "'+path0+'\\scripts\\colmap2nerf.py" --colmap_matcher exhaustive --run_colmap --aabb_scale ' +abab
os.system(command)
print("done")

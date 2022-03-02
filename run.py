import os
import shutil
import tkinter
from tkinter import *
from os import listdir
from os.path import isfile, join

print("Start the process...")
os.system('pause')

cwd = os.getcwd()
path = cwd, "\\instant-ngp\\tmp"
path1 = str(path)
path2 = path1.removeprefix("('")
path3 = path2.removesuffix("')")
path4 = path3.replace("', '", "")
mypath = path4
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
vidio = str(onlyfiles)
vidio1 = vidio.removesuffix("']")
vidio2 = vidio1.removeprefix("['")
os.chdir(path4)
peth = cwd, "\\instant-ngp" 
chpath = str(peth)
chpath1 = chpath.removeprefix("('")
chpath2 = chpath1.removesuffix("')")
chpath3 = chpath2.replace("', '", "")
command = "python ", chpath3, '\\scripts\\colmap2nerf.py --video_in ', vidio2, " --video_fps 2 --run_colmap --aabb_scale 16"
command1 = str(command)
command2= command1.removesuffix("')")
command3 = command2.removeprefix("('")
command4 = command3.replace("', '", "")
os.system(command4)


fina = cwd, "\\instant-ngp\\build\\testbed.exe --scene tmp\\images"
final = str(fina)
final1 = final.removeprefix("('")
final2 = final1.removesuffix("')")
final3 = final2.replace("', '", "")
os.system(final3)







x = input("Do you want to delete all files in tmp folder [Y]es/[N]o: ")
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

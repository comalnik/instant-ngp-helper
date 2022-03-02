import os
import subprocess
import shutil
import ctypes
import sys
from subprocess import call
cudaq = input("Do you have cuda 11.6 installed? [Y]es/[N]o: ")
cudaqu = str.upper(cudaq)
if cudaqu == str('N'):
    os.system("cuda.exe")
vsq = input("Do you have Visual Studio 2019? [Y]es/[N]o: ")
vsqu = str.upper(vsq)
if vsqu == str('N'):
    print('Make sure to install desktop development with C++! [press any key to continue]: ')
    os.system ('pause')
    os.system("vs.exe")
call(["python", "path.py"])
call(["python", "copy.py"])
os.system('git clone --recursive https://github.com/nvlabs/instant-ngp' + "&" + 'cd instant-ngp' + "&" + 'C:\\"Program Files (x86)"\\"Microsoft Visual Studio"\\2019\\Community\\Common7\\Tools\\VsDevCmd.bat' + "&" + 'cmake . -B build' + "&" + 'cmake --build build --config RelWithDebInfo -j 16' )
call(["python", "run.py"])
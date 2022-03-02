import os
import subprocess
import shutil
import ctypes
import sys
cudaq = input("Do you have cuda installed? [Y]es/[N]o: ")
cudaqu = str.upper(cudaq)
if cudaqu == str('N'):
    os.system("cuda.exe")
vsq = input("Do you have Visual Studio 2019? [Y]es/[N]o: ")
vsqu = str.upper(vsq)
if vsqu == str('N'):
    print('Make sure to install desktop development with C++! [press any key to continue]: ')
    os.system ('pause')
    os.system("vs.exe")
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    folder1 = "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.6\\extras\\visual_studio_integration\\MSBuildExtensions"
    folder2 = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\MSBuild\\Microsoft\\VC\\v160\\BuildCustomizations"
    files_in_src = os.listdir(folder1)
    for file_name in files_in_src:
        full_file_name = os.path.join(folder1, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, folder2)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
os.system('git clone https://github.com/NVlabs/instant-ngp.git' + "&" + 'cd instant-ngp' + "&" + 'C:\\"Program Files (x86)"\\"Microsoft Visual Studio"\\2019\\Community\\Common7\\Tools\\VsDevCmd.bat' + "&" + 'cmake . -B build' + "&" + 'cmake --build build --config RelWithDebInfo -j 16' )

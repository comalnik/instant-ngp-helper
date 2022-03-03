import subprocess
import os
import sys
import shutil
import ctypes
from subprocess import call
cwd = os.getcwd()
pthf1 = 'setx /m PATH "', cwd, '\\ffmpeg\\bin;%PATH%"'
pthf2 = str(pthf1)
pthf3 = pthf2.removeprefix("('")
pthf4 = pthf3.removesuffix("')")
pthf5 = pthf4.replace("', '", "")
pthc1 = 'setx /m PATH "', cwd, '\\COLMAP;%PATH%"'
pthc2 = str(pthc1)
pthc3 = pthc2.removeprefix("('")
pthc4 = pthc3.removesuffix("')")
pthc5 = pthc4.replace("', '", "")
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    os.system(pthf5)

    os.system(pthc5)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

path = cwd, "\\instant-ngp\\tmp"
path1 = str(path)
path2 = path1.removeprefix("('")
path3 = path2.removesuffix("')")
path4 = path3.replace("', '", "")
os.mkdir(path4)
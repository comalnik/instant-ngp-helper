import subprocess
import os
import sys
cwd = os.getcwd()
pthf1 = 'setx path "', cwd, '\\ffmpeg\\bin"'
pthf2 = str(pthf1)
pthf3 = pthf2.removeprefix("('")
pthf4 = pthf3.removesuffix("')")
pthf5 = pthf4.replace("', '", "")
os.system(pthf5)
pthc1 = 'setx path "', cwd, '\\COLMAP"'
pthc2 = str(pthc1)
pthc3 = pthc2.removeprefix("('")
pthc4 = pthc3.removesuffix("')")
pthc5 = pthc4.replace("', '", "")
os.system(pthc5)

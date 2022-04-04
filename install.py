import os
from subprocess import call
os.system('git clone --recursive https://github.com/nvlabs/instant-ngp' + "&" + 'cd instant-ngp' + "&" + 'C:\\"Program Files (x86)"\\"Microsoft Visual Studio"\\2019\\Community\\Common7\\Tools\\VsDevCmd.bat' + "&" + 'cmake . -B build' + "&" + 'cmake --build build --config RelWithDebInfo -j 16' )
call(["python", "copy.py"])
call(["python", "path.py"])

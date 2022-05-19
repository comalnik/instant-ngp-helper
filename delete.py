import os
import shutil
cwd = str(os.getcwd())
path1 = cwd+'\\instant-ngp\\tmp'
path0 = cwd+'\\instant-ngp'
folder = path1
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('failed to delete files')
print("done")
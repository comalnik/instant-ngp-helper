import os

cwd = str(os.getcwd())
path1 = cwd+'\\instant-ngp\\tmp'
path0 = cwd+'\\instant-ngp'

os.chdir(path0)
run = '"'+cwd+'\\instant-ngp\\build\\testbed" --scene tmp'
os.system(run)
print("done")
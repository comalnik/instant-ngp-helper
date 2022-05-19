import tkinter as tk
import os
from subprocess import call
from tkinter import *

root  = tk.Tk()

canvas = tk.Canvas(root, width=1100, height=700)
canvas.grid(columnspan=4)
canvas.grid(rowspan=3)
canvas.configure(background='#2d2d30')

cwd = str(os.getcwd())
path1 = cwd+'\\instant-ngp\\tmp'
path0 = cwd+'\\instant-ngp'
aabb=16

os.system("pip install numpy")
os.system("pip install opencv-python")

def runvidcol():
    aabb=int(aabbe.get())
    if 0 < aabb < 17:
        aabb=aabbe.get()
    else:
        aabb=16
    print(aabb)

    call(["python", "runvidcol.py"])

def runimgcol():
    aabb=int(aabbe.get())
    if 0 < aabb < 17:
        aabb=aabbe.get()
    else:
        aabb=16 
    print(aabb) 

    call(["python", "runimgcol.py"])
  
def rungp():
    call(["python", "rungp.py"])

def delete():
    call(["python", "delete.py"])

runvidcol_text = tk.StringVar()
runvidcol_btn = tk.Button(root, textvariable=runvidcol_text, height=5, width=20, command=lambda:runvidcol())
runvidcol_text.set("Run colmap (video)")
runvidcol_btn.grid(column=0, row=1)

runimgcol_text = tk.StringVar()
runimgcol_btn = tk.Button(root, textvariable=runimgcol_text, height=5, width=20, command=lambda:runimgcol())
runimgcol_text.set("Run colmap (images)")
runimgcol_btn.grid(column=1, row=1)

rungp_text = tk.StringVar()
rungp_btn = tk.Button(root, textvariable=rungp_text, height=5, width=20, command=lambda:rungp())
rungp_text.set("Run instant-ngp NeRF")
rungp_btn.grid(column=2, row=1)

del_text = tk.StringVar()
del_btn = tk.Button(root, textvariable=del_text, height=5, width=40, command=lambda:delete())
del_text.set("Delete all files from the \instant-ngp\tmp dir")
del_btn.grid(column=3, row=1)

aabbl=Label( text="Enter custom aabb scale (default=16):", bg="#2d2d30", fg="white")
aabbl.grid(row=0, column=0)
aabbe=Entry(root, width=40)
aabbe.grid(row=0, column=1)

root.mainloop()







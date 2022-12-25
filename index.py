from tkinter import *
import os
import subprocess
from main import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from subprocess import call

def show():
    pro = filedialog.askopenfilename()
    #l2.config(text=pro)
    os.system('"%s"'% pro)


def open_py_file():
    call(["python", "main.py"])

def output1():
    o = subprocess.check_output(["python", "C:\\Users\\shree\\OneDrive\\Pictures\\Documents\\python assignment\\main.py>"])
    Label(root, text=o).pack()

root = Tk()
root.geometry('300x300')

l = Label(root, text = "HASHING")
l.pack()

l2 = Label(root, text="")
l2.pack()

b = Button(root, text="start" , command=show)
b.pack()

b1 = Button(root, text="output")
b1.pack()

root.mainloop()
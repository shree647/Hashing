from tkinter import *
import os
import subprocess
from main import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from subprocess import call


def show():
    pro = filedialog.askopenfilename()
    # l2.config(text=pro)
    os.system('"%s"' % pro)


def open_py_file():
    call(["python", "main.py"])


def output1():
    o = subprocess.check_output(
        ["python", "C:\\Users\\shree\\OneDrive\\Pictures\\Documents\\python assignment\\main.py>"])
    Label(root, text=o).pack()


root = Tk()
root.geometry('300x300')

l = Label(root, text="HASHING")
l.pack()

l2 = Label(root, text="")
l2.pack(pady=20)

b = Button(root, text="show the program", command=show)
b.pack(pady=20)


def run():
    output = subprocess.check_output(["python", "main.py"])
    new_window = Toplevel(root)
    new_window.title("Output")
    new_window.geometry("500x500")
    label = Label(new_window, text=output)
    label.pack()


button4 = Button(root, text="output", command=run)
button4.pack()

root.mainloop()

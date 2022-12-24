from tkinter import *
#from main import *
from subprocess import call

def open_py_file():
    call(["python", "execution.py"])

root = Tk()
root.geometry('300x300')

l = Label(root, text = "HASHING")
l.pack()

b = Button(root, text="start" , command=open_py_file)
b.pack()

b1 = Button(root, text="output" )
b1.pack()

b2 = Button(root, text="stop")
b2.pack()

root.mainloop()
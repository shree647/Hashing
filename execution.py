from  tkinter import   *
from main import insertData, removeData

root1 = Tk()
root1.geometry('300x300')

e = Entry(root1, width=50)
e.pack()
bt = Button(root1, text="insert" , command=insertData)
bt.pack()

e1 = Entry(root1, width=50)
e1.pack()
bn = Button(root1, text="remove" , command=removeData)
bn.pack()



root1.mainloop()

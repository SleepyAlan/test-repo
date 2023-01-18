# Hello World.exe
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="DON'T PRESS", command=root.destroy).grid(column=1, row=0)
ttk.Label(frm, text="By Team Sleepy").grid(column=1, row=1)
root.mainloop()

# Hello World.exe
from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    root = Tk()
    frm = ttk.Frame(root, padding=100)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="DON'T PRESS", command=root.destroy).grid(column=1, row=0)
    ttk.Label(frm, text="By Team Sleepy").grid(column=0, row=1)
    ttk.Button(frm, text="I wonder what this does!").grid(column=1, row=1)
    root.mainloop()

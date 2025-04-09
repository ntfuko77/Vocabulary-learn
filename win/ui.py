from tkinter import *
from tkinter import ttk

def test():
    root = Tk()
    root.geometry("300x200")
    frame_top = Frame(root, bg="lightblue", height=150)
    frame_top.pack(side="top", fill="x")
    ttk.Label(frame_top, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frame_top, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
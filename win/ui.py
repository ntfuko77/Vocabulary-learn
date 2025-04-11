from tkinter import *
from tkinter import ttk
import sys
sys.path.append(r'Vocabulary-learn/script')
import stack

class simple_method:
    @staticmethod
    def simple():...
    @staticmethod
    def menu():...
class left_menu:
    def __init__(self):
        self.unit={'Button':None}

    def unit_menu(self, Frame):
        buffer=ttk.Label(Frame, text="Hello World!")
        buffer.pack(side="top", fill="x")
        buffer.bind("<Button-1>", lambda event: print("Hello World!"))

def test():
    root = Tk()
    root.geometry("500x400")
    frame_top = Frame(root, bg="lightblue", height=100)
    frame_top.pack(side="top", fill="x")
    frame_left_menu = Frame(root, bg="lightgreen", width=150)
    frame_left_menu.pack(side="left", fill="y")
    ttk.Label(frame_top, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frame_top, text="Quit", command=root.destroy).grid(column=1, row=0)
    x=left_menu()
    x.unit_menu(frame_left_menu)
    
    
    root.mainloop()
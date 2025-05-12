from enum import Enum
from tkinter import *

class BaseUI(Enum):
    geometry = '600x600'
    title = 'Vocabulary Learn'

class init():
    def __init__(self):
        root = Tk()
        root.title(BaseUI.title.value)
        root.geometry(BaseUI.geometry.value)
        self.root=root
        self.top_menu()
    def top_menu(self):
        member=Menu(self.root)
        add_menu = Menu(member, tearoff=0)
        add_menu.add_command(label='Edit', command=lambda: self.insert_data_frame())
        add_menu.add_command(label='add_unit', command=lambda: print('Search'))
        member.add_cascade(label='Add..', menu=add_menu)
        member.add_command(label='Delete', command=lambda: print('Delete'))
        quiz_menu = Menu(member, tearoff=0)
        quiz_menu.add_command(label='Quiz', command=lambda: print('Quiz'))
        member.add_cascade(label='Quiz', menu=quiz_menu)
        debug_menu = Menu(member, tearoff=0)
        debug_menu.add_command(label='delete frame', command=self.kill_all_frame)
        member.add_cascade(label='Debug', menu=debug_menu)
        member.add_command(label='Quit', command=self.root.quit)

        self.root.config(menu=member)
    def kill_all_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.top_menu()
        return
    def insert_data_frame(self):
        
        label = Label(self.root, text='Insert Data')
        label.pack()
        
        name = ['Word', 'part of speech', 'Meaning:1', 'part of speech', 'Meaning:2', 'part of speech', 'unit']
        number = len(name)
        bundle = [[] for i in range(number)]
        name = zip(name, range(number))
        name = list(name)
        for i in range(number):
            bundle[i].append(Frame(self.root, padx=5 , pady=5))
            bundle[i].append(Label(bundle[i][0], text=name[i][0]))
            bundle[i][1].pack(side='left')
            bundle[i].append(Entry(bundle[i][0]))
            bundle[i][2].pack(side='left', fill='x')
            bundle[i][0].pack(side='top', fill='x')


        button = Button(self.root, text='Submit', command=lambda: print(entry.get()))
        button.pack(side='bottom')
        self.root.bind('<Return>', lambda event: print('Enter pressed'))
        return 

    def run(self):
        self.root.mainloop()






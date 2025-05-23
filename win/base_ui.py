from enum import Enum
from tkinter import *

class BaseUI(Enum):
    geometry = '600x400'
    title = 'Vocabulary Learn'
    insert_data_name = ('Word', 'part of speech 1', 'Meaning:1', 'part of speech 2', 'Meaning:2', 'part of speech 3', 'unit')
    insert_data_title = 'Insert Data'
    insert_date_unit_name = ('unit',)
    insert_date_unit_title = 'Insert Unit'

class EventTransfer():
    """Event transfer class"""
    def __init__(self,name:str,set_callback):
        self.name=name
        self.set_callback=set_callback
class MenuResponsive():
    def __init__(self):
        self.reset_eho=None
        self.recv=None
        self.event={}
    def set_eho_update_callback(self, eho:Label):
        """Set the callback function to update the label"""
        def reset_eho(eho:Label,text:str):
            eho.config(text=text)
        self.eho=reset_eho
    def set_submit_callback(self,event:EventTransfer,receive:dict):
        """Set the callback function to receive data"""
        self.recv=receive
        self.event[event.name]=event.set_callback



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
        add_menu.add_command(label='Edit', command=lambda: self.insert_data_frame(BaseUI.insert_data_name.value, BaseUI.insert_data_title.value))
        add_menu.add_command(label='add_unit', command=lambda: self.insert_data_frame(BaseUI.insert_date_unit_name.value, BaseUI.insert_date_unit_title.value))
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
    def Create_insert_data_function(self, name:list, title:str ,typesave_data_function):
        def insert_data_frame(self,name:list,title:str):
            self.kill_all_frame()
            
            label = Label(self.root, text=title)
            label.pack()
            
            number = len(name)
            bundle = [[] for i in range(number)]
            name = zip(name, range(number))
            name = list(name)
            for i in range(number):
                bundle[i].append(Frame(self.root, padx=5 , pady=5))
                bundle[i].append(Label(bundle[i][0], text=name[i][0]))
                bundle[i][1].pack(side='left')
                bundle[i].append(Entry(bundle[i][0]))
                bundle[i][2].pack(side='left', fill='x', expand=True)
                bundle[i][0].pack(side='top', fill='x')

            eho = Label(self.root)
            eho.pack()
            button = Button(self.root, text='Submit', command=lambda: print(entry.get()))
            button.pack(side='bottom')
            def get_bundle_value(name,bundle):
                out={}
                for i in range(number):
                    out[name[i][0]] = bundle[i][2].get()
                print(out)
            self.root.bind('<Return>', lambda event: get_bundle_value(name, bundle))
            return
        self.insert_data_frame = insert_data_frame
    def insert_data_frame(self,name:list,title:str):
        self.kill_all_frame()
        
        label = Label(self.root, text=title)
        label.pack()
        
        number = len(name)
        bundle = [[] for i in range(number)]
        name = zip(name, range(number))
        name = list(name)
        for i in range(number):
            bundle[i].append(Frame(self.root, padx=5 , pady=5))
            bundle[i].append(Label(bundle[i][0], text=name[i][0]))
            bundle[i][1].pack(side='left')
            bundle[i].append(Entry(bundle[i][0]))
            bundle[i][2].pack(side='left', fill='x', expand=True)
            bundle[i][0].pack(side='top', fill='x')

        eho = Label(self.root)
        eho.pack()
        button = Button(self.root, text='Submit', command=lambda: print(entry.get()))
        button.pack(side='bottom')
        def get_bundle_value(name,bundle):
            out={}
            for i in range(number):
                out[name[i][0]] = bundle[i][2].get()
            return(out)
        self.root.bind('<Return>', lambda event: print(get_bundle_value(name, bundle)))
        return 

    def run(self):
        self.root.mainloop()






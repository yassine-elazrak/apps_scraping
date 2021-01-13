from tkinter import *
from Time import Time
from file import DIR
from list_box import Box
from fieldnames import Fieldnames
from download import Bar
from exec import Run
from tkinter.messagebox import showerror


class Body:

    def __init__(self, apps, parent, list_file=[]):
        print("Home")
        self.master = parent
        self.time = Time(parent)
        self.file = DIR(parent)
        self.box = Box(parent)

    def show(self):
        self.time.main()
        self.file.main()
        self.box.main()


def __init__(self, apps, parent, list_file=[]):
    self.body = Body()
    def remove(self):
        pass

class Home:
    def __init__(self, apps, parent, list_file=[]):
        self.body = Body(apps, parent, list_file)
        self.objs = {}
        self.objs[Body] = self.body
        self.run = Run(apps, parent , list_file)

    def set_objs(self, objs):
        print("set_objs", objs)
        try:
            for key , value in objs.items():
                self.objs[key] = value 
        except :
            print("error obj")
    def show(self):
        self.body.show()
        self.run.show()
    

class Field:
    def __init__(self, apps, parent, list_file=[]):
        print("Field")
        self.master = parent
        self.fieldname = Fieldnames(parent)

    def show(self):
        self.fieldname.main()


class Download:
    def __init__(self, apps, parent, list_file=[]):
        print("Download")
        self.master = parent
        self.apps = apps
        self.index_row = 0
        self.files = list_file

    def show(self):
        # showerror("error", message="erro dowm,md")
        for file in self.files:
            self.index_row += 1
            Bar(self.master , str(file), self.index_row , self.files, self.apps)

       

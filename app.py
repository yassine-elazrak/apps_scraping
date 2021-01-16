from tkinter import *
import tkinter.font as TkFont
from page import Home, Field, Download
from clean import Clean
from nb_tweet import Nb
from visual import Visual
from tkinter.messagebox import showerror
# from fieldnames import Fieldnames
#  home   filied   down visu   nbr_tw cleandata


class Head:
    def __init__(self, parent, obj_main):
        self.font_butt = TkFont.Font(
            family='Helvetica', size=10, weight=TkFont.BOLD)
        self.master = parent
        self.obj_main = obj_main
        self.frame = LabelFrame(
            self.master, text=" Head:", fg="red", bg="#091833",
            font=("Courier", 16, "italic"))
        self.frame.grid(row=0, rowspan=1, columnspan=14,
                        sticky='WENS', padx=5, pady=0, ipadx=5, ipady=0)
        self.controller()

    def controller(self):
        self.butt_clear = Button(self.frame, text="    HOME    ", command=lambda: self.obj_main.controller(
            "Home"), font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=2, padx=5, pady=5, ipadx=5, ipady=5)
        self.butt_clear = Button(self.frame, text=" FIELDNAMES ", command=lambda: self.obj_main.controller(
            "Field"), font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=3, padx=5, pady=5, ipadx=5, ipady=5)
        self.butt_clear = Button(self.frame, text="  DOWNLOAD  ", command=lambda: self.obj_main.controller(
            "Download"), font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=4, padx=5, pady=5, ipadx=5, ipady=5)
        self.butt_clear = Button(self.frame, text=" CLEAN DATA ", command=lambda: self.obj_main.controller(
            "Clean"), font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=5, padx=5, pady=5, ipadx=5, ipady=5)
        self.butt_clear = Button(self.frame, text="   NB_TWEET  ", command=lambda: self.obj_main.controller(
            "Nb"), font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=6, padx=5, pady=5, ipadx=5, ipady=5)
        self.butt_clear = Button(self.frame, text="VISUALIZATION", command=lambda: self.obj_main.controller(
          "Visual"), font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=7, padx=5, pady=5, ipadx=5, ipady=5)


class Main:
    def __init__(self, parent):
        self.master = parent
        self.objs = {}
        self.name_file = ["1", "2", "3"]
        self.last_obj = Home
        self.frame = LabelFrame(
            self.master, text=" Main:", fg="red",
            font=("Courier", 16, "italic"))
        self.frame.grid(row=2, rowspan=20, columnspan=16,
                        sticky='WENS', padx=5, pady=0, ipadx=9, ipady=0)
        self.frame.configure(background="#091833")
        dict = {"Home":Home, "Field" : Field, "Download" :Download, "Clean": Clean,"Nb": Nb , "Visual":Visual}
        for key , obj in dict.items():
            self.objs[key] = obj(parent, self.frame, self.name_file)
        self.objs["Home"].set_objs(self.objs)
        self.objs["Home"].show()
        # self.button_run = Button(
        #     parent, text=' run ', bg='red', width=13)
        # self.button_run.grid(row=19, column=4, sticky='W')

    def remove(self):
        # self.name_file = self.objs[self.last_obj].files
        for widget in self.frame.winfo_children():
            widget.destroy()

    def controller(self, obj):
        # if obj != self.last_obj:

        self.last_obj = obj
        self.remove()
        frame = self.objs[obj]
        frame.show()

    def add(self):
        self.home.show()

    def init(self):
        self.Time(self.frame)
        self.main()


class App:
    def __init__(self, parent):
        self.master = parent
        self.obj_main = Main(parent)
        self.obj_header = Head(parent, self.obj_main)
        # Button(parent, text="remv", command = self.main.remove).grid(row=25, column=8)
        # Button(parent, text="add", command = self.main.add).grid(row=17, column=8)

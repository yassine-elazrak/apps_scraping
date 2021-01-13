from tkinter import *
import tkinter.font as TkFont


class Run:
    def __init__(self, apps, parent, list_file=[]):
        self.parent = parent
        self.font_butt = TkFont.Font(family='Helvetica', size=10, weight=TkFont.BOLD)


    def show(self):
        print("Show run")
        # self.frame = Frame(self.parent).grid(row=19, column=0)
        self.button_run = Button(
            self.parent , text='  run  ', font=self.font_butt, bg='red', width=11)
        self.button_run.grid(row=19, column=6,  padx=0, pady=5, ipadx=1, ipady=2)
        self.button_clear = Button(
            self.parent , text=' clear ', font=self.font_butt, bg='red', width=11)
        self.button_clear.grid(row=19, column=5, padx=0, pady=5, ipadx=1, ipady=2)
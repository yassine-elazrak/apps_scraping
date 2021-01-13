
from tkinter import *
from tools import Input
from functools import reduce
from pprint import pprint
import tkinter.font as TkFont

class Box:
    def __init__(self, apps=None):
        self.master = apps
        self.Words = []
        self.font_butt = TkFont.Font(family='Helvetica', size=10, weight=TkFont.BOLD)


    def add(self):
        if self.data.get() and not "      enter key search" in self.data.get():
            self.Words.append(self.data.get())
            self.list_box.insert(0, self.data.get())
            self.data.ft_delete(0, END)

    def remove(self):
        if self.Words:
            self.list_box.delete(0)
            self.Words.pop()

    def get_all(self):
        print("keys=>>", self.Words)
        return self.Words
        
    def clear_all(self):
        self.Words.clear()
        self.list_box.delete(0,END)
        self.data.ft_delete(0,END)


    def creat(self):
        self.field1 = Frame(self.fram ,bg="#091833")
        self.field1.grid(row=0, columnspan=2, sticky='w', padx=2, pady=2)
        self.field1.configure(background="#091833")
        self.field2 = Frame(self.fram ,bg="#091833")
        self.field2.grid(row=1, columnspan=2, sticky='w', padx=2, pady=2)
        self.field2.configure(background="#091833")

        self.label = Label(self.field1, text="Search :", fg="snow", bg="#f2a343" , font =("Courier", 28, "italic"))
        self.label.grid(row=0, column=0)
        self.label.configure(background="#091833")

        self.data = Input(self.field1, "      enter key search")
        self.data.grid(row=0, column=1, padx=3,pady=5, ipadx=88, ipady=11)

        self.button_add = Button(self.field2, text='   add element  ',font=self.font_butt, bg='red', command=self.add)
        self.button_add.grid(row=0, column=7,sticky='w',  padx=5,pady=1, ipadx=5, ipady=5)###
        self.button_remove = Button(
        self.field2, text=' remove element ',font=self.font_butt, bg='red', command=self.remove)
        self.button_remove.grid(row=0, column=8,sticky='W',  padx=0,pady=1, ipadx=5, ipady=5)####
#####run the
        # self.button_clear = Button(self.field2, text=' clear all ',font=self.font_butt, bg='red', command=self.add)
        # self.button_clear.grid(row=0, column=9,sticky='w',  padx=5,pady=1, ipadx=5, ipady=5)###
        # self.button_run = Button(
        # self.field2, text=' run ',font=self.font_butt, bg='red', width=13, command=self.remove)
        # self.button_run.grid(row=0, column=10,sticky='W',  padx=7,pady=2, ipadx=5, ipady=5)####

        self.field2 = Frame(self.fram,bg="#091833")
        self.field2.grid(row=0, column=5, columnspan=2, rowspan=3, \
                sticky='NS', padx=1, pady=1)
        self.list_box = Listbox(self.field2, height=4,
                                width=18,
                                bg="#f2a343",
                                activestyle='dotbox',
                                font="Helvetica",
                                fg="gray44")
        self.list_box.grid(row=0, column=7)

    def main(self):
        self.fram = LabelFrame(
            self.master, text=" Enter Details For Words Search :" ,fg = "red",
		  font =("Courier", 26, "italic"))
        self.fram.grid(row=5, columnspan=7, sticky='W', padx=5, pady=0, ipadx=5, ipady=4)
        self.fram.configure(background="#091833")

        self.creat()

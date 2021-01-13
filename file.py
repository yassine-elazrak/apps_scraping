from tkinter import *
from pprint import pprint
from tools import Input
from os import path
import os
from tkinter import filedialog
import tkinter.font as TkFont
# from main import apps

class DIR:
    def __init__(self, apps=None):
        self.master=apps
        self.var_csv = IntVar()
        self.var_json = IntVar()
        self.dir = StringVar() 
        self.dir.set(os.getcwd())
        self.font_butt = TkFont.Font(family='Helvetica', size=10, weight=TkFont.BOLD)

      
    def ft_name_file(self):#########
        Label(self.fram, text="Name Of File Output  ", bg="#f2a343" , font =("Courier", 15, "italic")).grid(row=2, column=0, columnspan=4 ,sticky='w', padx=5, pady=2)
        self.name_file=Input(self.fram, "      name file")
        self.name_file.grid(row=2, column=5, columnspan=4 ,padx=3,pady=5, ipadx=88, ipady=11)

    def test_dir(self, data):
        return path.isdir(data)

    def get_dir(self):#########
        name = filedialog.askdirectory(initialdir = "/",title = "Select directory file output")
        if name:
            self.dir.set(name)
        else:
            self.dir.set(os.getcwd())


    def ft_path(self):
        Label(self.fram, text="Directory Of File", bg="#f2a343" , font =("Courier", 15, "italic")).grid(row=0, column=0, columnspan=4 ,sticky='w', padx=5, pady=2)
        self.buton_change = Button(self.fram, text="change path", command=self.get_dir,font=self.font_butt, bg='red', width=16)
        self.buton_change.grid(row=0, column=7, columnspan=2, padx=5, pady=2, ipadx=5, ipady=5)
        Label(self.fram, textvariable=self.dir, bg="#f2a343" , font =("Courier", 15, "italic")).grid(row=1, column=0, columnspan=6, sticky='w', padx=5, pady=2) 
        
    def clear_all(self):
        self.name_file.ft_delete(0, END)
        self.dir.set(os.getcwd())
        self.var_json.set(0)
        self.var_csv.set(0)

    def change_csv(self):####hello
        if self.var_json.get() == 1:
            self.var_json.set(0)

    def change_json(self):
        if self.var_csv.get() == 1:
            self.var_csv.set(0)

    def box_type_file(self):
        Checkbutton(self.fram, text=str("Format csv ") ,variable=self.var_csv, command=self.change_csv, bg="bisque" , font =("Courier", 14, "italic")).grid(row=3, column=0, padx=0, pady=0)
        Checkbutton(self.fram, text=str("Format josn") ,variable=self.var_json, command=self.change_json, bg="bisque" , font =("Courier", 14, "italic")).grid(row=3, column=5,columnspan=2, padx=0, pady=0)
        self.var_csv.set(1)
        

    def get_all(self):
        path_file = "."
        name_file = "tweets_twitter"
        path_file = self.dir.get()
        if  self.name_file.get() and  not "name file" in self.name_file.get() :
            name_file = self.name_file.get()
        if self.var_json.get() == 1:
            path_file = path_file + "/" + name_file + ".json"
        else:
            path_file = path_file + "/" + name_file + ".csv"
        return path_file
        
    def main(self):
        self.fram = LabelFrame(self.master, text=" Enter Details For Output :" ,fg = "red", font =("Courier", 26, "italic"))
        self.fram.grid(row=2, columnspan=8, sticky='w', \
                 padx=1, pady=1, ipadx=1, ipady=4)
        self.fram.configure(background="#091833")   
        self.ft_name_file()
        self.ft_path()
        self.box_type_file()

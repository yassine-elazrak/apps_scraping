
from tkinter import *
from tools import Input
from functools import reduce
from pprint import pprint
import tkinter.font as TkFont
# import tkinter.font 
# import tkinter
# import tkFont
# import tkinter.font as TkFont

# helv36 = TkFont.Font(family='Helvetica', size=36, weight=TkFont.BOLD)
class Fieldnames(Frame):

    def __init__(self, apps):
        Frame.__init__(self, apps)
        self.vars = []
        self.font_butt = TkFont.Font(family='Helvetica', size=10, weight=TkFont.BOLD)
        self.fieldnames = [[
            "created_at",
            "date"
                ,
            "time",
            "username"
        ],
        [
            "name",
            "place"
        ,
            "tweet",
            "language"
        ],
        [
            "mentions",
            "urls"
       ,
            
            "likes_count"
            ,"retweet"
        ], [
            "hashtags",
            "cashtags"
        ,
            "retweets_count",
            "link"
            ],
        [
            "thumbnail",
            "near"
         ,
            "retweet_id",
            "reply_to"
            ],
        [
            "retweet_date",
            "translate","retweet_date",
            "translate"
            ]
        ]

        self.keys = reduce(lambda i, j: i + j, self.fieldnames)
        self.fields = []

    def creat(self):
        index = 0
        for name in self.fieldnames:
            self.field1 = Frame(self.fram,bg="#091833")
            self.field1.grid(row=index, columnspan=8, sticky='w', padx=2, pady=4)  
            var = IntVar()
            box = Checkbutton(self.field1, text=str(name[0]) ,variable=var,bg="#091833", fg = "purple", font =("Courier", 12, "italic"))
            box.pack(side=LEFT)
            self.vars.append(var)
            var = IntVar()
            box = Checkbutton(self.field1, text=str(name[1]) ,variable=var,bg="#091833", fg = "purple", font =("Courier", 12, "italic"))
            box.pack(side=LEFT)
            self.vars.append(var)

            var = IntVar()
            box = Checkbutton(self.field1, text=str(name[2]) ,variable=var,bg="#091833", fg = "purple", font =("Courier", 12, "italic"))
            box.pack(side=LEFT)
            self.vars.append(var)
            var = IntVar()
            box = Checkbutton(self.field1, text=str(name[3]) ,variable=var,bg="#091833", fg = "purple", font =("Courier", 12, "italic"))
            box.pack(side=LEFT)
            self.vars.append(var)
            index += 1
        self.butt_set = Button(self.fram, text=  "set all       " ,font=self.font_butt, command=self.set_all, bg = "red" ,width=13)
        self.butt_set.grid(row=15, column=0 , padx=5,pady=5, ipadx=5, ipady=5)
        self.butt_clear = Button(self.fram, text="clear all     ",font=self.font_butt, command=self.clear_all, bg = "red" ,width=13)
        self.butt_clear.grid(row=15, column=1, padx=5,pady=5, ipadx=5, ipady=5)

    def ft_map(self):
        index = 0
        for Variable in self.vars:
            if Variable.get() == 1:
                self.fields.append(self.keys[index])
            index += 1

    def get_all(self):
        self.ft_map()
        pprint(self.vars)
        if not self.fields:
            return self.keys
        return self.fields

    def set_all(self):
         for var in self.vars:
            var.set(1)

    def clear_all(self):
        for var in self.vars:
            var.set(0)
        

    def main(self):
        self.fram = self.master
        # = LabelFrame(self.master, text="Enter Fieldnames:" ,bg="#091833" ,fg = "red",
		#   font =("Courier",22, "italic"))
        # self.fram.grid(row=4, columnspan=8, rowspan=12, \
        #         sticky='W', padx=5, pady=5)

        self.creat()

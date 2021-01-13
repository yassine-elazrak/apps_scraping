from tkinter import *
from  tools import Input
import tkinter.font as TkFont

class Nb:
    def __init__(self, apps, parent, list_file=[]):
        print("nembers")
        self.parent = parent
        self.nb = IntVar()
        self.font_butt = TkFont.Font(
            family='Helvetica', size=10, weight=TkFont.BOLD)



    def show(self):
        Label(self.parent, text="Enter Number Tweets :", bg="#f2a343" , font =("Courier", 15, "italic")).grid(row=2, column=0, columnspan=4 ,sticky='w', padx=5, pady=2)
        self.name_file=Input(self.parent, "      enter number tweets ")
        self.name_file.grid(row=2, column=4, columnspan=4 ,padx=13,pady=5, ipadx=12, ipady=9)

        Checkbutton(self.parent, text=str(" all tweet "), variable=self.nb, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=2, column=12, padx=18, pady=6, ipadx=5, ipady=5)

        self.save_download = Button(
            self.parent, text=" Save Change", font=self.font_butt, bg="red", width=13)
        self.save_download.grid(row=3, column=0, padx=5,
                                pady=5, ipadx=6, ipady=5)
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showerror
from app import App
from tkinter.messagebox import showerror
# import urllib2

# def internet_on():
#     try:
#         response=urllib2.urlopen('http://74.125.228.100',timeout=20)
#         return True
#     except urllib2.URLError as err: pass
#     return False
# def report_callback_exception(self, exc, val, tb):
#         showerror("Error", message=str(val))

# app = Tk()
# tk.Tk.report_callback_exception = report_callback_exception
    # now method is overridden



    # fg= "steel blue"  "#f2a343" "bg#d9d9d9" "#c60000"
# pyinstaller.exe --onefile -w --hiddenimport=babel.numbers
# pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
# pyinstaller --onefile --windowed --icon assets\zahlen_und_code.icn main.py
# 
### pyinstaller --onefile --windowed part_manager.py
### pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py


####key___["Royal Air Maroc" , "@RAM_Maroc",    "@RAM_Maroc", \
#   "royalairmaroc", "الخطوط المغربيه" , "#الخطوط_الملكية_المغربية "\
#  , "الخطوط الملكية المغربية"    , "لارام",  " لارام"\
# ,"الخطوط_الملكية_المغربية" ]
# pip3 install https://github.com/pyinstaller/pyinstaller/archive/develop.zip


#### https://medium.com/analytics-vidhya/how-to-determine-the-optimal-k-for-k-means-708505d204eb
app = tk.Tk()


def main():
    root = App(app)


if __name__ == '__main__':
    app.geometry('850x640+0+0')
    app.configure(background="#091833")
    app.title('hello new word')
    main()
    app.mainloop()

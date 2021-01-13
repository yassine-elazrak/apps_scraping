from tkinter import *
import tkinter as tk
from tkinter.messagebox import showerror
from app import App

# def report_callback_exception(self, exc, val, tb):
#         showerror("Error", message=str(val))

# app = Tk()
# tk.Tk.report_callback_exception = report_callback_exception
    # now method is overridden
app = tk.Tk()


def main():
    root = App(app)


if __name__ == '__main__':
    app.geometry('850x640+0+0')
    app.configure(background="#091833")
    app.title('hello new word')
    main()
    app.mainloop()

from tkinter import *
from tkinter import ttk
from random import randint

class Bar:
    def __init__(self, apps, name_file, row, list_file, root, download):
        self.apps = apps
        self.root = root
        self.download= download
        self.fr = Frame(apps, bg="#091833")
        self.fr.pack(side="top", fill="both", expand=False)
        self.fr.grid_rowconfigure(0, weight=1)
        self.fr.grid_columnconfigure(0, weight=1)
        self.flag = True
        Label(self.fr, text=name_file).grid(
            row=0, column=0, padx=3, pady=2, ipadx=2, ipady=1)
        self.progress = ttk.Progressbar(self.fr, orient="horizontal",
                                        length=300, mode='determinate')
        self.progress.grid(row=0, column=3, padx=33, pady=2, ipadx=22, ipady=1)
        self.bytes = 0
        self.step = 30
        self.maxbytes = 0
        self.progress.start()
        # self.cancle = Button(self.fr, text="stop ", command=self.stop)
        # self.cancle.grid(row=0, column=6, padx=4, pady=2, ipadx=22, ipady=1)
        self.remove = Button(self.fr, text="cancle", command=self.remove)
        self.remove.grid(row=0, column=7, padx=2, pady=2, ipadx=22, ipady=1)
        # self.start()
        print("download  ====>> ")


    def start(self):
        self.progress["value"] = 0
        self.maxbytes = 5000000
        self.progress["maximum"] = 5000000
        self.read_bytes()

    def read_bytes(self):
        if self.flag:
            self.bytes += randint(45, 555555)  # self.step
            self.progress["value"] = self.bytes
            if self.bytes < self.maxbytes:
                self.root.after(1000, self.read_bytes)
            else:
                self.progress["value"] = 0
                self.bytes = 0
                self.root.after(1000, self.read_bytes)

    def stop(self):
        print("Stopping bar")
        if self.flag:
            self.progress.stop()
            self.flag = False

    def remove(self):
        self.download.DictFiles[name_file] = -1
        self.stop()
        for widget in self.fr.winfo_children():
            widget.destroy()
        self.fr.destroy()

    def ok(self, name_file):
        self.progress["value"] = 5000000


# class ManageDown:
#     def __init__(self, apps, parent, list_file=[]):
#         self.master = parent
#         self.apps = apps
#         self.index_row = 0
#         self.files = list_file

#     def init_win(self):
#         for file in self.files:
#             self.index_row += 1
        # Bar(self.master , str(file), self.index_row , files, self.apps)
    # def add_one(self , name_file):
    #     self.files.append(name_file)

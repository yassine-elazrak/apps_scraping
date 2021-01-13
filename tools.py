from tkinter import *
# from ft_twint import Config_twint , File
from pprint import pprint
from threading import Timer, Thread
from tkinter.messagebox import *
import os
from tempfile import TemporaryDirectory 
from pathlib import Path
from touch import touch 
import tkinter.font as TkFont
import shutil
import pandas as pd
import csv
from tkinter import ttk

class Input(Entry):
    def __init__(
        self,
        master=None,
        placeholder="PLACEHOLDER",
        color="grey",
        color_error="red3",
        test=None ,
    ):
        super().__init__(master)
        self["bg"] = "snow"
        self["fg"] = "blue"
        # height=100)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self["fg"]
        self.color_error = color_error
        self.func_test = test
        self.data_is_valid = False
        self.cursor = False
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)
        self.bind("<KeyRelease>", self.release)
        self.put_placeholder()


    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self["fg"] = self.placeholder_color

    def foc_in(self, *args):
        self.cursor = True
        if self["fg"] == self.placeholder_color:
            self.delete("0", "end")
            self["fg"] = self.default_fg_color

    def ft_delete(self, *args):
        self.delete(*args)
        if not self.cursor:
            self.put_placeholder()

    def release(self, *args):
        if self.func_test is not None:
            if not self.func_test(self.get()):
                self["fg"] = self.color_error
                self.data_is_valid = False
            else:
                self["fg"] = self.default_fg_color
                self.data_is_valid = True

    def foc_out(self, *args):
        self.cursor = False
        if not self.get():
            self.put_placeholder()
       
# class BUTTON(Button):
#     def __init__(self, *args):
# #         super.__init__(*args)


# class DIR:
#     def __init__(self, list_file=[]):
#         self.list_file = list_file
#         self.name = ".files"
#         os.makedirs(self.name,exist_ok=True)


#     def __enter__(self):
#         return self.name
        
#     def __exit__(self,exc_type, exc_value, traceback):
#         # os.rmdir(self.name)
#         shutil.rmtree(self.name)
#         # pass

# class Bar:

#     def __init__(self, apps=None):
#         self.apps = apps
#         self.progress = ttk.Progressbar(self.apps, orient="horizontal",
#                                         length=600, mode='determinate')
#         self.progress.grid(row=8, column=3)
#         self.bytes = 0
#         self.step = 30
#         self.maxbytes = 0
#         self.progress.start()

#     def start(self):
#         self.progress["value"] = 0
#         self.maxbytes = 50000
#         self.progress["maximum"] = 50000
#         self.read_bytes()

#     def read_bytes(self):
#         '''simulate reading 500 bytes; update progress bar'''
#         self.bytes += self.step
#         self.progress["value"] = self.bytes
#         if self.bytes < self.maxbytes:
#             # read more bytes after 10 ms
#             self.apps.after(2, self.read_bytes)
#         else:
#             self.progress["value"] = 0
#             self.bytes  = 0
#             self.apps.after(2, self.read_bytes)

#     def stop(self):
#         print("Stopping bar")
#         self.progress.stop()
#         self.progress.destroy()


# class Run:
#     def __init__(self, apps=None, date=None, path=None, box=None, arena=None):
#         self.master = apps
#         self.date = date
#         self.path = path
#         self.box = box
#         self.arena = arena
#         self.keys = []
#         self.custom = []
#         self.since = ""
#         self.until = ""
#         self.name_file = ""
#         self.list_thread = []
#         self.list_file = []
#         self.list_time = []
#         self.start = True
#         self.font_butt = TkFont.Font(family='Helvetica', size=10, weight=TkFont.BOLD)

       
      

#     def get_all(self):
#        self.since, self.until =  self.date.get_all()
#        self.name_file =  self.path.get_all()
#        self.custom =  self.box.get_all()
#        self.keys =  self.arena.get_all()
#     #    self.clear_all()



#     def clear_all(self):
#         self.date.clear_all()
#         self.path.clear_all()
#         self.box.clear_all()
#         self.arena.clear_all()
#         # self.list_time.clear()
#         # self.list_file.clear()
#         # self.
#         self.keys = []
#         self.custom = []
#         self.since = ""
#         self.until = ""
#         self.name_file = ""
#         self.list_thread = []
#         self.list_file = []
#         self.list_time = []
#         self.start = True

#     def exec(self):
#         for thread in self.list_thread:
#             thread.start()

#     def my_job(self, keys, since, until , outfile):
#         # print("my_job keys=>", keys)
#         # print("my_job since=>", since)
#         # print("my_job until=>", until)
#         # print("my_job outfile=>", outfile)
#         self.twint = Config_twint(keys=keys , since=since , \
#             until=until, outfile=outfile)
#         self.twint.run()

#     def join_files(self):
#         list_df = []
#         for name_file in self.list_file:
#             df  = pd.read_csv(name_file)
#             list_df.append(df)
        
#         df_all = pd.concat(list_df)
#         pd.csv_to(self.name_file)


#     def update_time(self):
#         self.list_time.append(self.since)
#         since, self.since = self.since.split("-", 1)
#         until , _ = self.until.split("-", 1)
#         self.diff_time = int(until) - int(since)
#         for i in range(1 , self.diff_time):
#             self.list_time.append(str(int(since) + i) + "-" + self.since)
#         self.list_time.append(self.until)
#         print("list_time",  self.list_time)

#     def wait_thread(self):
#         for thread in self.list_thread:
#             thread.join()
#         self.list_thread.clear()
#         self.start = True
#         print("\n\n\n\n\n   finish thread    \n\n\n\n")
#         File(self.list_file,self.name_file, self.custom).sum_file()
#         self.clear_all()
#         # self.bar.stop()

#     def task_thread(self):
#         self.get_all()
#         self.update_time()
#         header = ["id","conversation_id","created_at","date","time","timezone","user_id","username","name","place","tweet","language","mentions","urls","photos",\
#             "replies_count","retweets_count","likes_count","hashtags",\
#                 "cashtags","link","retweet","quote_url","video","thumbnail","near","geo","source",\
#                 "user_rt_id","user_rt","retweet_id","reply_to","retweet_date","translate","trans_src","trans_dest"]
#         with  DIR() as temp_dir:
#             for i in range(0, len(self.list_time) - 1):
#                 self.since = self.list_time[i]
#                 self.until = self.list_time[i + 1]
#                 for key in self.keys:
#                     name_file = self.since + key + ".csv"
#                     name_path =  os.path.join(temp_dir , name_file)
#                     name_path = name_path.replace(" ","_").replace(":","_")
#                     touch(name_path)
#                     with open(name_path,'a+') as file_csv:
#                         head = csv.DictWriter(file_csv, fieldnames=header)
#                         head.writeheader()
#                     self.list_file.append(name_path)

#                     self.list_thread.append(Thread(target=self.my_job, args=[[key] , self.since , \
#                         self.until, name_path ]))
#             self.list_time.clear()
#             self.exec()
#             print("\\n\n\n\n\nend --------  threading         ")
#             self.wait_thread()
            
    
#     def run(self):
#         if self.start == True:
#             self.start = False
#             th = Thread(target=self.task_thread).start()
#             # th.join()
#             print("join")
#             # self.bar = Bar(self.master)
#             # self.bar.start()
#         else:
#             print("waitng  is not finish frsit search\n")

        

            

#     def creat(self):
#         self.buton = Frame(self.master, bg="#091833")
#         self.buton.grid(row=8, columnspan=13, rowspan=3, sticky="SE")
#         self.buton_clear = Button(
#             self.buton, text="clear",font=self.font_butt, command=self.clear_all, bg="red", width=14
#         )
#         self.buton_clear.grid(row=2, column=12, padx=5,pady=2, ipadx=5, ipady=5)
#         self.buton_run = Button(self.buton, text="run",font=self.font_butt,bg="red", command=self.run, width=14)
#         self.buton_run.grid(row=2, column=14, padx=5, pady=2, ipadx=5, ipady=5)

#     def main(self):
#         # Error("hello error test")
#         self.creat()























# class Error:
#     def __init__(self, message="error try again"):
#         # root = Tk()
#         # root.withdraw()
#         # showerror(title = "Error", message=message)
#         # import tkMessageBox
 
#        messagebox.showinfo("Title", "a Tk MessageBox")
        # root.destroy()


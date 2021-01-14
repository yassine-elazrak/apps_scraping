from tkinter import *
import tkinter.font as TkFont
from tkinter import *
from scraping import Config_twint, File
from pprint import pprint
from threading import Timer, Thread
from tkinter.messagebox import *
import os
from tempfile import TemporaryDirectory
from pathlib import Path
from touch import touch
import shutil
import pandas as pd
import csv
from tkinter import ttk
import  sys


class Run:
    def __init__(self, apps, parent, list_file=[]):
        self.parent = parent
        self.root = apps
        self.objs = {}
        self.threads = []
        self.index = 0
        # self.index_file = 0
        print("Running\n\n\n")
        self.font_butt = TkFont.Font(
            family='Helvetica', size=10, weight=TkFont.BOLD)

    def show(self):
        print("Show run")
        # self.frame = Frame(self.parent).grid(row=19, column=0)
        self.button_run = Button(
            self.parent, text='  run  ', command=self.test, font=self.font_butt, bg='red', width=11)
        self.button_run.grid(row=19, column=6,  padx=0,
                             pady=5, ipadx=1, ipady=2)
        self.button_clear = Button(
            self.parent, text=' clear ', font=self.font_butt, bg='red', width=11)
        self.button_clear.grid(row=19, column=5, padx=0,
                               pady=5, ipadx=1, ipady=2)

    def set_objs(self, objs):
        self.objs = objs
        print("set_objs", self.objs)
   

    def test(self):
        self.index += 1
        # self.index_file += 1
        Exec(self.objs, self.index).run()###.join()
        # self.since, self.until =  self.objs["Home"].body.time.get_all()
        # print("date",self.objs["Home"].body.time.get_all())
        # print("file" , self.objs["Home"].body.file.get_all())
        # print("box" , self.objs["Home"].body.box.get_all())
        # print("filed" , self.objs["Field"].fieldname.get_all())

        # self.name_file =  self.path.get_all()
        # self.custom =  self.box.get_all()
        # self.keys =  self.arena.get_all()


class Exec:
    def __init__(self, objs={}, index=0):
        self.date = objs["Home"].body.time
        self.path = objs["Home"].body.file
        self.box = objs["Field"].fieldname
        self.arena = objs["Home"].body.box
        self.download = objs["Download"]
        self.keys = []
        self.custom = []
        self.since = ""
        self.until = ""
        self.name_file = ""
        self.list_thread = []
        self.list_file = []
        self.list_time = []
        self.start = True
        # self.index_folder = id_folder
        self.index = index

    def get_all(self):
        self.since, self.until = self.date.get_all()
        self.name_file = self.path.get_all()
        self.custom = self.box.get_all()
        self.keys = self.arena.get_all()
    #    self.clear_all()

    def clear_all(self):
        self.date.clear_all()
        self.path.clear_all()
        self.box.clear_all()
        self.arena.clear_all()
        # self.list_time.clear()
        # self.list_file.clear()
        # self.
        self.keys = []
        self.custom = []
        self.since = ""
        self.until = ""
        self.name_file = ""
        self.list_thread = []
        self.list_file = []
        self.list_time = []
        self.start = True

    def exec(self):
        for thread in self.list_thread:
            thread.start()

    def my_job(self, keys, since, until, outfile):
        print("my_job keys=>", keys)
        print("my_job since=>", since)
        print("my_job until=>", until)
        print("my_job outfile=>", outfile)

        self.twint = Config_twint(keys=keys , since=since , \
            until=until, outfile=outfile)
        self.twint.run()
        

    def join_files(self):
        list_df = []
        try:
            for name_file in self.list_file:
                df = pd.read_csv(name_file)
                list_df.append(df)

            df_all = pd.concat(list_df)
            pd.csv_to(self.name_file)
        except :
            print("error in pandas join file]n]n]nn\n\n\n\n\n")

    def update_time(self):
        self.list_time.append(self.since)
        since, self.since = self.since.split("-", 1)
        until, _ = self.until.split("-", 1)
        self.diff_time = int(until) - int(since)
        for i in range(1, self.diff_time):
            self.list_time.append(str(int(since) + i) + "-" + self.since)
        self.list_time.append(self.until)
        print("list_time",  self.list_time)

    def wait_thread(self):
        # try:
        for thread in self.list_thread:
            thread.join()
        self.list_thread.clear()
        self.start = True
        # except:
        #     print("error threading")
            ##########
        print("\n\n\n\n\n   finish thread    \n\n\n\n")
        File(self.list_file, self.name_file, self.custom).sum_file()
        self.download.ft_push(self.name_file , 0)
        self.clear_all()

        # self.bar.stop()
    # def ft_exit(self):
    #     print("\n\n\n\n\n hello world yassine")
    #     exit()
    def task_thread(self):
        
        self.get_all()
        self.download.ft_push(self.name_file , 1)
        self.update_time()
        header = ["id", "conversation_id", "created_at", "date", "time", "timezone", "user_id", "username", "name", "place", "tweet", "language", "mentions", "urls", "photos",
                  "replies_count", "retweets_count", "likes_count", "hashtags",
                  "cashtags", "link", "retweet", "quote_url", "video", "thumbnail", "near", "geo", "source",
                  "user_rt_id", "user_rt", "retweet_id", "reply_to", "retweet_date", "translate", "trans_src", "trans_dest"]
        
        with DIR(self.index) as temp_dir:
            print("\n\n\n\n id=>", self.index)
            for i in range(0, len(self.list_time) - 1):
                self.since = self.list_time[i]
                self.until = self.list_time[i + 1]
                for key in self.keys:
                    name_file = self.since + key + ".csv"
                    name_path = os.path.join(temp_dir, name_file)
                    name_path = name_path.replace(" ", "_").replace(":", "_")
                    touch(name_path)
                    with open(name_path, 'a+') as file_csv:
                        head = csv.DictWriter(file_csv, fieldnames=header)
                        head.writeheader()
                    self.list_file.append(name_path)
                    print("threading keys==> ", key)
                    self.list_thread.append(Thread(target=self.my_job, args=[[key] , self.since , \
                        self.until, name_path ]))
            self.list_time.clear()
            self.exec()
            print("\\n\n\n\n\nend --------  threading         ")
            self.wait_thread()

    def run(self):
        # if self.start == True:
        #     self.start = False
        th = Thread(target=self.task_thread).start()
        # th.join()
        print("join")
            # self.bar = Bar(self.master)
            # self.bar.start()
        # else:
        #     print("waitng  is not finish frsit search\n")
        return th


class DIR:
    def __init__(self, index=0,list_file=[]):
        self.list_file = list_file
        self.name = ".files" + '_' + str(index)
        os.makedirs(self.name, exist_ok=True)

    def __enter__(self):
        return self.name

    def __exit__(self, exc_type, exc_value, traceback):
        # os.rmdir(self.name)
        shutil.rmtree(self.name)

    # def creat(self):
    #     self.buton = Frame(self.master, bg="#091833")
    #     self.buton.grid(row=8, columnspan=13, rowspan=3, sticky="SE")
    #     self.buton_clear = Button(
    #         self.buton, text="clear",font=self.font_butt, command=self.clear_all, bg="red", width=14
    #     )
    #     self.buton_clear.grid(row=2, column=12, padx=5,pady=2, ipadx=5, ipady=5)
    #     self.buton_run = Button(self.buton, text="run",font=self.font_butt,bg="red", command=self.run, width=14)
    #     self.buton_run.grid(row=2, column=14, padx=5, pady=2, ipadx=5, ipady=5)

    # def main(self):
    #     # Error("hello error test")
    #     self.creat()

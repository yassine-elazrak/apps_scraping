# try:
import twint
import datetime
import pandas as pd
from tkinter.messagebox import showerror
import csv
# except RuntimeError:
#     import sys; sys.exit() from threading import Timer, Thread
from tkinter.messagebox import showerror

class File:
    def __init__(self, list_file=[],name_file="", custom = [] , nb=100):
        self.list_file = list_file
        self.name_file = name_file
        self.custom = custom
        self.nb = nb

    def sum_file(self):
        header = ["id", "conversation_id", "created_at", "date", "time", "timezone", "user_id", "username", "name", "place", "tweet", "language", "mentions", "urls", "photos",
                  "replies_count", "retweets_count", "likes_count", "hashtags",
                  "cashtags", "link", "retweet", "quote_url", "video", "thumbnail", "near", "geo", "source",
                  "user_rt_id", "user_rt", "retweet_id", "reply_to", "retweet_date", "translate", "trans_src", "trans_dest"]
        try:
            list_csv = []
            for f in self.list_file:
                df = pd.read_csv(f)
                print("name  ", df.shape, df.shape[0],"\n\n\n")
                if df.shape[0] > 1:
                    list_csv.append(df)
            data_csv = pd.concat(list_csv)
            if len(self.custom) != 22:
                data_csv = data_csv[self.custom]
            if self.nb >= 0:
                data_csv.head(self.nb).to_csv(self.name_file , index=False )
            else:
                data_csv.to_csv(self.name_file , index=False )

        except Exception as e:
            with open(self.name_file, 'w') as file_csv:
                        head = csv.DictWriter(file_csv, fieldnames=header)
                        head.writeheader()
                        showerror("Error file %s" % self.name_file , " not data found ")
            # print("\n\n\nError pandass yassine ", e)


class Config_twint:
    def __init__(self, keys=[], since="2018-12-29",until="2019-01-01", outfile="tweets33", number_tweet=100):
        print("\n\n\n\n\\nyassine  ttkeys ", keys)
        print("ttsince ", since)
        print("ttuntil ", until)
        print("ttoutfile", outfile)
        print("number_tweet", number_tweet)
        print("\n\n\n\n\n\n\n")
  
        try:
            self.c = twint.Config()
            self.c.Search = keys
            self.c.Since = since
            self.c.Until = until

            # self.c.Search = ["RAM_Maroc"]#keys
            # self.c.Since = "2019-11-01" ##since
            # self.c.Until = "2019-11-09" #until

            if number_tweet >= 0:
                self.c.Limit = number_tweet
            self.c.Store_csv = True
            self.c.Output = outfile
            self.c.Hide_output = True
        except :
            showerror("error config twint", message=" parameter not valid")
            return


    def run(self):
        twint.run.Search(self.c)




# def main():
#     run = Config_twint(keys=["RAM_Maroc"])
#     run.run()
# if __name__ == "__main__":
#     main()

# import twint

# c = twint.Config()
# c.Username = "noneprivacy"
# c.Limit = 100
# c.Store_csv = True
# c.Output = "none.csv"
# c.Lang = "en"
# # c.Translate = True
# # c.TranslateDest = "it"
# twint.run.Search(c)
# list_file = [ ".files/2017-11-23 12:00:00RAM_Maroc.csv",".files/2018-11-23 12:00:00RAM_Maroc.csv",\
#     ".files/2019-11-23 12:00:00RAM_Maroc.csv" ,".files/2019-12-27 12:00:00RAM_Maroc.csv" ]
# File(list_file,"./data_all.csv").sum_file()
# combined_csv = pd.concat( [ pd.read_csv(f) for f in list_file] )
# combined_csv.to_csv( "combined_csv.csv", index=False )
# out = open("out_all.csv", 'a')
# for line in open(list_file[0]):
#     out.write(line)
# for i in range(1, len(list_file)):
#     data = open(list_file[i], "r+")
#     data.__next__()
#     for line in  data:
#         out.write(line)
#     data.close()
# out.close()
# with open("lolo.csv", 'a') as out:
#     for name in list_file:
#         with open(name, 'r+') as data:
#             data.__next__()
#             for line in data:
#                 out.write(line)


# try:
import twint
import datetime
import pandas as pd
# except RuntimeError:
#     import sys; sys.exit() from threading import Timer, Thread
from tkinter.messagebox import showerror

class File:
    def __init__(self, list_file=[],name_file="", custom = []):
        self.list_file = list_file
        self.name_file = name_file
        self.custom = custom

    def sum_file(self):
        # with open(self.name_file, 'a') as out:
        #     for name in self.list_file:
        #         with open(name, 'r+') as data:
        #             data.__next__()
        #             for line in data:
        #                 out.write(line)
        # def slice_file(self):
    #     df = pd.read_csv(".tweets.csv")
    #     new_f = df[self.keys]
    #     new_f.to_csv(self.name_file , index=False)

        # data_files = []
        # for name in self.list_file:
        #     df = pd.read_csv(name)
        #     data_files.append(df)
        # df_all = pd.concat(data_files)
        # df_all.to_csv(self.name_file, index=False)
       data_csv = pd.concat( [ pd.read_csv(f) for f in self.list_file] )
    #    print("\n \n custom", self.custom, len(self.custom))
       if len(self.custom) != 22:
           data_csv = data_csv[self.custom]
    #    print("hehe\h]h]h]]n]\n\n\n\n\n\n\n\n\n\n",data_csv["language"].head())
       data_csv.to_csv(self.name_file , index=False )



class Config_twint:
    def __init__(self, keys=[], since="2018-12-29",until="2019-01-01", outfile="tweets33"):
        print("\n\n\n\n\\nyassine  ttkeys ", keys)
        print("ttsince ", since)
        print("ttuntil ", until)
        print("ttoutfile", outfile)
        print("\n\n\n\n\n\n\n")
  
        # self.name_file = outfile
        # self.keys = custom
        self.c = twint.Config()
        self.c.Search = keys
        self.c.Since = since
        self.c.Until = until

        # self.c.Search = ["RAM_Maroc"]#keys
        # self.c.Since = "2019-11-01" ##since
        # self.c.Until = "2019-11-09" #until
        # self.c.Lang = "en"
        self.c.Limit = 100
        self.c.Store_csv = True
        self.c.Output = outfile
        # "tweets.csv" 
        self.c.Hide_output = True
        
    # def slice_file(self):
    #     df = pd.read_csv(".tweets.csv")
    #     new_f = df[self.keys]
    #     new_f.to_csv(self.name_file , index=False)


    def run(self):
        # pass
        twint.run.Search(self.c)
#         # self.slice_file()



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


from collections import Counter
from tkinter.messagebox import showerror
from tkinter import filedialog
# import matplotlib.pyplot as plt
# import sweetviz as sv
# from tools import Clean
# import texthero as hero
# from PIL import Image
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# from collections import Counter
# from textblob import TextBlob

# drop_list = ['id', 'conversation_id', 'created_at', 'name', 'timezone', 'user_id', 'cashtags', 'place', 'quote_url', 'near', 'geo',
#              'source', 'user_rt_id', 'user_rt', 'retweet_id', 'retweet_date', 'translate', 'trans_src', 'trans_dest', 'video', 'retweet']


# class Visual(Clean):
#     def __init__(self, name_file=""):
#         super().__init__(name_file)
#         print("hello")
#         # print(self.df.head())

#     def cluster(self):
#         self.df['pca'] = (
#             self.df['clean_tweet']
#             .pipe(hero.tfidf, max_features=300)
#             .pipe(hero.pca)
#         )
#         # for s in self.df['pca']:
#         #     print(s)
#         # print("---------")
#         self.df['kmeans'] = (
#             self.df['clean_tweet']
#             .pipe(hero.tfidf, max_features=300)
#             .pipe(hero.kmeans, n_clusters=5)
#         )
#         print( self.df['pca'])
#         # for i in range(0 ,5):#self.df['pca'][self.df['kmeans'] == i,0]
#         #     plt.scatter( filter(,), self.df['pca'][self.df['kmeans'] == i,1])     #.apply(lambda x : if ), self.df['pca'].apply(lambda x : if ))
#         # plt.show()
#         # for s in self.df['kmeans']:
#         #     print(s)
#         # print("---------")
#         # for s in self.df['clean_tweet']:
#         #     print(s)
#         # print("---------")
#         # self.df.head()
#         # hero.scatterplot(self.df, 'pca', color='kmeans',
#         #                  hover_data=['clean_tweet'])

#     def show_word(self):
#         wordcloud = WordCloud(width=900, height=500, max_words=1628).generate(
#             ''.join(self.df['clean_tweet']))
#         plt.figure()
#         plt.imshow(wordcloud, interpolation="bilinear")
#         plt.axis("off")
#         plt.show()
#         # plt.savefig('books_read.png')

#     def language(self):
#         dic = Counter(self.df['language'])
#         plt.pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')
#         plt.show()
#         # plt.savefig('books_read.png')
#         # negative vs. positive neutral

#     def analyse(self, text):
#         try:
#             analys = TextBlob(text)
#         except:
#             print('error textblob')

#         if analys.polarity > 0.0:
#             return 'positive'
#         elif analys.polarity == 0.0:
#             return 'neutral'
#         else:
#             return 'negative'

#     def sentiment(self):
#         self.df['sentiment'] = self.df['clean_tweet'].apply(self.analyse)
#         dic = Counter(self.df['sentiment'])
#         plt.pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')
#         # plt.show()

#     def show(self):
#         fig, x = plt.subplots(2, 2)
#         dic = Counter(self.df['language'])
#         # explode = (0, 0.1, 0, 0)

#         x[0, 0].pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')

#         self.df['sentiment'] = self.df['clean_tweet'].apply(self.analyse)
#         dic = Counter(self.df['sentiment'])
#         x[0, 1].pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')

#         wordcloud = WordCloud(width=90, height=50, max_words=1628).generate(
#             ''.join(self.df['clean_tweet']))
#         x[1, 0].imshow(wordcloud, interpolation="bilinear")
#         x[1, 0].axis("off")

#         plt.show()


# data = Visual('arr.csv')
# data.cluster()
# # data.language()

# # data.show_word()
# # data.sentiment()
# # data.show()




# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import filedialog
# import os

# root = Tk()
# root.geometry("850x700+300+150")
# root.resizable(width=True, height=True)

# def openfn():
#     filename = filedialog.askopenfilename(title='open')
#     return filename
# def open_img():
#     x = './téléchargement.png'          #openfn()
#     img = Image.open(x)
#     img = img.resize((650, 650), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(img)
#     panel = Label(root, image=img)
#     panel.image = img
#     panel.pack()

# btn = Button(root, text='open image', command=open_img).pack()

# root.mainloop()


from tkinter import *
from  tools import Input
import tkinter.font as TkFont
from tkinter.messagebox import showerror
import  os
from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from wordcloud import WordCloud
from  textblob import TextBlob
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class  load_visual:
    def __init__(self, parent , dirname, flg_clean):
        self.parent = parent
        self.dir = dirname
        self.font_butt = TkFont.Font(
            family='Helvetica', size=10, weight=TkFont.BOLD)
        self.flg_clean = flg_clean
        self.df = pd.read_csv(dirname)    

    def show(self):
        pass

    def controller(self):
        self.frame = LabelFrame(
            self.parent, text=" controller :" ,fg = "red",  bg="#091833",
		  font =("Courier",11, "italic"))
        self.frame.grid(row=0, columnspan=9, sticky='W', padx=15, pady=5, ipadx=5, ipady=6)
        self.root = LabelFrame(
            self.parent, text=" visualisation :" ,fg = "red", bg="#091833",
		  font =("Courier",11, "italic"))
        self.root.grid(row=1, columnspan=12, sticky='W', padx=8, pady=6, ipadx=0, ipady=0)

        self.butt_clear = Button(self.frame, text="Language".center(21),  command=self.language ,
           font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=2, padx=30, pady=0, ipadx=5, ipady=0)
        self.butt_clear = Button(self.frame, text="Sentiment".center(21),  command=self.sentiment,
            font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=3, padx=30, pady=0, ipadx=5, ipady=0)
        self.butt_clear = Button(self.frame, text="Cluster".center(21),  
            font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=4, padx=30, pady=0, ipadx=5, ipady=0)
        self.butt_clear = Button(self.frame, text="Freq words".center(21),  command= self.show_word,
            font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=5, padx=30, pady=0, ipadx=5, ipady=0)

    
#     def show_word(self):
#         wordcloud = WordCloud(width=900, height=500, max_words=1628).generate(
#             ''.join(self.df['clean_tweet']))
#         plt.figure()
#         plt.imshow(wordcloud, interpolation="bilinear")
#         plt.axis("off")
#         plt.show()
#         # plt.savefig('books_read.png')
# f = plt.Figure(figsize=(4,4))
#         #a = f.add_subplot(111)
#         pie = plt.pie(values, labels=header, colors=colors, startangle=90, 
#                       autopct='%.1f%%')
#         self.canvas = FigureCanvasTkAgg(f, top_frame)
    def language(self):###https://datatofish.com/matplotlib-charts-tkinter-gui/
        dic = Counter(self.df['language'])
        figure1 = plt.Figure(figsize=(8,4))
        ax1 = figure1.add_subplot(111)
        ax1.pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')
        bar1 = FigureCanvasTkAgg(figure1, self.root)
        bar1.get_tk_widget().grid(row=0, column=0)
        ax1.legend(dic.keys()) 
        ax1.set_xlabel('languages')
        ax1.set_title('Static languages')

    def show_word(self):
        wordcloud = WordCloud(width=1100, height=600, max_words=2222).generate(
            ''.join(self.df['clean_tweet']))
        figure1 = plt.Figure(figsize=(8,4))
        ax1 = figure1.add_subplot(111)
        ax1.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        bar1 = FigureCanvasTkAgg(figure1, self.root)
        bar1.get_tk_widget().grid(row=0, column=0)
        # ax1.legend(dic.keys()) 
        # ax1.set_xlabel('languages')
        # ax1.set_title('Static languages')
        # plt.savefig('books_read.png')


#         # plt.savefig('books_read.png')
#         # negative vs. positive neutral

    def analyse(self, text):
        try:
            analys = TextBlob(text)
        except:
            print('error textblob')

        if analys.polarity > 0.0:
            return 'positive'
        elif analys.polarity == 0.0:
            return 'neutral'
        else:
            return 'negative'

    def sentiment(self):
        self.df['sentiment'] = self.df['tweet'].apply(self.analyse)
        dic = Counter(self.df['sentiment'])
        # plt.pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')
        # plt.show()
        figure1 = plt.Figure(figsize=(8,4))
        ax1 = figure1.add_subplot(111)
        ax1.pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')
        bar1 = FigureCanvasTkAgg(figure1, self.root)
        bar1.get_tk_widget().grid(row=0, column=0)
        ax1.legend(dic.keys()) 
        ax1.set_xlabel('languages')
        ax1.set_title('Static languages')

       

    # def analyse(self, text):
    #     try:
    #         analys = TextBlob(text)
    #     except:
    #         print('error textblob')
        
    # def language(self):
    #     data1 = {'Country': ['US','CA','GER','UK','FR'],
    #      'GDP_Per_Capita': [45000,42000,52000,49000,47000]
    #     }
    #     df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])
    #     figure1 = plt.Figure(figsize=(8,4), dpi=100)
    #     ax1 = figure1.add_subplot(111)
    #     bar1 = FigureCanvasTkAgg(figure1, self.root)
    #     bar1.get_tk_widget().grid(row=0, column=0)
    #     df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
    #     df1.plot(kind='bar', legend=True, ax=ax1)
    #     ax1.set_title('Country Vs. GDP Per Capita')
    
    # def sentiment(self):
    #     pass
    # def words(self):
    #     pass
    # def cluster(self):
    #     pass

class  Visual:
    def __init__(self, apps, parent, list_file=[]):
        print("visual")
        self.parent = parent
        self.dir = None
        self.name_file = StringVar()
        self.var_clean = IntVar()
        self.name_file.set("filename :")
        self.font_butt = TkFont.Font(
            family='Helvetica', size=10, weight=TkFont.BOLD)


    def exec(self):
        if not self.dir or not os.path.exists(self.dir):
            return
        for widget in self.parent.winfo_children():
            widget.destroy()
        ################################################################
        load_visual(self.parent  , self.dir , 1).controller()

    def show(self):
        Label(self.parent, text="Enter name file :", bg="#f2a343" , font =("Courier", 15, "italic")).grid(row=2, column=0, columnspan=6 ,sticky='w', padx=15, pady=12)
        self.save_download = Button(self.parent, text="choise file ".center(25), command=self.path,
                                    font=self.font_butt, bg="red", width=12)
        self.save_download.grid(row=2, column=1, padx=15, pady=12, ipadx=6, ipady=5)
        self.save_download = Button(self.parent, text="Run".center(25), command=self.exec,
                                    font=self.font_butt, bg="red", width=12)
        self.save_download.grid(row=2, column=2, padx=15, pady=12, ipadx=6, ipady=5)
        Checkbutton(self.parent, text=str(" file is clean "), variable=self.var_clean, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=3, column=0, padx=18, pady=6, ipadx=5, ipady=5)
        Label(self.parent,  textvariable= self.name_file, bg="#f2a343" , font =("Courier", 15, "italic")).grid(row=5, column=0, columnspan=9 ,sticky='w',padx=15, pady=12)

    def path(self):
        self.dir = filedialog.askopenfilename(
            initialdir=os.getcwd(), title="Please select a file:",)
        print("namme", self.dir)
        if self.dir and os.path.isfile(self.dir):
            self.name_file.set("filename : " + Path(self.dir).name)


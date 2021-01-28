from tkinter import filedialog
# # import texthero as hero
# # import numpy.random.common
# # import numpy.random.bounded_integers
# # import numpy.random.entropy

from tkinter import *
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import Counter###
import numpy as np###
from pathlib import Path
import pandas as pd
import tkinter.font as TkFont
from tkinter.messagebox import showerror
import os
from clean import Preprocessing
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from pprint import pprint
from sklearn.decomposition import PCA

# pca = PCA(n_components=2)
# principalComponents = pca.fit_transform(x)
# principalDf = pd.DataFrame(data = principalComponents
#              , columns = ['principal component 1', 'principal component 2'])

class load_visual:
    def __init__(self, parent, dirname, flg_clean , dict_clean):
        self.parent = parent
        self.dir = dirname
        self.font_butt = TkFont.Font(
            family='Helvetica', size=10, weight=TkFont.BOLD)
        self.flg_clean = flg_clean
        # print("Writing", flg_clean , "---",dict_clean)
        if flg_clean == 1:
            pass
            # Preprocessing(dirname, dict_clean)

        self.df = pd.read_csv(dirname)
        self.df = self.df[pd.notnull(self.df['clean_tweet'])]############################################

    def show(self):
        pass

    def controller(self):
        self.frame = LabelFrame(
            self.parent, text=" controller :", fg="red",  bg="#091833",
            font=("Courier", 11, "italic"))
        self.frame.grid(row=0, columnspan=9, sticky='W',
                        padx=15, pady=5, ipadx=5, ipady=6)
        self.root = LabelFrame(
            self.parent, text=" visualisation :", fg="red", bg="#091833",
            font=("Courier", 11, "italic"))
        self.root.grid(row=1, columnspan=12, sticky='W',
                       padx=8, pady=6, ipadx=0, ipady=0)

        self.butt_clear = Button(self.frame, text="Language".center(21),  command=self.language,
                                 font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=2, padx=30,
                             pady=0, ipadx=5, ipady=0)
        self.butt_clear = Button(self.frame, text="Sentiment".center(21),  command=self.sentiment,
                                 font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=3, padx=30,
                             pady=0, ipadx=5, ipady=0)
        self.butt_clear = Button(self.frame, text="Cluster".center(21),  command=self.cluster,
                                 font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=4, padx=30,
                             pady=0, ipadx=5, ipady=0)
        self.butt_clear = Button(self.frame, text="Freq words".center(21),  command=self.show_word,
                                 font=self.font_butt, bg="red", width=13)
        self.butt_clear.grid(row=2, column=5, padx=30,
                             pady=0, ipadx=5, ipady=0)

    def language(self):  # https://datatofish.com/matplotlib-charts-tkinter-gui/
        if not 'language' in self.df.columns:
            showerror("Error Visual language", "not find column language:")
            return
        dic = Counter(self.df['language'])
        figure1 = plt.Figure(figsize=(8, 4))
        ax1 = figure1.add_subplot(111)
        ax1.pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')
        bar1 = FigureCanvasTkAgg(figure1, self.root)
        bar1.get_tk_widget().grid(row=0, column=0)
        ax1.legend(dic.keys())
        ax1.set_xlabel('languages')
        ax1.set_title('Static languages')

    def show_word(self):
        if not 'clean_tweet' in self.df.columns:
            showerror("Error Visual word",
                      "not find column clean_tweet, please clean file ")
            return
        # wordcloud = WordCloud(width=1100, height=600, max_words=1000).generate(
        #     ''.join(self.df['clean_tweet']))
            # plot.barh(x='words',
            #           y='count',
            #           ax=ax,
            #           color="purple")
        data = ''.join(self.df['clean_tweet'])
        dic = dict(Counter(data.split()).most_common(111))
        pprint(dic)
        figure1 = plt.Figure(figsize=(8, 4))
        ax1 = figure1.add_subplot(111)
        ax1.pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')
        bar1 = FigureCanvasTkAgg(figure1, self.root)
        bar1.get_tk_widget().grid(row=0, column=0)
        ax1.legend(dic.keys())
        # ax1.set_xlabel('languages')
        # ax1.set_title('Static languages')
        ax1.set_title('Frequense WordS')
        # ax1.imshow(wordcloud, interpolation="bilinear")
        # plt.axis("off")
        # plot.barh(x='words',
        #               y='count',
        #               ax=ax,
        #               color="purple")
        # bar1 = FigureCanvasTkAgg(figure1, self.root)
        # bar1.get_tk_widget().grid(row=0, column=0)

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
        if not 'clean_tweet' in self.df.columns:
            showerror("Error Visual sentiment :",
                      "not find column clean_tweet, please clean file ")
            return
        self.df['sentiment'] = self.df['clean_tweet'].apply(self.analyse)
        dic = Counter(self.df['sentiment'])

        figure1 = plt.Figure(figsize=(8, 4))
        ax1 = figure1.add_subplot(111)
        ax1.pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')
        bar1 = FigureCanvasTkAgg(figure1, self.root)
        bar1.get_tk_widget().grid(row=0, column=0)
        ax1.legend(dic.keys())
        ax1.set_xlabel('')
        ax1.set_title('Analyse Sentiment tweets')

    def cluster(self):
        if not 'clean_tweet' in self.df.columns:
            showerror("Error Visual cluster :",
                      "not find column clean_tweet, please clean file ")
            return
        vectorizer = TfidfVectorizer(stop_words = 'english')
        data = vectorizer.fit_transform(self.df['clean_tweet'])
        pca = PCA(n_components=2)
        p = pca.fit_transform(data)
        kmeans = KMeans(n_clusters=3).fit(df)
        centroids = kmeans.cluster_centers_

        # self.df['tfidf'] = self.df['clean_tweet'].pipe(hero.tfidf)
        # self.df['pca'] = (
        #     self.df['tfidf'].pipe(hero.pca)
        # )
        # self.df['kmeans'] = (
        #     self.df['tfidf']
        #     .pipe(hero.kmeans, n_clusters=3)
        # )
        # figure1 = plt.Figure(figsize=(8, 4))
        # ax1 = figure1.add_subplot(111)
        # for i in range(0, 5):
        #     data = self.df[self.df['kmeans'] == i]['pca'].to_numpy()
        #     x = []
        #     y = []
        #     for i in data:
        #         x.append(i[0])
        #         # print(i[0])
        #         y.append(i[1])
        #     # pprint(x)
        #     ax1.scatter(x, y)

        # bar1 = FigureCanvasTkAgg(figure1, self.root)
        # bar1.get_tk_widget().grid(row=0, column=0)
        # ax1.legend([1, 2, 3, 4, 5])
        # ax1.set_xlabel('')
        # ax1.set_title('Analyse Category tweets')


class Visual:
    def __init__(self, apps, parent, list_file=[]):
        # print("visual")
        self.parent = parent
        self.dir = None
        self.dict_clean = {}
        self.name_file = StringVar()
        self.var_clean = IntVar()
        self.var_clean.set(0)
        self.name_file.set("filename :")
        self.font_butt = TkFont.Font(
            family='Helvetica', size=10, weight=TkFont.BOLD)

    def set_dict(self, data):
        # print("----->", data)
        self.dict_clean = data

    def exec(self):
        if not self.dir or not os.path.exists(self.dir):
            # '%s'" % Path(self.dir).name)
            showerror("Error ", "not find file")
            return

        for widget in self.parent.winfo_children():
            widget.destroy()
        ################################################################
        load_visual(self.parent, self.dir, self.var_clean.get() , self.dict_clean).controller()

    def show(self):
        Label(self.parent, text="Enter name file :", bg="#f2a343", font=(
            "Courier", 15, "italic")).grid(row=2, column=0, columnspan=6, sticky='w', padx=15, pady=12)
        self.save_download = Button(self.parent, text="choise file ".center(25), command=self.path,
                                    font=self.font_butt, bg="red", width=12)
        self.save_download.grid(row=2, column=1, padx=15,
                                pady=12, ipadx=6, ipady=5)
        self.save_download = Button(self.parent, text="Run".center(25), command=self.exec,
                                    font=self.font_butt, bg="red", width=12)
        self.save_download.grid(row=2, column=2, padx=15,
                                pady=12, ipadx=6, ipady=5)
        Checkbutton(self.parent, text=str("  want to clean file "), variable=self.var_clean, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=3, column=0, padx=18, pady=6, ipadx=5, ipady=5)
        Label(self.parent,  textvariable=self.name_file, bg="#f2a343", font=(
            "Courier", 15, "italic")).grid(row=5, column=0, columnspan=9, sticky='w', padx=15, pady=12)

    def path(self):
        self.dir = filedialog.askopenfilename(
            initialdir=os.getcwd(), title="Please select a file:",)
        # print("namme", self.dir)
        if self.dir and os.path.isfile(self.dir):
            self.name_file.set("filename : " + Path(self.dir).name)

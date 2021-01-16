
import pandas as pd
import demoji
import emoji
import string
from tkinter.messagebox import showerror
from nltk.stem import PorterStemmer
from deep_translator import GoogleTranslator
from tkinter import *
import tkinter.font as TkFont
from tkinter import filedialog
import os
import nltk
import re
from  threading import Timer, Thread

class Preprocessing:
    def __init__(self, name_file=None , dic={}):
        self.dic = dic
        self.stopwords = set(nltk.corpus.stopwords.words('english'))
        stop_w = ["Royal Air Maroc", "RAM_Maroc",    "@RAM_Maroc",
                  "royalairmaroc", "الخطوط المغربيه", "#الخطوط_الملكية_المغربية ", "الخطوط الملكية المغربية", "Royal Air Maroc", "لارام",  " لارام", "الخطوط_الملكية_المغربية", "RAM"]
        self.stopwords = self.stopwords.union(set(stop_w))
        print("ddd", self.stopwords)
        # demoji.download_codes()
        self.porter = PorterStemmer()
        self.df = pd.DataFrame([])
        try:
            self.df = pd.read_csv(name_file)
        except IOError:
            raise Exception("erro file %s" % (name_file))
        self.language = None
        self.trans()
       
        for s in self.df['tweet']:
            print(s)
        print("---------")
        self.df['clean_tweet'] = self.df['tweet'].apply(self.test)
        for s in self.df['clean_tweet']:
            print(s)
        print("---------")

    def trans(self):
        for key, value in self.dic['trans'].items():
            if value == 1:
                self.language = key
        if self.language:
            self.translate = GoogleTranslator(source='auto', target=self.language)

    def start(self):
        self.df['clean_tweet'] = self.df['tweet'].apply(
            self.test)

    def test(self , text):
        text = str(text)
        if not text:
            return ""
        text = self.change_emoji(text)
        if self.dic["word"]["name"] == 1:
            text = ' '.join(filter(lambda x: x and x[0] != '@', text.split()))
        if self.dic["word"]["whitespace"] == 1:
            text = text.strip()
        if self.dic["word"]["punctuation"] == 1:
            text = text.translate(str.maketrans("","",string.punctuation))
        if self.dic["word"]["urls"] == 1:
            text = re.sub(r'https\S+','',text)
        if not text:
            return ""
     
        if self.language :
            print("ll", self.language)
            text = self.filter_text(text)

        if not text:
            return ""
        text = text.split()
        if self.dic["word"]["digit"] == 1:
            text = filter(lambda x : x and x.isalpha() , text)
        if self.dic["word"]["lowercase"] == 1:
            text = map(lambda x : x.lower(), text)
            text = filter(lambda x : not x in self.stopwords , text)
        if self.dic["word"]["stem"] == 1:
            text = map(lambda x : self.porter.stem(x) , text)
            
        
        return ' '.join(text)

    def change_emoji(self, text):
        if self.dic["emoji"]["stay"] == 1:
            return text
        elif self.dic["emoji"]["replace"] == 1:
            text_new = demoji.replace_with_desc(text).replace(":", " ")
        else:
            text_new = re.sub(emoji.get_emoji_regexp(), "", text)
        return text_new

    def filter_text(self, text):
        if not text:
            return text
        if len(text) < 5000:
            return (self.translate.translate(text))
        return self.translate.translate(text[:4999])

    def get_df(self):
        return self.df

# def main():
#     dict = {'trans': {'en': 1, 'fr': 0, 'ar': 0},\
#          'word': {'name': 1, 'lowercase': 1,\
#          'diacritics': 1, 'fillna': 1, 'stem': 1, 'digit': 1,\
#          'punctuation': 1, 'urls': 1, 'whitespace': 1}, \
#              'emoji': {'remove': 1, 'stay': 0, 'replace': 0}} 
#     cla = Preprocessing('fb.csv' , dict)
# if __name__=='__main__':
#     main()
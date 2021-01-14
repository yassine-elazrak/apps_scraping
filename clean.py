# import texthero as hero
import pandas as pd
import demoji
from tkinter.messagebox import showerror
# from texthero import stopwords
# from texthero import preprocessing
from deep_translator import GoogleTranslator
from tkinter import *
import tkinter.font as TkFont
from tkinter import filedialog
import os
from  threading import Timer, Thread

# class Preprocessing:
#     def __init__(self, name_file=None):
#         self.df = pd.DataFrame([])
#         try:
#             self.df = pd.read_csv(name_file)
#         except IOError:
#             raise Exception("erro file %s" % (name_file))

#         self.translate = GoogleTranslator(source='auto', target='en')
#         self.filter_word()
#         self.clean()
#         self.ft_translate()
#         self.clean_word()
#         # for s in self.df['clean_tweet']:
#         #     print(s)
#         self.remove_stop_words()
#         # for s in self.df['tweet']:
#         #     print(s)
#         # print("---------")

#     def filter_word(self):
#         self.df['clean_tweet'] = self.df['tweet'].apply(self.change_words)

#     def remove_stop_words(self):
#         stop_w = ["Royal Air Maroc", "RAM_Maroc",    "@RAM_Maroc",
#                   "royalairmaroc", "الخطوط المغربيه", "#الخطوط_الملكية_المغربية ", "الخطوط الملكية المغربية", "Royal Air Maroc", "لارام",  " لارام", "الخطوط_الملكية_المغربية", "RAM"]
#         default_stopwords = stopwords.DEFAULT.union(stopwords.SPACY_EN)
#         custom_stopwords = default_stopwords.union(set(stop_w))
#         self.df['clean_tweet'] = hero.remove_stopwords(
#             self.df['clean_tweet'], custom_stopwords)

#     def clean(self):
#         custom_pipeline = [
#             preprocessing.remove_digits, preprocessing.fillna, preprocessing.remove_punctuation, preprocessing.remove_urls, preprocessing.remove_whitespace
#         ]
#         self.df['clean_tweet'] = hero.clean(
#             self.df['clean_tweet'], pipeline=custom_pipeline)

#     def change_words(self, text):
#         text_new = demoji.replace_with_desc(text).replace(":", " ")
#         text_new = " ".join(
#             filter(lambda x: x[0] != '@', text_new.split()))
#         return text_new

#     def filter_text(self, text):
#         if not text:
#             return text
#         if len(text) < 5000:
#             return (self.translate.translate(text))
#         return self.translate.translate(text[:4999])

#     def ft_translate(self):
#         self.df['clean_tweet'] = self.df['clean_tweet'].apply(
#             self.filter_text)

#     def clean_word(self):
#         custom_pipeline = [
#             preprocessing.remove_diacritics, preprocessing.lowercase,  preprocessing.stem
#         ]
#         self.df['clean_tweet'] = hero.clean(
#             self.df['clean_tweet'], pipeline=custom_pipeline)
#         self.df['clean_tweet'] = self.df['clean_tweet'].apply(
#             self.ft_remove_word_digit)

#     def ft_remove_word_digit(self, text):
#         if text:
#             return ' '.join(filter(lambda x: x.isalpha(), text.split()))
#         return text

#     def get_df(self):
#         return self.df


# def main():
#     df = Clean('arr.csv').get_df()
#     print(df['tweet'])
#     print(df['clean_tweet'])


# if __name__ == '__main__':
#     main()


class Trans:
    def __init__(self, parent):
        self.en = IntVar()
        self.fr = IntVar()
        self.ar = IntVar()
        self.parent =parent
        self.dict = {}
        for name in ["en" , "fr" , "ar"]:
            self.dict[name] = 0

    def main(self):
        self.fram = LabelFrame(
            self.parent, text=" Stting Language Translate", fg="red",
            font=("Courier", 21, "italic"))
        self.fram.grid(row=3, columnspan=14, sticky='WENS',
                       padx=5, pady=5, ipadx=5, ipady=5)
        Label(self.fram, text="Language", bg="#f2a343", font=("Courier", 15, "italic")).grid(
            row=1, column=0, columnspan=2, sticky='w', padx=5, pady=6)
        Checkbutton(self.fram, text=str("  English   "), variable=self.en, command=self.ft_replace, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=1, column=2, padx=8, pady=6, ipadx=5, ipady=5)
        Checkbutton(self.fram, text=str("  Fransh    "), variable=self.fr, command=self.ft_stay, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=1, column=4, padx=8, pady=6, ipadx=5, ipady=5)
        Checkbutton(self.fram, text=str("  Arabic    "), variable=self.ar, command=self.ft_remove, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=1, column=6, padx=8, pady=6, ipadx=5, ipady=5)
        # self.en.set(1)

    def ft_replace(self):
        self.fr.set(0)
        self.ar.set(0)

        
        

    def ft_stay(self):
        self.en.set(0)
        self.ar.set(0)

    def ft_remove(self):
        self.fr.set(0)
        self.en.set(0)

    def save(self):
        self.dict["en"] = self.en.get()
        self.dict["fr"] = self.fr.get()
        self.dict["ar"] = self.ar.get()
    def get_all(self):
        return self.dict


    def clear_all(self):
        self.en.set(0)
        self.ar.set(0)
        self.fr.set(0)

    def set_all(self):
        self.en.set(1)
        


class Emoji:
    def __init__(self, parent):
        self.parent = parent
        self.replace = IntVar()
        self.remove = IntVar()
        self.stay = IntVar()
        self.dict = {}
        for name in ["remove" , "stay" , "replace"]:
            self.dict[name] = 0

    def main(self):
        self.fram = LabelFrame(
            self.parent, text=" Stting Emoji ", fg="red",
            font=("Courier", 21, "italic"))
        self.fram.grid(row=2,  columnspan=14, sticky='WENS',
                       padx=5, pady=5, ipadx=5, ipady=5)
        Label(self.fram, text="Stting Emoji ", bg="#f2a343", font=("Courier", 15, "italic")).grid(
            row=1, column=0, columnspan=2, sticky='w', padx=5, pady=6)
        Checkbutton(self.fram, text=str("replace emoji"), variable=self.replace, command=self.ft_replace,
                    bg="bisque", font=("Courier", 14, "italic")).grid(row=1, column=2, padx=8, pady=6)
        Checkbutton(self.fram, text=str(" stay  emoji "), variable=self.stay, command=self.ft_stay,
                    bg="bisque", font=("Courier", 14, "italic")).grid(row=1, column=4, padx=8, pady=6)
        Checkbutton(self.fram, text=str("remove  emoji"), variable=self.remove, command=self.ft_remove,
                    bg="bisque", font=("Courier", 14, "italic")).grid(row=1, column=6, padx=8, pady=6)
        self.replace.set(1)

    def ft_replace(self):
        self.stay.set(0)
        self.remove.set(0)

    def ft_stay(self):
        self.replace.set(0)
        self.remove.set(0)

    def ft_remove(self):
        self.replace.set(0)
        self.stay.set(0)
    def save(self):
        self.dict["remove"] = self.remove.get()
        self.dict["stay"] = self.stay.get()
        self.dict["replace"] = self.replace.get()
    def get_all(self):
        return self.dict

    def clear_all(self):
        self.replace.set(0)
        self.remove.set(0)
        self.stay.set(0)
    
    def set_all(self):
        self.replace.set(1)



class Word:
    def __init__(self, parent):
        self.parent = parent
        self.stem = IntVar()
        self.digit = IntVar()
        self.punctuation = IntVar()
        self.urls = IntVar()
        self.whitespace = IntVar()
        self.diacritics = IntVar()
        self.lowercase = IntVar()
        self.fillna = IntVar()
        self.name = IntVar()
        self.dict = {}
        for name in ["name" , "lowercase"  , "diacritics" , "fillna" , "stem" , "digit" , "punctuation" , "urls" , "whitespace"]:
            self.dict[name] = 0
        




    def main(self):
        self.fram = LabelFrame(
            self.parent, text=" Stting Clean :", fg="red",
            font=("Courier", 21, "italic"))
        self.fram.grid(row=0, columnspan=14, sticky='WENS',
                       padx=5, pady=1, ipadx=5, ipady=1)
        Checkbutton(self.fram, text=str("remove digit "), variable=self.digit, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=0, column=2, padx=8, pady=6)
        Checkbutton(self.fram, text=str("remove punctuation"), variable=self.punctuation,
                    bg="bisque", font=("Courier", 14, "italic")).grid(row=0, column=4, padx=8, pady=6)
        Checkbutton(self.fram, text=str("   remove  urls   "), variable=self.urls, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=0, column=6, padx=8, pady=6)

        Checkbutton(self.fram, text=str("remove  whitespace"), variable=self.whitespace,
                    bg="bisque", font=("Courier", 14, "italic")).grid(row=1, column=6, padx=4, pady=6)
        Checkbutton(self.fram, text=str(" lowercase   "), variable=self.lowercase, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=1, column=2, padx=8, pady=6)
        Checkbutton(self.fram, text=str("remove diacritics "), variable=self.diacritics,
                    bg="bisque", font=("Courier", 14, "italic")).grid(row=1, column=4, padx=11, pady=6)

        Checkbutton(self.fram, text=str("remove fillna"), variable=self.fillna, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=2, column=2, padx=14, pady=6)
        Checkbutton(self.fram, text=str("  stemming words  "), variable=self.stem, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=2, column=4, padx=14, pady=6)
        Checkbutton(self.fram, text=str("remove screen name"), variable=self.name, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=2, column=6, padx=14, pady=6)

    # def ft_replace(self):
    #     pass

    # def ft_stay(self):
    #     pass

    # def ft_remove(self):
    #     pass
# ["name" , "lowercase"  , "diacritics" , "fillna" , "stem" , "digit" , "punctuation" , "urls" , "whitespace"]:

    def save(self):
        self.dict["punctuation"] = self.punctuation.get()
        self.dict["name"] = self.name.get()
        self.dict["stem"] = self.stem.get()
        self.dict["lowercase"] = self.lowercase.get()
        self.dict["digit"] = self.digit.get()
        self.dict["fillna"] = self.fillna.get()
        self.dict["urls"] = self.urls.get()
        self.dict["whitespace"] = self.whitespace.get()
        self.dict["diacritics"] = self.diacritics.get()

    def get_all(self):
        return self.dict

    def clear_all(self):
        self.punctuation.set(0)
        self.name.set(0)
        self.stem.set(0)
        self.lowercase.set(0)
        self.digit.set(0)
        self.fillna.set(0)
        self.urls.set(0)
        self.whitespace.set(0)
        self.diacritics.set(0)
        self.dict = {}

    def set_all(self):
        self.punctuation.set(1)
        self.name.set(1)
        self.stem.set(1)
        self.lowercase.set(1)
        self.digit.set(1)
        self.fillna.set(1)
        self.urls.set(1)
        self.whitespace.set(1)
        self.diacritics.set(1)


class Clean:
    def __init__(self, apps, parent, list_file=[]):
        print("Clean")
        self.master = parent
        self.font_butt = TkFont.Font(
            family='Helvetica', size=10, weight=TkFont.BOLD)
        self.word = Word(parent)
        self.emoji = Emoji(parent)
        self.trans = Trans(parent)
        self.dict = {}

    def exec(self):
            th  = Thread(target=self.run).start()
    def run(self):
            dic = self.get_all()
            print("Running" , dic)
    def path(self):
        self.name_file = filedialog.askopenfilename(
            initialdir=os.getcwd(), title="Please select a file:",)
        print("namme", self.name_file)
        self.exec()

    def get_all(self):
        self.dict["trans"] = self.trans.get_all()
        self.dict["word"] = self.word.get_all()
        self.dict["emoji"] = self.emoji.get_all()
        return self.dict

    def clear_all(self):
        self.trans.clear_all()
        self.word.clear_all()
        self.emoji.clear_all()

    def save(self):
        self.trans.save()
        self.word.save()
        self.emoji.save()

    def set_all(self):
        self.trans.set_all()
        self.word.set_all()
        self.emoji.set_all()


    def show(self):
        self.fram = Frame(
            self.master , bg="#091833")
        self.fram.grid(row=4, columnspan=14, sticky='WENS',
                       padx=5, pady=1, ipadx=5, ipady=1)
        self.word.main()
        self.emoji.main()
        self.trans.main()

        self.save_download = Button(
            self.fram, text=" Save Download".center(25), command = self.save, font=self.font_butt, bg="red", width=18)
        self.save_download.grid(row=1, column=1, padx=5,
                                pady=5, ipadx=6, ipady=5)
        self.save_download = Button(self.fram, text=" Execute For File Exist".center(25),
                                    command=self.path, font=self.font_butt, bg="red", width=18)
        self.save_download.grid(row=1, column=2, padx=5,
                                pady=6, ipadx=6, ipady=5)
        self.save_download = Button(self.fram, text="set all".center(25),
                                    command=self.set_all, font=self.font_butt, bg="red", width=18)
        self.save_download.grid(row=1, column=3, padx=5,
                                pady=6, ipadx=6, ipady=5)
        self.save_download = Button(self.fram, text="clear all".center(25),
                                    command=self.clear_all, font=self.font_butt, bg="red", width=18)
        self.save_download.grid(row=1, column=4, padx=5,
                                pady=6, ipadx=6, ipady=5)


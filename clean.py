# import texthero as hero
import pandas as pd
import demoji
# from texthero import stopwords
# from texthero import preprocessing
from deep_translator import GoogleTranslator
from tkinter import *
import tkinter.font as TkFont
from tkinter import filedialog
import os

# class Clean:
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
        self.en.set(1)

    def ft_replace(self):
        pass

    def ft_stay(self):
        pass

    def ft_remove(self):
        pass

    def get_all(self):
        pass

    def clear_all(self):
        pass


class Emoji:
    def __init__(self, parent):
        self.parent = parent
        self.replace = IntVar()
        self.remove = IntVar()
        self.stay = IntVar()


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
        pass

    def ft_stay(self):
        pass

    def ft_remove(self):
        pass

    def get_all(self):
        pass

    def clear_all(self):
        pass


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

    def ft_replace(self):
        pass

    def ft_stay(self):
        pass

    def ft_remove(self):
        pass

    def get_all(self):
        pass

    def clear_all(self):
        pass


# class G_Clean:
#     def __init__(self, parent):
#         self.master = parent

#     def s_emoji(self):
#         self.s_emoj


# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.pickedfiletypes = (('png files', '*.png'), ('jpeg files', '*.jpeg'))
#         self.create_widgets()

#     def create_widgets(self):
#         ...

#         self.fileselect = tk.filedialog.askopenfilename(self,
#                                     initialdir= os.getcwd(),
#                                     title= "Please select a file:",
#                                     filetypes= self.pickedfiletypes)
#         ...

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()

class Clean:
    def __init__(self, apps, parent, list_file=[]):
        print("Clean")
        self.master = parent
        self.font_butt = TkFont.Font(
            family='Helvetica', size=10, weight=TkFont.BOLD)
        self.word = Word(parent)
        self.emoji = Emoji(parent)
        self.trans = Trans(parent)

    def path(self):
        name = filedialog.askopenfilename(
            initialdir=os.getcwd(), title="Please select a file:",)
        print("namme", name)

    def get_all(self):
        pass

    def clear_all(self):
        pass

    def show(self):
        self.fram = Frame(
            self.master , bg="#091833")
        self.fram.grid(row=4, columnspan=14, sticky='WENS',
                       padx=5, pady=1, ipadx=5, ipady=1)
        self.word.main()
        self.emoji.main()
        self.trans.main()

        self.save_download = Button(
            self.fram, text=" Save Download", font=self.font_butt, bg="red", width=18)
        self.save_download.grid(row=1, column=1, padx=5,
                                pady=5, ipadx=6, ipady=15)
        self.save_download = Button(self.fram, text=" Execute For File Exist",
                                    command=self.path, font=self.font_butt, bg="red", width=18)
        self.save_download.grid(row=1, column=2, padx=5,
                                pady=6, ipadx=6, ipady=15)


# app = Tk()

# def main():
#     em = Word(app)
#     em.main()
#     eme = Emoji(app)
#     eme.main()
#     t = Trans(app)
#     t.main()
#     Save(app)


# if __name__ == '__main__':

#     app.geometry('950x640+0+0')
#     app.configure(background="#091833")
#     app.title('hello new word')
#     main()
#     app.mainloop()

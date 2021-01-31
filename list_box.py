
from tkinter import *
from tools import Input
from functools import reduce
from pprint import pprint
import tkinter.font as TkFont
from tkinter.messagebox import showerror
from  autocomplet import AutocompleteEntry


class Box:
    def __init__(self, apps=None):
        self.master = apps
        self.Words = []
        self.var_clean = IntVar()
        self.valuer_clean = 0
        self.font_butt = TkFont.Font(
            family='Helvetica', size=10, weight=TkFont.BOLD)

    def add(self):
        word = str(self.data.get()).strip()
        if word and not "      enter key search" in word:
            self.Words.append(str(self.data.get()).strip())
            self.list_box.insert(0,   word)
            self.data.delete(0, END)

    def remove(self):
        if self.Words:
            self.list_box.delete(0)
            self.Words.pop()

    def get_all(self):
        # print("keys=>>", self.Words)
        self.valuer_clean = self.var_clean.get()
        return self.Words

    def init(self):
        self.Words = []
        self.list_box.delete(0, END)

    def clear_all(self):
        self.Words.clear()
        self.list_box.delete(0, END)
        self.data.ft_delete(0, END)
        self.var_clean.set(0)

    def creat(self):
        self.field1 = Frame(self.fram, bg="#091833")
        self.field1.grid(row=0, columnspan=2, sticky='w', padx=2, pady=2)
        self.field1.configure(background="#091833")
        self.field2 = Frame(self.fram, bg="#091833")
        self.field2.grid(row=1, columnspan=2, sticky='w', padx=2, pady=2)
        self.field2.configure(background="#091833")

        self.label = Label(self.field1, text="Search :", fg="snow",
                           bg="#f2a343", font=("Courier", 28, "italic"))
        self.label.grid(row=0, column=0)
        self.label.configure(background="#091833")##############################
        autocompleteList = [ 'Dora Lyons (7714)', 'Hannah Golden (6010)', 'Walker Burns (9390)', 'Dieter Pearson (6347)', 'Allen Sullivan (9781)', 'Warren Sullivan (3094)', 'Genevieve Mayo (8427)', 'Igor Conner (4740)', 'Ulysses Shepherd (8116)', 'Imogene Bullock (6736)', 'Dominique Sanchez (949)', 'Sean Robinson (3784)', 'Diana Greer (2385)', 'Arsenio Conrad (2891)', 'Sophia Rowland (5713)', 'Garrett Lindsay (5760)', 'Lacy Henry (4350)', 'Tanek Conley (9054)', 'Octavia Michael (5040)', 'Kimberly Chan (1989)', 'Melodie Wooten (7753)', 'Winter Beard (3896)',
            'Callum Schultz (7762)', 'Prescott Silva (3736)', 'Adena Crane (6684)', 'Ocean Schroeder (2354)', 'Aspen Blevins (8588)', 'Allegra Gould (7323)', 'Penelope Aguirre (7639)', 
            'Deanna Norman (1963)', 'Herman Mcintosh (1776)', 'August Hansen (547)', 'Oscar Sanford (2333)', 'Guy Vincent (1656)', 'Indigo Frye (3236)', 'Angelica Vargas (1697)', 'Bevis Blair (4354)', 'Trevor Wilkinson (7067)', 'Kameko Lloyd (2660)', 'Giselle Gaines (9103)', 'Phyllis Bowers (6661)', 'Patrick Rowe (2615)', 'Cheyenne Manning (1743)', 'Jolie Carney (6741)', 'Joel Faulkner (6224)', 'Anika Bennett (9298)', 'Clayton Cherry (3687)', 'Shellie Stevenson (6100)', 'Marah Odonnell (3115)', 'Quintessa Wallace (5241)', 'Jayme Ramsey (8337)', 'Kyle Collier (8284)', 'Jameson Doyle (9258)', 'Rigel Blake (2124)', 'Joan Smith (3633)', 'Autumn Osborne (5180)', 'Renee Randolph (3100)', 'Fallon England (6976)', 'Fallon Jefferson (6807)', 'Kevyn Koch (9429)', 'Paki Mckay (504)', 'Connor Pitts (1966)', 'Rebecca Coffey (4975)', 'Jordan Morrow (1772)', 'Teegan Snider (5808)', 'Tatyana Cunningham (7691)', 'Owen Holloway (6814)', 'Desiree Delaney (272)', 'Armand Snider (8511)', 'Wallace Molina (4302)', 'Amela Walker (1637)', 'Denton Tillman (201)', 'Bruno Acevedo (7684)', 'Slade Hebert (5945)', 'Elmo Watkins (9282)',
      'Oleg Copeland (8013)', 'Vladimir Taylor (3846)', 'Sierra Coffey (7052)', 'Holmes Scott (8907)', 'Evelyn Charles (8528)', 'Steel Cooke (5173)', 'Roth Barrett (7977)', 'Justina Slater (3865)', 'Mara Andrews (3113)', 'Ulla Skinner (9342)', 'Reece Lawrence (6074)', 'Violet Clay (6516)', 'Ainsley Mcintyre (6610)', 'Chanda Pugh (9853)', 'Brody Rosales (2662)', 'Serena Rivas (7156)', 'Henry Lang (4439)', 'Clark Olson (636)', 'Tashya Cotton (5795)', 'Kim Matthews (2774)', 'Leilani Good (5360)', 'Deirdre Lindsey (5829)', 'Macy Fields (268)', 'Daniel Parrish (1166)', 'Talon Winters (8469)','@BrunoRafaello', '@RAM_Maroc', 'Hello', 'Bruno,', 'we', 'are', 'very', 'sorry', 'for', 'the', 'time', 'taken', 'on', 'the', 'conclusion', 'of', 'your', 'case.', 'We', 'have', 'reinforced', 'the', 'case', 'to', 'the', 'proper', 'area,', 'so', 'an', 'answer', 'can', 'be', 'provided', 'as', 'promptly', 'as', 'possible.', 'As', 'soon', 'as', 'we', 'receive', 'a', 'feedback,', 'we', 'will', 'get', 'back', 'to', 'you.', 'Thank', 'you.Bonjour', '@RAM_Maroc,', 'Voilà', '128', 'jours', 'que', 'vous', "m'avez", 'promis', 'un', 'dédommagement', 'sous', '4', 'à', '6', 'semaines,', 'serait-il', 'possible', 'de', 'voir', 'mon', 'dossier', 'avancer', '?', 'Pas', 'la', 'peine', 'de', 'me', 'dire', 'de', 'vous', 'contacter', 'en', 'DM,', 'je', "l'ai", 'déjà', 'fait', 'à', 'plusieurs', 'reprises', 'ainsi', 'que', 'par', 'courrielRoyal', 'Air', 'Maroc', '(RAM)', "n'a", 'jamais', 'porté', 'aussi', 'bien', 'son', 'nom:', 'elle', 'rame..@RAM_Maroc', 'Garder', 'mon', 'bagage', ',', 'c’est', 'fini', 'voyager', 'avec', 'vous', 'à', 'tout', 'jamais', ',', 'et', 'je', 'ferai', 'touts', 'pour', 'montrer', 'votre', 'vrai', 'visages', 'par', 'tout', 'dans', 'le', 'monde', ',', '#RAM', 'c’est', 'la', 'pire', 'compagnie', 'aérienne', 'dans', 'le', 'monde@RAM_Maroc', ',', 'service', 'de', 'pire', 'en', 'pire.', 'Vous', 'ne', 'montrez', 'même', 'pas', 'au', 'début', 'du', 'vol', 'comment', 'réagir', 'face', 'à', 'un', 'état', "d'urgence.", 'Et', 'même', 'en', 'cas', "d'urgence", "l'équipement", 'est', 'dégradé.', 'On', 'paie', 'cher', 
        'pour', 'rien', ',', 'pire', "qu'une", 'compagnie', "low-cost.Today's", 'Flight', 'Schedule', '#Gibraltar', '@easyJet', '@British_Airways', '@RAM_Maroc', '#VisitGibraltar', 'https://t.co/4FjSPqUXGb@RAM_Maroc', 'the', 'worst', 'airline', 'the', 'world.@TaoufikBouali', 'Bonsoir,', 'Pour', 'mieux', 'vous', 'assister,' ]

        self.data = AutocompleteEntry(autocompleteList, self.field1, listboxLength=6, width=16)

        # Input(self.field1, "      enter key search")
        self.data.grid(row=0, column=1, padx=3, pady=5, ipadx=88, ipady=11)########################

        self.button_add = Button(
            self.field2, text='   add element  ', font=self.font_butt, bg='red', command=self.add)
        self.button_add.grid(row=0, column=7, sticky='w',
                             padx=5, pady=1, ipadx=5, ipady=5)
        self.button_remove = Button(
            self.field2, text=' remove element ', font=self.font_butt, bg='red', command=self.remove)
        self.button_remove.grid(
            row=0, column=8, sticky='W',  padx=0, pady=1, ipadx=5, ipady=5)
        Checkbutton(self.field2, text=str("clean data"), variable=self.var_clean, bg="bisque", font=(
            "Courier", 14, "italic")).grid(row=0, column=9, padx=7, pady=0)

# run the
        # self.button_clear = Button(self.field2, text=' clear all ',font=self.font_butt, bg='red', command=self.add)
        # self.button_clear.grid(row=0, column=9,sticky='w',  padx=5,pady=1, ipadx=5, ipady=5)###
        # self.button_run = Button(
        # self.field2, text=' run ',font=self.font_butt, bg='red', width=13, command=self.remove)
        # self.button_run.grid(row=0, column=10,sticky='W',  padx=7,pady=2, ipadx=5, ipady=5)####

        self.field2 = Frame(self.fram, bg="#091833")
        self.field2.grid(row=0, column=5, columnspan=2, rowspan=3,
                         sticky='NS', padx=1, pady=1)
        self.list_box = Listbox(self.field2, height=4,
                                width=18,
                                bg="#f2a343",
                                activestyle='dotbox',
                                font="Helvetica",
                                fg="gray44")
        self.list_box.grid(row=0, column=7)
        for word in self.Words:
            self.list_box.insert(0,   word)

    def main(self):
        self.fram = LabelFrame(
            self.master, text=" Enter Details For Words Search :", fg="red",
            font=("Courier", 26, "italic"))
        self.fram.grid(row=5, columnspan=7, sticky='W',
                       padx=5, pady=0, ipadx=5, ipady=4)
        self.fram.configure(background="#091833")

        self.creat()

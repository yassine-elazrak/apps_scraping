
from tkinter import *
import re
from pprint import pprint

class AutocompleteEntry(Entry):
    def __init__(self, autocompleteList, *args, **kwargs):

        # Listbox length
        self.ll  = args
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 18

        # Custom matches function
        # print('arg', args[1],"n\n\n\n kwargs")
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
                return re.match(pattern, acListEntry)
                
            self.matchesFunction = matches

        
        Entry.__init__(self, *args, **kwargs)
        self.focus()

        self.autocompleteList = autocompleteList
        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)
        
        self.listboxUp = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = Listbox(self.ll[0] , width=37, height=2)
                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)####
                    self.listbox.bind('<<ListboxSelect>>', self.selection)
                    self.listbox.grid(row=2 , column=1)
                    # place(x=self.winfo_x() + 13, y=531)
                    self.listboxUp = True
                
                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END,w)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False
        
    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(ACTIVE))
            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(END)

    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
                
            if index != '0':                
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)
                
                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
                
            if index != END:                        
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)
                
                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index) 

    def comparison(self):
        return [ w for w in self.autocompleteList if self.matchesFunction(self.var.get(), w) ]

# if __name__ == '__main__':
#     autocompleteList = [ 'Dora Lyons (7714)', 'Hannah Golden (6010)', 'Walker Burns (9390)', 'Dieter Pearson (6347)', 'Allen Sullivan (9781)', 'Warren Sullivan (3094)', 'Genevieve Mayo (8427)', 'Igor Conner (4740)', 'Ulysses Shepherd (8116)', 'Imogene Bullock (6736)', 'Dominique Sanchez (949)', 'Sean Robinson (3784)', 'Diana Greer (2385)', 'Arsenio Conrad (2891)', 'Sophia Rowland (5713)', 'Garrett Lindsay (5760)', 'Lacy Henry (4350)', 'Tanek Conley (9054)', 'Octavia Michael (5040)', 'Kimberly Chan (1989)', 'Melodie Wooten (7753)', 'Winter Beard (3896)',
#      'Callum Schultz (7762)', 'Prescott Silva (3736)', 'Adena Crane (6684)', 'Ocean Schroeder (2354)', 'Aspen Blevins (8588)', 'Allegra Gould (7323)', 'Penelope Aguirre (7639)', 
#      'Deanna Norman (1963)', 'Herman Mcintosh (1776)', 'August Hansen (547)', 'Oscar Sanford (2333)', 'Guy Vincent (1656)', 'Indigo Frye (3236)', 'Angelica Vargas (1697)', 'Bevis Blair (4354)', 'Trevor Wilkinson (7067)', 'Kameko Lloyd (2660)', 'Giselle Gaines (9103)', 'Phyllis Bowers (6661)', 'Patrick Rowe (2615)', 'Cheyenne Manning (1743)', 'Jolie Carney (6741)', 'Joel Faulkner (6224)', 'Anika Bennett (9298)', 'Clayton Cherry (3687)', 'Shellie Stevenson (6100)', 'Marah Odonnell (3115)', 'Quintessa Wallace (5241)', 'Jayme Ramsey (8337)', 'Kyle Collier (8284)', 'Jameson Doyle (9258)', 'Rigel Blake (2124)', 'Joan Smith (3633)', 'Autumn Osborne (5180)', 'Renee Randolph (3100)', 'Fallon England (6976)', 'Fallon Jefferson (6807)', 'Kevyn Koch (9429)', 'Paki Mckay (504)', 'Connor Pitts (1966)', 'Rebecca Coffey (4975)', 'Jordan Morrow (1772)', 'Teegan Snider (5808)', 'Tatyana Cunningham (7691)', 'Owen Holloway (6814)', 'Desiree Delaney (272)', 'Armand Snider (8511)', 'Wallace Molina (4302)', 'Amela Walker (1637)', 'Denton Tillman (201)', 'Bruno Acevedo (7684)', 'Slade Hebert (5945)', 'Elmo Watkins (9282)',
#       'Oleg Copeland (8013)', 'Vladimir Taylor (3846)', 'Sierra Coffey (7052)', 'Holmes Scott (8907)', 'Evelyn Charles (8528)', 'Steel Cooke (5173)', 'Roth Barrett (7977)', 'Justina Slater (3865)', 'Mara Andrews (3113)', 'Ulla Skinner (9342)', 'Reece Lawrence (6074)', 'Violet Clay (6516)', 'Ainsley Mcintyre (6610)', 'Chanda Pugh (9853)', 'Brody Rosales (2662)', 'Serena Rivas (7156)', 'Henry Lang (4439)', 'Clark Olson (636)', 'Tashya Cotton (5795)', 'Kim Matthews (2774)', 'Leilani Good (5360)', 'Deirdre Lindsey (5829)', 'Macy Fields (268)', 'Daniel Parrish (1166)', 'Talon Winters (8469)','@BrunoRafaello', '@RAM_Maroc', 'Hello', 'Bruno,', 'we', 'are', 'very', 'sorry', 'for', 'the', 'time', 'taken', 'on', 'the', 'conclusion', 'of', 'your', 'case.', 'We', 'have', 'reinforced', 'the', 'case', 'to', 'the', 'proper', 'area,', 'so', 'an', 'answer', 'can', 'be', 'provided', 'as', 'promptly', 'as', 'possible.', 'As', 'soon', 'as', 'we', 'receive', 'a', 'feedback,', 'we', 'will', 'get', 'back', 'to', 'you.', 'Thank', 'you.Bonjour', '@RAM_Maroc,', 'Voilà', '128', 'jours', 'que', 'vous', "m'avez", 'promis', 'un', 'dédommagement', 'sous', '4', 'à', '6', 'semaines,', 'serait-il', 'possible', 'de', 'voir', 'mon', 'dossier', 'avancer', '?', 'Pas', 'la', 'peine', 'de', 'me', 'dire', 'de', 'vous', 'contacter', 'en', 'DM,', 'je', "l'ai", 'déjà', 'fait', 'à', 'plusieurs', 'reprises', 'ainsi', 'que', 'par', 'courrielRoyal', 'Air', 'Maroc', '(RAM)', "n'a", 'jamais', 'porté', 'aussi', 'bien', 'son', 'nom:', 'elle', 'rame..@RAM_Maroc', 'Garder', 'mon', 'bagage', ',', 'c’est', 'fini', 'voyager', 'avec', 'vous', 'à', 'tout', 'jamais', ',', 'et', 'je', 'ferai', 'touts', 'pour', 'montrer', 'votre', 'vrai', 'visages', 'par', 'tout', 'dans', 'le', 'monde', ',', '#RAM', 'c’est', 'la', 'pire', 'compagnie', 'aérienne', 'dans', 'le', 'monde@RAM_Maroc', ',', 'service', 'de', 'pire', 'en', 'pire.', 'Vous', 'ne', 'montrez', 'même', 'pas', 'au', 'début', 'du', 'vol', 'comment', 'réagir', 'face', 'à', 'un', 'état', "d'urgence.", 'Et', 'même', 'en', 'cas', "d'urgence", "l'équipement", 'est', 'dégradé.', 'On', 'paie', 'cher', 
# 'pour', 'rien', ',', 'pire', "qu'une", 'compagnie', "low-cost.Today's", 'Flight', 'Schedule', '#Gibraltar', '@easyJet', '@British_Airways', '@RAM_Maroc', '#VisitGibraltar', 'https://t.co/4FjSPqUXGb@RAM_Maroc', 'the', 'worst', 'airline', 'the', 'world.@TaoufikBouali', 'Bonsoir,', 'Pour', 'mieux', 'vous', 'assister,' ]
#     def matches(fieldValue, acListEntry):
#         pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
#         return re.match(pattern, acListEntry)
    
    # root = Tk()
    # entry = AutocompleteEntry(autocompleteList, root, listboxLength=6, width=32, matchesFunction=matches)
    # entry.grid(row=0, column=0)    
    # Button(text='Python').grid(column=0)
    # Button(text='Tkinter').grid(column=0)
    # Button(text='Regular Expressions').grid(column=0)
    # Button(text='Fixed bugs').grid(column=0)
    # Button(text='New features').grid(column=0)
    # Button(text='Check code comments').grid(column=0)
    # root.mainloop()
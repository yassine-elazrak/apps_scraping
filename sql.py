# import sqlite3

# class Database:
#     def __init__(self, db):
#         self.conn = sqlite3.connect(db)
#         self.cur = self.conn.cursor()
#         self.cur.execute(
#             "CREATE TABLE IF NOT EXISTS routers (id INTEGER PRIMARY KEY, hostname text, brand text, ram integer, flash integer)")
#         self.conn.commit()

#     def fetch(self, hostname=''):
#         self.cur.execute(
#             "SELECT * FROM routers WHERE hostname LIKE ?", ('%'+hostname+'%',))
#         rows = self.cur.fetchall()
#         return rows

#     def fetch2(self, query):
#         self.cur.execute(query)
#         rows = self.cur.fetchall()
#         return rows

#     def insert(self, hostname, brand, ram, flash):
#         self.cur.execute("INSERT INTO routers VALUES (NULL, ?, ?, ?, ?)",
#                          (hostname, brand, ram, flash))
#         self.conn.commit()

#     def remove(self, id):
#         self.cur.execute("DELETE FROM routers WHERE id=?", (id,))
#         self.conn.commit()

#     def update(self, id, hostname, brand, ram, flash):
#         self.cur.execute("UPDATE routers SET hostname = ?, brand = ?, ram = ?, flash = ? WHERE id = ?",
#                          (hostname, brand, ram, flash, id))
#         self.conn.commit()

#     def __del__(self):
#         self.conn.close()

import  twint
import sqlite3
import re 
import string
import pandas as pd
import numpy as np
import emoji
from threading import Timer, Thread
from os import  path
import os
import   shutil


class Sinonime:
    def __init__(self,index,word):
        self.keys =list( word)
        self.db = Database()
        self.index = index

    def get_word(self):
        self.c = twint.Config()
        self.c.Search = self.keys
        self.c.Limit = 100
        self.c.Store_csv = True
        self.c.Output = str(self.index)+'.csv' 
        self.c.Hide_output = True
        twint.run.Search(self.c)
        self.clean_file()


    def clean_file(self):
        name = str(self.index)+'.csv' 
        if not  path.exists(name):
            return
        df  = pd.read_csv(name)
        data = list(map( self.cl,df['tweet'].tolist()))
        # data = set(''.join(data))
        self.add(set(' '.join(data).split()))
        print("remove  fille", name)
        # os.remove(name)
        shutil.rmtree(name)


    def cl(self, text):
        text = text.strip()
        text = re.sub(emoji.get_emoji_regexp(), "", text)
        text = text.translate(str.maketrans("","",string.punctuation))
        text = re.sub(r'http\S+','',text)
        text = ' '.join(filter(lambda x: len(str(x)) > 3 and str(x).isalpha(), text.split()))
        return text

    def add(self, set_word):
        for word in set_word:
            self.db.insert(word)

    def run(self):
        Thread(target=self.get_word).start()


class  Database:
    def __init__(self):
        self.db_name = 'db_auto'
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY, name text)")
        self.conn.commit()

        if not self.all():
            self.arr = ["Royal Air Maroc" , "@RAM_Maroc",    "@RAM_Maroc", \
  "royalairmaroc", "الخطوط المغربيه" , "#الخطوط_الملكية_المغربية "\
 , "الخطوط الملكية المغربية"    , "لارام",  " لارام"\
,"الخطوط_الملكية_المغربية" ]
            for ward in self.arr:
                self.insert( ward)


    def run_query(self , query , parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def insert(self , word):
        # if self.run_query("SELECT * FROM product WHERE name LIKE ?", ('%'+word+'%',)):
        query = 'INSERT INTO product VALUES(NULL, ?)'
        parameters =  (word,)
        self.run_query(query, parameters)
        print('')

    def delete(self , word):
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, (word, ))
    
    def all(self):
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows =list(self.run_query(query))
        if db_rows:
            return( list(set(np.array(db_rows)[:,1])))
        return []
        # for row in db_rows:
        #     print(row[1])
        # print( )
    # def __del__(self):
    #     self.conn.close()
        

    





    









# def main():
#     db = Database()
#     arr = ["Royal Air Maroc" , "@RAM_Maroc",    "@RAM_Maroc", \
#   "royalairmaroc", "الخطوط المغربيه" , "#الخطوط_الملكية_المغربية "\
#  , "الخطوط الملكية المغربية"    , "لارام",  " لارام"\
# ,"الخطوط_الملكية_المغربية" ]
#     for ward in arr:
#         db.insert( ward)
#     db.all()
#     # cl = Sinonime('facebook')
#     # cl.get_word()


# if __name__ == "__main__":
#     main()
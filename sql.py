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


import sqlite3


class  Database:
    def __init__(self):
        self.db_name = 'db_auto'
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY, name text)")
        self.conn.commit()

    def run_query(self , query , parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def insert(self , word):
        if not self.run_query("SELECT * FROM product WHERE name LIKE ?", ('%'+word+'%',)):
            query = 'INSERT INTO product VALUES(NULL, ?)'
            parameters =  (word,)
            self.run_query(query, parameters)

    def delete(self , word):
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, (word, ))
    
    def all(self):
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            print(row)

    # def __del__(self):
    #     self.conn.close()
        

    










def main():
    db = Database()
    db.insert(  'llllolol')

    # db.insert(  'llrllolol')
    # db.insert(  'lllflolol')
    # db.insert(  'lldllolol')
    db.all()


if __name__ == "__main__":
    main()
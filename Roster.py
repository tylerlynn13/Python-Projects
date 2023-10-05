
import sqlite3
from sqlite3 import Error
def create_connection():
    """create database connection to a database that resides in the memory"""
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
#connecting to sqlite
import sqlite3
with sqlite3.connect(':memory:') as connection:
#creating table and
    c = connection.cursor()
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")

    Name = input("Name: Jean-Baptiste ")
    Species = input("Species:Human ")
    IQ = int(input("IQ: 122"))
    personData =(Name, Species, IQ)

    with sqlite3.connect(':memory:') as connection:
        c = connection.cursor()
        c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)

        c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
                  ('Human', 'Korean Dallas', 100))
    

if __name__== '__main__':
    create_connection()

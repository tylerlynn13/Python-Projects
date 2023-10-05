import sqlite3
connection = sqlite3.connect ("C:/Users/stamp/Documents/GitHub/Python-Projects/test_database.db")

c = connection.cursor()

c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()
connection = sqlite3.connect(':memory:')
c.execute("DROP TABLE IF EXISTS People")

connection.close()
import sqlite3
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
                    """)

    peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
    

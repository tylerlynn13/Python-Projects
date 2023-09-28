import sqlite3

conn = sqlite3.connect('test.db')
#creating table tbl_files
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fnames TEXT)")
    conn.commit()

conn = sqlite3.connect('test.db')

#tuple names

files_tuple = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', \
                 'data.pdf', 'myPhoto.jpg')
#to get only .txt endings
for x in files_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_fnames) VALUES (?)", (x,))
            print(x)


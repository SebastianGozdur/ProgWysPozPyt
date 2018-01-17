import sqlite3

connection = sqlite3.connect("example.db")

cursor = connection.cursor()

cursor.execute('''begin''')
cursor.execute('''CREATE TABLE IF NOT EXISTS books (id integer, name text, auid integer)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS authors (id integer, name text)''')

cursor.execute('''INSERT INTO books VALUES (1, 'First Test book', 43)''')
cursor.execute('''INSERT INTO authors VALUES (43, 'Jakis autor')''')


for row in cursor.execute('''SELECT * FROM books AS b INNER JOIN authors AS a ON b.auid = a.id''' ):
    print row

connection.close()



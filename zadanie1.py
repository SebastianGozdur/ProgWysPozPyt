import sqlite3

connection = sqlite3.connect("example.db")

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books (id integer, name text, author text)''')
cursor.execute('''INSERT INTO books VALUES (1, 'First Test book', 'First Test author')''')
cursor.execute('''INSERT INTO books VALUES (2, 'Second Test book', 'Second Test author')''')

for row in (cursor.execute('''SELECT * FROM books''')):
    print(row)

cursor.execute('''DELETE FROM books WHERE id = 1''')
print('after delete')

for row in (cursor.execute('''SELECT * FROM books''')):
    print(row)

connection.close()
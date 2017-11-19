'''
napisUnicode = u''
napisStr = napisUnicode.encode('utf8')
napisUnicode2 = napisStr.decode('utf8')

print len(napisUnicode), len(napisStr), len(napisUnicode2)
print isinstance('test', basestring)
print ' Test '.strip()
print ' Test '.strip().center(30)
print 'test '.strip().capitalize()

#wyrazenia regularne

import re
regex_email = re.complile(
  r(?P<adres>
    (?P<login>[\w+.]+)
      @
      (?P<domena>\w+(\.\w+)+)
    )
  )
  )

#serializacja
import json

slownik = {
  'k1' : 'w1',
  'k2' : 2,
  3 : [1,2,3]
}

jsonStr = json.dumps(slownik)
print jsonStr
slownik2 = json.loads(jsonStr)
print slownik2.items()

'''
#ZADANIE 1
'''
def fun(path, width):
  with open(path, 'r') as file:
    for line in file:
      print(line[:width])
      
fun('test.txt', 10);
'''	  
	  
#ZADANIE 2
'''
def fun(path, width):
  with open(path, 'r') as file:
    for line in file:
      print(line.center(width))
      
fun('test.txt', 100)
'''
#ZADANIE 3
'''
 import re
 
 regex_ip = re.compile(
 r
(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.
  (25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.
  (25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.
  (25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])
 );
 
 ip = '192.168.0.1'
 print(regex_ip.match(ip))
'''
 
 
#ZADANIE 4
'''
import re

regex_pesel = re.compile(
	r \d{11}$
);

print(regex_pesel.match('95010845251')
'''

#ZADANIE 5
class Book:
	title = ''
	isbn = ''
	number = ''
	author = ''
	
	def __init__(self, title, isbn, number, author):
		self.title = title
		self.isbn = isbn
		self.number = number
		self.author = author
		
class BookList:
	books = []
	state = ''
	
	def addBook(self, book):
		self.books.append(book)
		self.state = 'added book'
	
	def removeBook(self, index):
		self.books.pop()	 
	
	def saveState():
		file = open('state.txt', 'w+')
		file.write(self.state)
		
	
bookList = BookList()
bookList.addBook(Book("test", "124", "123232", "test auth"))
print(len(bookList.books))
		
		



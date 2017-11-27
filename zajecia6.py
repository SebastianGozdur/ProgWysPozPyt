'''def divide(x,y):
  try:
    result = x/y
  except ZeroDivisionError:
    print 'wyjatek'
  else:
      print 'brak wyjatku'
      return result
  finally:
      print 'koniec funkcji'
      
print divide(1, 0)

import urllib2

response = urllib2.urlopen('http://python.org/')
html = response.read()
print html

from xml.dom import minidom

xml = 'd'

print xml

doc = minidom.parseString(xml)

ele = doc.getElementsByTagName("el")

for el in ele:
  sid = el.getAttribute("id")
  test = el.getElementsByTagName("test")[0]
  print test.firstChild'''
  
#ZADANIE 1
'''
import math
def fun():
  try:
    inputValue = int(raw_input())
    print(math.sqrt(inputValue))
  except Exception, e:
    print e
    
fun()
'''

#ZADANIE 2
import re
class EmailManager:
  emails = ()
  
  def __init__(self, email):
    try:
      if self.validate(email) == None:
        raise Exception, 'Bledny format'
      else:
        print 'To jest email'
    except Exception, e:
      print e
    
  def validate(self, email):
    regexEmail = re.compile(
    r'''(?P<adres>
      (?P<login>[\w+.]+)      # login, np. m.j.panczyk+umcs.pl
      @                       # znak @
      (?P<domena>\w+(\.\w+)+) # domena, np. gmail.com
    )''',re.IGNORECASE | re.VERBOSE)
    return regexEmail.match(email)
    
obj = EmailManager('sebastian@gozdur.com')

  
  
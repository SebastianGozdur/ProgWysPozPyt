import urllib
import urllib.request
from xml.dom import minidom

req = urllib.request.Request('https://niebezpiecznik.pl/', headers={'User-Agent' : "Magic Browser"}) 
con = urllib.request.urlopen( req )
html =  con.read()
doc = minidom.parseString('<?xml version="1.0" encoding="iso-8859-1"?>'+str(html))


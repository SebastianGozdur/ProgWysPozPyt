from urllib.request import urlopen

response = urlopen('http://google.com')
html = response.read()
print(html)
file = open('zadanie4.html','w+')
file.write(str(html))
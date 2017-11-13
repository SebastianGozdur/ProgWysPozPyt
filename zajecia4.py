'''
slownik = {
'k1' : 'w1',
2 : [1,2,3],
(4,3,2) : 4
}

print(slownik)
'''

#STRINGI
'''
napis1 =  'Ala ma kota'
print(napis1.split())

#PLIKI
f = open("test.txt")
print f.read()
f.close()

#czytanie po linii
with open("plik.txt", "w") as f:
	f.write('test')
'''

#ZADANIE 1	
print('ZADANIE 1')
def fun(sentence):
	dict = {}
	for line in sentence.split('\n'):
		dict[line.split(':')[0]] = line.split(':')[1]
	return dict
	
print(fun('''k1:w1
k2:w2
k3:w3'''))


#ZADANIE 2
'''
import sys
print('\n\nZADANIE 2')

def splitFromFile(arg):
	dict = {}
	with open(arg) as file:
		for line in file:
			dict[line.split(':')[0]] = line.split(':')[1]
	return dict

print(splitFromFile(sys.argv[1]))
'''

#ZADANIE 3
'''
import sys
print('\n\nZADANIE 3')
def createDict(file):
	dict = {}
	with open(file,'r') as f:
		for line in f:
			for word in line.split():
				if word in dict:
					dict[word] += 1
				else:
					dict[word] = 1
	return dict
	
print(createDict(sys.argv[1]))
'''

#ZADANIE 4	
'''
import sys;
print('\n\nZADANIE 4')

def checkLines(fileName, searchExpression):
	if fileName != '-':
		with open(fileName, 'r') as f:
			for line in f:
				if searchExpression in line:
					print(line)
	else:
		lines = []
		while True:
			line = input()
			if line:
				lines.append(line)
			else:
				break
	
		for line in lines:
			if searchExpression in line:
				print(line)
				
checkLines(sys.argv[1],'test');
checkLines('-','test')
'''

#ZADANIE 5
def encrypt(fromFile, toFile, offset):
	translatedText = ''
	with open(fromFile, "r") as f:
		for line in f:
			translatedText = ceasarCipher(line, offset)
	
	fileToSave = open(toFile, "w+")
	fileToSave.write(translatedText)
	fileToSave.close()
	
def ceasarCipher(text, offset):
	result = ''
	for character in text:
		if character == ' ':
			result += character
			continue
		numericValue = ord(character)
		numericValue += offset
		if numericValue > ord('Z') and numericValue < ord('a'):
			numericValue -= 26
		if numericValue > ord('z'):
			numericValue -= 26
		result += chr(numericValue)
	return result
	
encrypt('zadanie5.txt', 'zadanie5_encrypted.txt', 5)
import re

class ElectronicDictionary:
	words = []
	
	def addWord(self, word):
		self.words.append(word)
		
	def removeWord(self, index):
		del self.words[index]
		
	def editWord(self, index, newValue):
		self.words[index] = newValue
		
	def find(self, term):
		matchObj = re.compile(r''+term+'+');
		searchedWords = []
		for word in self.words:
			if matchObj.match(word):
				searchedWords.append(word)
				
		print('Found words \n')
		for searchedWord in searchedWords:
			print searchedWord
		
	def display(self):
		for idx, word in enumerate(self.words):
			print '['+str(idx)+'] '+word ;
			
	def importToFile(self, filename):
		file = open(filename, 'w')
		for word in self.words:
			file.write(word+'\n')
		file.close()
	
	def exportFromFile(self, filename):
		try:
			with open(filename) as file:
				for line in file.readlines():
					line = line.rstrip()
					self.addWord(line)
		except e:
			print(e.getMessage())
		
def getSimpleUiInterface():
	return '''
-------------------------------------------------------
-					OPTIONS
- [0] - display words
- [1] - add word
- [2] - remove word
- [3] - find by term
- [4] - import to file
- [5] - export from file
- [6] - exit
--------------------------------------------------------
'''
		
elDict = ElectronicDictionary()
activeMenu = 1

while activeMenu:
	print(getSimpleUiInterface())
	inputValue = int(raw_input())
	
	if inputValue == 0:
		elDict.display()
	elif inputValue == 1:
		word = raw_input('type new word: ')
		elDict.addWord(word)
	elif inputValue == 2:
		index = int(raw_input('remove word - put index: '))
		elDict.removeWord(index)
	elif inputValue == 3:
		term = raw_input('type term')
		elDict.find(term)
	elif inputValue == 4:
		filename = raw_input('type filename: ')
		print(filename)
		elDict.importToFile(filename)
		print('words imported')
	elif inputValue == 5:
		filename = raw_input('type filename: ')
		elDict.exportFromFile(filename)
	elif inputValue == 6: 
		activeMenu = 0
	
	
	
	
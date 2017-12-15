import subprocess
import os

#with open(os.devnull, 'w') as devnull:
try:	
	out1 = subprocess.call('g++ -i test zadanie1.cpp', shell = True)
except e:
	print(e)

	

	
print(out1)
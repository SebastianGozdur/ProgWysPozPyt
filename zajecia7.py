import subprocess
import os

with open(os.devnull, 'w') as devnull:
	out1 = subprocess.call(["ls"], shell = True)
	
try:
	out2 = subprocess.check_call(["ls"], shell = True)
except subprocess.CalledProcessError as ex:
	print(ex);
	
print(out1)
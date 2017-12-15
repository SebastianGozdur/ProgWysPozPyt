import math

def fun(n):
	k = math.sqrt(n)
	output = ();
	while n>1:
		while n%k==0: 
			print(k)
			output.append(k)
			n/=k
			++k
	
	return k
	
print(fun(756))
# Write a python program to find all prime numbers within a given range.


def primenum(ul):
	
	for i in range(2,ul):
		for j in range(2,i):
			if(i % j==0):
				break
		else:
			print(i)
		
ul=int(input("Enter upper limit: "))
primenum(ul)
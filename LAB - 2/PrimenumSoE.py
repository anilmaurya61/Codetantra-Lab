# Write a Python program to print all primes smaller than or equal to, n using Sieve of Eratosthenes

val=int(input("Enter the value: "))
print("Following are the prime numbers smaller")
print("than or equal to "+str(val))
for i in range(2,val):
	for j in range(2,i):
		if(i % j==0):
			break
	else:
	   print(i)
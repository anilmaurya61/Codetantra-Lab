# Write a python program to print 'n' terms of Fibonacci series using iteration(Use Dynamic Programming).

def fib(x):
	if x<=1:
		return x
	else:
		return(fib(x-1)+fib(x-2))
		

n=int(input("How many terms to print?: "))
print("Fibonacci sequence:")
for i in range(n):
	print(fib(i))
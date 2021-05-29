# Write a python program to print 'n' terms of Fibonacci series using iteration(Recursion).

def fib(x):
	if x<=1:
		return x
	else:
		return(fib(x-1) + fib(x-2))
		

n=int(input("Enter the fibonacci term to be printed: "))
if n<=0:
	print("Invalid input")
else:
    print("Fibonacci Series is: ")
    for i in range(n):
        print((fib(i)),end=" ")
    print()
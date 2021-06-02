#Program to add two numbers using recursion
def add(x, y):
	if y==0:
		return x
	else:
		return (1+add(x,y-1))


	
	
# write your code here
	
		
a=int(input("Please enter an integer: "))
b=int(input("Please enter another integer: "))
print(add(a, b))
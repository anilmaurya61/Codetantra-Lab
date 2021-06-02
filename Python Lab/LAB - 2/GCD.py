def computeGCD(x, y):

	if(y==0):
		return x;
	else:
		return computeGCD(y,x%y)
		
x=int(input("Enter x value: "))
y=int(input("Enter y value: "))
print(computeGCD(x,y))

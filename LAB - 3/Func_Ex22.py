#Program to illustrate recursion
def recurfact(n):
	if (n==0 or n==1):
		return 1;
	return (n*recurfact(n-1));
	
num=int(input("Enter a number: "))
if(num<0):
	print("The factorial does not exist for a negative number")
else:
    print("The factorial of the given number is ",recurfact(num))


# write your code here
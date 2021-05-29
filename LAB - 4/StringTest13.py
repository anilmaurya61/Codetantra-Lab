#use len() to find length of String

s1=input("Enter first string: ")
s2=input("Enter second string: ")
l1=len(s1)
l2=len(s2)
if l1==l2:
	print("Both strings are of same length - Enclosing Not done")
elif l1>l2:
	print(s2+s1+s2)
else:
	print(s1+s2+s1)
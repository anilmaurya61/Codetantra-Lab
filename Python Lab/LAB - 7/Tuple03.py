x=tuple(input("Enter tuple elements separated by ,(Comma): ").split(','))
print("Elements of tuple:",x)
s=input("Enter an element to check whether it exist in tuple or not: ")
if s in x:
	print("True")
else:
	print("False")
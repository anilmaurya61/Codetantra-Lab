# write a program to print the every character in the given string twice

s=input("Enter a string: ")
print("The result is:  ",end="")
for i in s:
	print(i+i,end="")
print()
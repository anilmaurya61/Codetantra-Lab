s=input("Enter string: ")
l=len(s)
s1=s[::-1]
if l<3:
	print(s)
elif s1[:3]=="gni":
	print(s+"ly")
else:
	print(s+"ing")
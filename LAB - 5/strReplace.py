def changechar(s1):
	char=s1[0]
	s1=s1.replace(char,'$')
	s1=char+s1[1:]
	return s1


s=input("Enter input: ")
print(changechar(s))
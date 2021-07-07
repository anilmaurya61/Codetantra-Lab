a = []
b = []
c = str(input("Enter file name: "))
f = open(c,"rt")
a = f.readlines()
for i in a:	
	if i not in b:	
		b.append(i)
f.close()
f = open("NEW FILE","wt")
for i in b:
	f.write(i)
f.close()
f = open("NEW FILE","rt")
print("The new file after removing duplicates is: ")
for i in f:	
	print(i,end="")

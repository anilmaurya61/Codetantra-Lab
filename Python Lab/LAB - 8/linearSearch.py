lst=[]
lst=[int(item) for item in input("Enter the list of numbers: ").split()]
s=int(input("The number to search for: "))
flag=0
for i in range(len(lst)):
	if lst[i]==s:
	    print(str(s)+" was found at index "+str(i)+".")
	    flag=1
if flag==0:
	print(str(s)+" was not found"+str("."))
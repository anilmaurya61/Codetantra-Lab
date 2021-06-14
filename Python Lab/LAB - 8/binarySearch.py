lst=[]
n=int(input("Enter size of list: "))
for i in range(0,n):
	e=int(input("Enter your number: "))
	lst.append(e)

lst.sort()	
print("After sorting list is: ",lst)

s=int(input("The number to search for: "))

flag=0
for i in range(len(lst)):
	if lst[i]==s:
		print(str(s)+" was found at index "+str(i)+".")
		flag=1

if flag==0:
	print(str(s)+" was not found.")
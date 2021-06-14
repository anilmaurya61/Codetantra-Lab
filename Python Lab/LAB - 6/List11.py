listA=list(input("Enter list of elements separated by ,(comma): ").split(','))
print(listA)
listB=[]
for i in listA:
	if i not in listB:
		listB.append(i)	
print("List after removing all duplicates:",listB)
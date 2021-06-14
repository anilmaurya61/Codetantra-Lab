listA=[]
while(True):
	s=input("Enter element, 'XXX' to end: ")
	if s=="XXX":
		break;
	listA.append(s)
print("Initial stack")
print(listA)
print("Elements poped from stack:")
for i in range(3):
	l=listA.pop()
	print(l)
print("Stack after elements are poped:")
print(listA)

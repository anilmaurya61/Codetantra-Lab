listA=[]
while(True):
	s=input("Enter element, 'XXX' to end: ")
	if s=="XXX":
		break;
	listA.append(s)
print("Initial queue")
print(listA)
print("Elements dequeued from queue:")
for i in range(3):
	l=listA.pop(0)
	print(l)
print("Queue after removing elements:")
print(listA)

	
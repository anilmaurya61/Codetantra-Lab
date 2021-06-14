listA=list(input("Enter integer values separated by ,(Comma): ").split(','))
res=list(map(int,listA))
print(res)
if listA[0]>listA[-1]:
	print("Largest element among first and last elements:",listA[0])
else:
    print("Largest element among first and last elements:",listA[-1])
t=tuple(input("Enter integer elements separated by ,(Comma): ").split(','))
res=tuple(map(int,t))
print("Tuple elements:",res)
sum=0
for i in t:
	sum+=int(i)
print("Sum of tuple elements:",sum)

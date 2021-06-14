n=list(input("Enter the list of numbers: ").split(" "))
print(n)

for i in range(1,len(n)):
	key=n[i]
	j=i-1
	while j>=0 and key<n[j]:
		n[j+1]=n[j]
		j-=1
	n[j+1]=key
	
print(n)
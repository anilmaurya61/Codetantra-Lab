n=list(input("Enter the list of numbers: ").split(" "))
for i in range(len(n)):
	min_ind=i
	for j in range(i+1,len(n)):
		if n[min_ind]>n[j]:
			min_ind=j
			
	n[i],n[min_ind]=n[min_ind],n[i]
	
print(n)
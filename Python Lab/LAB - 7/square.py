def squareroot(n,l):
	x=n;
	count=0
	while(1):
		count+=1
		ans=0.5*(x+(n/x))
		if(abs(ans-x)<l):
			break
		x=ans
		g=float("{0:.4f}".format(ans))
	return g
	
	
n=int(input("Enter n: "))
l=float(input("Enter l: "))
print(squareroot(n,l))
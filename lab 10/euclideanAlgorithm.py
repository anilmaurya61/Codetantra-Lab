def gcd(a,b):
	i=0
	while i == 0:
		d = a%b
		if d == 0:
			return b
		else:
			a = b
			b = d

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
c = gcd(a,b)
print("gcd(",a,",",b,") = ",c)

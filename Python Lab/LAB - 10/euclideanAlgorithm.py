def gcd(a, b):	
	if a == 0:
		return b	
	return gcd(b%a,a)
	
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
print(f"gcd( {a} , {b} ) = ",gcd(a,b))
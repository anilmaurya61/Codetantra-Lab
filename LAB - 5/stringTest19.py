s=input("Enter a string: ")
l=len(s)
l1=int(l/2)
if l%2==0:
	print("First half string of given even length string is: "+s[:l1])
else:
	print("Second half string of given odd length string is: "+s[l1+1:])
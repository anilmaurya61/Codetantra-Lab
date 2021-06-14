key=list(input("Enter elements separated by ,(comma) for keys: ").split(','))
value=list(input("Enter elements separated by ,(comma) for values: ").split(','))
k=input("Enter key to check whether the element exist in dictionary or not: ")
if k in key:
	print("True")
else: 
	print("False")
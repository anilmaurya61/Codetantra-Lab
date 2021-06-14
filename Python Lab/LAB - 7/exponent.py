def pow(n,exponent):
  res =1
  while exponent !=0:
    res*=n
    exponent-=1
  return res
  
n=int(input("Enter n value: "))
e=int(input("Enter exponent value: "))
print("The value of "+str(n)+" to the power "+str(e)+" is: "+str(pow(n,e)))
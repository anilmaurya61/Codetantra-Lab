n=list(input("Enter a list element separated by space: ").split(' '))
res=list(map(int,n))
res.sort()
print("Largest element is:",res[-1])
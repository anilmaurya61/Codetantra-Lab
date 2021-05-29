# Get the Input string

# Sort the string

# Take empty List

# For each character in the input

# check whether printed or not

# print char and count

# add to printed list
from collections import Counter
def charfreq(s):
	s1=[]
	d=Counter(s)
	for i in d:
		print("'"+i+"'"+"\t"+str(d[i]))
		s1.append(i)
	print(s1)
	
	
s=input("Please enter sentence: ")
s1=sorted(s);
charfreq(s1)
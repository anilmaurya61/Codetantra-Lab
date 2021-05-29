
# Write a program that accepts a sequence of whitespace separated words as input and prints  the  words  after  removing  all  duplicate  words  and  sorting  them alphanumerically.

s=input("Enter input: ")
s1=s.split(' ')

word_list=[]
for i in s1:
	if i not in word_list:
		word_list.append(i)
	else:
		continue

print((' ').join(word_list))
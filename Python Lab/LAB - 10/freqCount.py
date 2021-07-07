a = str(input("Enter file name: "))
file = open(a,"rt")
fword = ""
f = 0
word = []
for line in file:	
	line_word = line.lower().replace(",","").replace(".","").split(" ")	
	for i in line_word:	
		word.append(i)
		for i in range(0,len(word)):
			count = 1
			for j in range(i +1,len(word)):	
				if(word[i] == word[j]):	
					count = count + 1	
				if(count> f):		
					f = count		
					fword = word[i];
print("Most repeated word: " + fword)
print("Frequency: " + str(f))
f.close()

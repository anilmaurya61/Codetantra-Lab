fin = open('InputData2.txt' , 'r')
charCount = wordCount = lineCount = 0			#Initialize Counters
for line in fin:								#Read each Line
	lineCount += 1
	word = 'Y'
	for letter in line:	
		if(letter != ' ' and word == 'Y' ):	
			wordCount  += 1		
			word = 'N'	
		elif (letter == " "):	
			word = 'Y'	
		for i in letter:	
			charCount += 1


print("Line count = ", lineCount)  #Print the Counts
print("Word count = ", wordCount)
print("Char count = ", charCount)
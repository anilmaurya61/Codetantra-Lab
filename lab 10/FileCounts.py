fin = open('InputData2.txt' , 'r')
charCount = wordCount = lineCount = 0			#Initialize Counters
for line in fin:								#Read each Line

	if line:
		lineCount += 1

	word = line.split()
	wordCount += len(word)

	charCount += len(line)

print("Line count = ", lineCount)  #Print the Counts
print("Word count = ", wordCount)
print("Char count = ", charCount)

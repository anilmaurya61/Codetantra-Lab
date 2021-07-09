fl = input("Enter file name: ")
input_file = open(fl,"r")
output_file = open("new_file.txt","w")
read_line = set()
for line in input_file:
	if line not in read_line:
		output_file.write(line)
		read_line.add(line)
		
input_file.close()
output_file.close()
file = open("new_file.txt","r")
print("The new file after removing duplicates is: ")
print(file.read())

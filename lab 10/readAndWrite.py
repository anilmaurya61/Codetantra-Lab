fn = input("Enter file name: ")
file1 = open(fn,"r")
print(file1.read())
file1.close()

file2 = open(fn,"a")
file2.write("World")
file2.close()

file3 = open(fn,"r")
print(file3.read())
file3.close()

# Write a python program to perform Matrix Multiplication.

def matrixA():
	print("Enter values for matrix - A")
	row=int(input("Number of rows, m = "))
	columns=int(input("Number of columns, n = "))
	matrix=[]
	for i in range(row):
		a=[]
		for j in range(columns):
			print("Entry in row: "+str(i+1)+" column: "+str(j+1))
			a.append(int(input()))
		matrix.append(a)

	print("Enter values for matrix - B")
	row1=int(input("Number of rows, m = "))
	columns1=int(input("Number of columns, n = "))
	matrixb=[]
	for i in range(row1):
	    b=[]
	    for j in range(columns1):
	    	print("Entry in row: "+str(i+1)+" column: "+str(j+1))
	    	b.append(int(input()))
	    matrixb.append(b)

	print("Matrix - A =",matrix)
	print("Matrix - B =",matrixb)
	result=[[0 for j in range (0,columns1)]for i in range (0 , row)]
	for i in range(0,row):
		for j in range(0,columns1):
			for k in range(0,columns):
				result[i][j]+=matrix[i][k]*matrixb[k][j]
	print("Matrix - A * Matrix- B =",result)

matrixA()


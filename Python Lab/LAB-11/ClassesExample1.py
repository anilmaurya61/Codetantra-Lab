class Student:
	pass

# # write your code here

	def __init__(self,name,age,degree):	
		self.name = name	
		self.age = age		
		self.degree = degree	
		
a = str(input("Enter name of the student:"))
b = str(input("Enter age of the student:"))
c = str(input("Enter degree of the student:"))
Stud_1 = Student(a,b,c)
print("Stud_1.name:",Stud_1.name)
print("Stud_1.age:",Stud_1.age)
print("Stud_1.graduate:",Stud_1.degree)

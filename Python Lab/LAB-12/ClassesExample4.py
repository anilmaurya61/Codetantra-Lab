class Student:
	def __init__(self, name, age, email):
		# Write your code here
		self.name = name
		self.age =age
		self.email =email
	def studentDetails(self):
		# Write your code here
		print(f"Name: {self.name} , age: {self.age} , email: {self.email}")	
		
a = str(input("Enter name of the student: "))
b = int(input("Enter age of the student: "))
c = str(input("Enter emial of the student: "))
student = Student(a,b,c)
student.studentDetails()

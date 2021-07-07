class Employee:
	pass
	def __init__(self,name,salary):	
		self.name = name		
		self.salary = salary
		
a = str(input("Please enter an employee name: "))
Emp_1 = Employee(a,25000)
print("Emp_1.name:",Emp_1.name)
print("Emp_1.salary:",Emp_1.salary)

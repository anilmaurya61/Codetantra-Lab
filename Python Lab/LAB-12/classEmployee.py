class Employee:
	def __init__(self, name, salary):
		self.name = name
		self.salary=salary
		
    def displayEmployee(self):
        print(f"Name: {self.name} , Salary: {self.salary}")
     
a = str(input("Enter name of the employee: "))
b = str(input("Enter salary of the employee: "))
Emp = Employee(a,b)
Emp.displayEmployee()	
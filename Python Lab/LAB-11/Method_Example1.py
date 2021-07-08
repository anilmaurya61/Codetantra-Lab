class Person:
	def __init__(self):		
		pass
	def setName(self,name):		
		self.name = name	
	def getName(self):	
		return self.name
		
a = str(input("Enter name of the person1: "))
b = str(input("Enter name of the person2: "))
p1 = Person()
p2 = Person()
p1.setName(a)
p2.setName(b)
print(f"Person P1 name: {p1.getName()}")
print(f"Person P2 name: {p2.getName()}")

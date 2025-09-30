# Super function : 
#In Python, the super() function is used to call methods from a parent (superclass) inside a child (subclass). 
# It allows you to extend or override inherited methods while still reusing the parent’s functionality.

#Syntax : super()

class Emp:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class fun(Emp):
    def __init__(self, id, name, email):
        super().__init__(id, name)   #Calls Emp’s __init__
        self.email = email

obj = fun(101, "Olivia", "olivia@email.com")
print(obj.id, obj.name, obj.email)

# problem when not using super() :
#If a child class overrides the constructor without using super(),
#the parent class’s attributes won’t be initialized, which can lead to errors:
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Emp(Person):
    def __init__(self, name, id):
        self.name_ = name   # Forgot to call Person’s __init__

emp = Emp("Jack", 103)
print(emp.name)
#output : AttributeError: 'Emp' object has no attribute 'name'

#FIxing the above problem using super() :
class Person1:  
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Emp1(Person1):  
    def __init__(self, name, id):
        super().__init__(name, id) 

emp = Emp1("James", 103)
print(emp.name, emp.id)


#Polymorphism in Python:
#Technically, in Python, polymorphism allows same method,
#  function or operator to behave differently depending on object it is working with.
#  This makes code more flexible and reusable.

# Need of Polymorphism:
# Ensures consistent interfaces across different classes.
# Allows objects to respond differently to the same method call.
# Promotes loose coupling by relying on shared behavior, not specific types.
# Enables writing flexible, reusable code that works across types.
# Simplifies testing and future extension of code.

#Types of Polymorphism:
# 1. Compile Time Polymorphism (Static Polymorphism):
#    This is achieved using function overloading or method overloading.
#    It means deciding which method or operation to run during compilation,
#        usually through method overloading.

#Note :
# In Python:

# True compile-time polymorphism is not supported.
# Instead, Python mimics it using default arguments or *args/**kwargs.
# Operator overloading can also be seen as part of polymorphism, though it is implemented at runtime in Python.

# 2. Runtime Polymorphism (Dynamic Polymorphism): 
#     1. method overiding  2. Duck Typing 3. Operator overloading
#    This is achieved using function overriding or method overriding .
#    It means deciding which method or operation to run during runtime,
#        usually through method overriding.

#Example of compile time polymorphism:
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(5, 10))       # Two arguments
print(calc.add(5, 10, 15))   # Three arguments
print(calc.add(1, 2, 3, 4))  # Any number of arguments

#Example of runtime polymorphism:
# Method Overriding
# We start with a base class and then a subclass that "overrides" the speak method.
class Animal:
    def speak(self):
        return "I am an animal."

class Dog(Animal):
    def speak(self):
        return "Woof!"

print(Dog().speak())

# 2 Duck Typing
class Cat:
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    # This function works for both Dog and Cat because they both have a 'speak' method.
    return animal.speak()

print(make_animal_speak(Cat()))
print(make_animal_speak(Dog()))

# 3 Operator Overloading
# We create a simple class that customizes the '+' operator.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # This special method defines the behavior of the '+' operator.
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

print(v3)
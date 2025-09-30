#Object Oriented Programming is a fundamental concept in Python,
# empowering developers to build modular,
#  maintainable and scalable applications.

#OOP is a way of organizing code that uses objects and classes 
# to represent real-world entities and their behavior.
#  In OOP, object has attributes thing that has specific data
#  and can perform certain actions using methods.

#Key Features of  OOPs :

# Organizes code into classes and objects
# Supports encapsulation to group data and methods together
# Enables inheritance for reusability and hierarchy
# Allows polymorphism for flexible method implementation
# Improves modularity, scalability, and maintainability

# Core principles of OOPs:
#1. Object : A real-world entity with attributes and behavior
#2. Class : A blueprint for creating objects with specific attributes and behavior
#3. Encapsulation : bundling data and methods together into a single unit
#4. Inheritance : A way of creating new classes by inheriting properties and methods from existing classes
#5. Polymorphism : A way of allowing objects of different classes to be treated as objects of a common superclass or interface
#6. Abstraction : Hiding the internal details of a class and only exposing the necessary functionality to the user

# 1 class :
#Note : We will use 'class' keyword to define a class in Python

#creating a class
#synatx : class ClassName: 
class Dog :
    species='Canine' #class attribute
    def __init__(self,name ,age): #constructor method
        self.name =name #
        self.age=age

#2. Object
#Note : An object is an instance of a class
# syntax : object_name = class_name(arguments)

#creating an object
dog1=Dog("Tommy",10)

#3. Accessing attributes and methods
# syntax : object_name.attribute_name or object_name.method_name()

#accessing attributes
print(dog1.name) # Output: Tommy
print(dog1.age) # Output: 10
print(dog1.species) # Output: Canine
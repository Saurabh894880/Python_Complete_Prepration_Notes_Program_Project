 # Inheritance :
# Inhertance allows a class (child class) to acquire properties and methods from a parent class (base class).
# It supports hierarchical relationships and promotes code reusability.

# Types of Inheritance : 
# 1. Single Inheritance : A child class can inherit properties and methods from only one parent class.
# 2. Multiple Inheritance : A child class can inherit properties and methods from multiple parent classes.
# 3. Multilevel Inheritance : A child class can inherit properties and methods from a parent class,
#  which in turn inherits properties and methods from another parent class.
# 4. Hierarchical Inheritance : Multiple child classes inherit from a single parent class.
# 5 .Hybrid Inheritance : A combination of two or more types of inheritance.

# Syntax :
# class ChildClass(BaseClass1, BaseClass2):
#     # Child class body


# Example :
# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")

# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name}Guides the way!")

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

# Example Usage
lab = Labrador("Buddy") 
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()
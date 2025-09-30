# Constructor in python : 
# In Python, constructors are special methods used for object initialization.
#  The constructor is written as __init__().

# Syntax: def __init__(self, parameters):
#  self.parameters = parameters

# Types of constructors:
# 1. Default constructor: This constructor does not have any parameters except self. 
#    It initializes the attributes of the class to default values.
#   Automatically provided by Python if you don’t define one.

# Example of a class with a default constructor:

class Dog1:
    def __init__(self):
        self.name = 'Kishan'
        self.age = 20
    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

d=Dog1()
d.display_info()  # Output: Name: Kishan, Age: 20

# 2. Parameterized constructor: This constructor takes parameters when creating an object.
#   It initializes the attributes of the class with the given values.

# Example of a class with a parameterized constructor:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

d=Person('Buddy', 5)
d.display_info()  # Output: Name: Buddy, Age: 5

# 3. Copy constructor: This constructor creates a copy of an existing object.
#   It initializes the attributes of the class with the values of the existing object.

# Note: Python does not provide a built-in copy constructor like C++.

class Dog:
    def __init__(self, name=None):
        if isinstance(name, Dog):   # Copy constructor
            self.name = name.name
        elif isinstance(name, str): # Parameterized constructor
            self.name = name
        else:                       # Default constructor
            self.name = "Unknown"

    def display(self):
        print(f"Dog's Name: {self.name}")

# Example usage
d1 = Dog("Max")     # parameterized constructor
d2 = Dog(d1)        # copy constructor
d3 = Dog()          # default constructor

d1.display()
d2.display()
d3.display()

#NOte :
# isintance() function checks if the object is an instance of a class.
#syntax: isinstance(object, class)
# Returns True if the object is an instance of the class, otherwise False.
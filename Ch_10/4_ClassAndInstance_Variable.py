# Class and Instance variables

# Class Variables :
# These are the variables that are shared among all instances of a class.
#  They are defined outside of the any methods and can be accessed using the class name itself.
#  They are typically used to store data that is common to all instances.
# All objects of the class share the same value for a class variable unless explicitly overridden in an object.

# Instance Variables :
# These are the variables that are specific to each instance of a class.
# they are defined within the __init__() method and can be accessed using the instance name followed by the variable name.
#Each object maintains its own copy of instance variables, independent of other objects.

# Example of a class with class and instance variables :

class Dog :
    species = "Canine"  # Class variable
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age  # Instance variable

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 7)
print(dog1.species)  # Output: Canine   # Accessing class variable
print(dog1.name)  # Output: Buddy   # Accessing instance variable
print(dog1.age)  # Output: 5   # Accessing instance variable

dog1.name = "Rex"  # Modifying instance variable
print(dog1.name)  # Output: Rex   # Accessing modified instance variable

dog2.species = "Feline"  # Modifying class variable
print(dog2.species)  # Output: Feline   # Accessing modified class variable

print(dog2.name)  # Output: Max   # Accessing instance variable (not modified by class variable)

print(Dog.species)  # Output: Canine   # Accessing class variable (not modified by instance variable)
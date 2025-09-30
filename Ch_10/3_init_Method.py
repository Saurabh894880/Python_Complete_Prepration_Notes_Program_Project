# __init__ method

# This method is the constructor in Python, automatically called when a new object is created. 
# It initializes the attributes of the class.
# Syntax : def __init__(self, attribute1, attribute2,...):

#Example of a class with an __init__ method :

class Dog  :
    def __init__(self, name='Kishan', age=20) :
        self.name =name #instance variable to store the name of the dog
        self.age=age    #instance variable to store the age of the dog

dog1=Dog()
print(dog1.name)  # Output: None
print(dog1.age)   # Output: None

dog2=Dog('Tom', 25)
print(dog2.name)  # Output: Tom
print(dog2.age)   # Output: 25


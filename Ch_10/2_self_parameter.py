# Self Parameter :
#In Python, self is a fundamental concept when working with object-oriented programming (OOP).
# It represents the instance of the class being used.
#   Whenever we create an object from a class, self refers to the current object instance.
#It is essential for accessing attributes and methods within the class

class Dog :
    species='Canine' #class attribute
    def __init__(self,name ,age): #constructor method
        self.name =name #
        self.age=age

dog1=Dog('Buddy',3)
dog2=Dog('Max',5)

#Accessing instance and class attributes
print(dog1.name,dog1.age,dog1.species) #Output: Buddy 3 Canine 
print(dog2.name,dog2.age,dog2.species) #Output: Max 5 Canine

#Accessing class attributes
print(Dog.species) #Output: Canine
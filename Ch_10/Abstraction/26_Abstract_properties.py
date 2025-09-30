# #Abstract Properties
# Abstract properties work like abstract methods but are used for properties.
#  These properties are declared with @property decorator and marked as abstract using @abstractmethod. 
# Subclasses must implement these properties.

from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass  # Abstract property, must be implemented by subclasses

class Dog(Animal):
    @property
    def species(self):
        return "Canine"

# Instantiate the concrete subclass
dog = Dog()
print(dog.species)
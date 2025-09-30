# #Abstract Class Instantiation
# Abstract classes cannot be instantiated directly. 
# This is because they contain one or more abstract methods or properties that lack implementations.
#  Attempting to instantiate an abstract class results in a TypeError.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

animal = Animal() # TypeError: Can't instantiate abstract class Animal with abstract methods make_sound
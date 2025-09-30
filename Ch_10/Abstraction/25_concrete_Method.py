# Concrete Method
# Concrete methods are fully implemented methods within an abstract class. 
# Subclasses can inherit and use them directly,
#  promoting code reuse without needing to redefine common functionality.

from abc import ABC, abstractmethod
class Animal(ABC) :
    @abstractmethod
    def sound(self) :
        pass # Abstract method that must be implemented by subclasses

    def move(self) :
        print("Animal moves")  # Concrete method that can be overridden by subclasses


class Dog(Animal) :
    def sound(self) :
        print("Woof!")

d=Dog()
d.sound()  # Output: Woof! # Concrete method overridden by Dog subclass
d.move()  # Output: Animal moves # Concrete method inherited from Animal class
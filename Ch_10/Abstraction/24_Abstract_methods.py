# Abstract Method
# Abstract methods are method declarations without a body defined inside an abstract class. 
# They act as placeholders that force subclasses to provide their own specific implementation,
#  ensuring consistent structure across derived classes.

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, no implementation here

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

d=Dog()
d.make_sound()
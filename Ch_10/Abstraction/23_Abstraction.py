# Data Abstraction in python :
# Data abstraction means showing only the essential features
#  and hiding the complex internal details.

# Technically, in Python abstraction is used to hide
#  the implementation details from the user and expose only necessary parts,
#  making the code simpler and easier to interact with.

# Need of Data Abstraction :

# It hides internal logic and only shows the necessary details, making it easier to use complex systems.
# Sensitive or unnecessary details are not exposed, reducing chances of misuse or accidental changes.
# Users can focus on what the object does instead of how it does it.
# Internal changes don’t affect external code, making it easier to update or modify code components.


# Abstract Base Class :

# In Python, an Abstract Base Class (ABC) is used to achieve data abstraction 
# by defining a common interface for its subclasses.
#  It cannot be instantiated directly and serves as a blueprint for other classes.

# Abstract classes are created using abc module and @abstractmethod decorator,
#  allowing developers to enforce method implementation in subclasses while hiding complex internal logic.

# Example of an abstract class and its subclass :

from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())


# Components of Abstraction :
# 1. Abstract methods : These are methods that must be implemented in the subclasses.
# 2. Concrete methods : These are methods that are not abstract and have some implementation.
# 3. abstract properties : These are properties that must be implemented in the subclasses.
# 4. Class instantiation Rules : These are rules that govern the instantiation of abstract classes and their subclasses.


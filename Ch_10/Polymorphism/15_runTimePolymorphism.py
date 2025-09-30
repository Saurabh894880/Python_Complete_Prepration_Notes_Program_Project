# #2. Runtime Polymorphism (Overriding)
# Runtime polymorphism means that the behavior of
#  a method is decided while program is running, 
# based on the object calling it.

# In Python, this happens through Method Overriding 
# a child class provides its own version of a method 
# already defined in the parent class.
#  Since Python is dynamic, it supports this,
#  allowing same method call to behave differently for different object types.

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())
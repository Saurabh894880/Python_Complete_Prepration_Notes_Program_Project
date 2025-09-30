# #   Polymorphism in Functions :

# In Python, polymorphism lets functions accept 
# different object types as long as they support needed behavior.
#  Using duck typing, Python focuses on whether 
# an object has right method not its type allowing flexible
#  and reusable code.

#for example :
class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())

perform_task(Pen())
perform_task(Eraser())


#Polymorphism in built-in functions:

# Python’s built-in functions like 
# len() and max() are polymorphic 
# they work with different data types and 
# return results based on type of object passed. 
# This showcases it's dynamic nature, where same
#  function name adapts its behavior depending on input.

# for example:
print(len("Hello"))  # String length
print(len([1, 2, 3]))  # List length

print(max(1, 3, 2))  # Maximum of integers
print(max("a", "z", "m"))  # Maximum in strings



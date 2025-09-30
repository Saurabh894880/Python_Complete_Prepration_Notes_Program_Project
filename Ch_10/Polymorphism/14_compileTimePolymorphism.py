# 1. Compile-time Polymorphism
# Compile-time polymorphism means deciding which 
# method or operation to run during compilation, 
# usually through method or operator overloading.

# Languages like Java or C++ support this. 
# But Python doesn’t because it’s dynamically typed
#  it resolves method calls at runtime, not during compilation. 
# So, true method overloading isn’t supported in Python, 
# though similar behavior can be achieved using default or variable arguments.

# Example of compile-time polymorphism in Python:

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())            
print(calc.multiply(4))           

# Using multiple arguments
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))

#Types of functions
# 1. Built-in Functions: These are functions that are provided by the programming language itself and are readily available for use. Examples include print(), len(), and input() in Python.
# 2. User-Defined Functions: These are functions that are created by the programmer to
#    perform specific tasks. They are defined using the def keyword in Python.

# 3. Anonymous Functions (Lambda Functions): These are small, unnamed functions that are defined using the lambda keyword in Python. They are typically used for short, throwaway functions that are not intended to be reused.
# 4. Recursive Functions: These are functions that call themselves in order to solve a problem. They typically have a base case to terminate the recursion and a recursive case to break down the problem into smaller subproblems.
# 5. Higher-Order Functions: These are functions that can accept other functions as arguments or return functions as results. They enable functional programming techniques and allow for more abstract and flexible code.
# 6. Generator Functions: These are functions that use the yield keyword to produce a sequence of values over time, instead of returning a single value. They are useful for handling large datasets or infinite sequences. 
# 7.decorator Functions: These are functions that modify or enhance the behavior of other functions. They are defined using the @decorator syntax in Python and are commonly used for tasks such as logging, authentication, and caching.
# 8. Asynchronous Functions: These are functions that can be executed asynchronously, allowing for non-blocking operations. They are defined using the async keyword in Python and are commonly used for tasks such as network requests and file I/O.
# 9. Callback Functions: These are functions that are passed as arguments to other functions and are invoked at a later time. They are commonly used in event-driven programming and asynchronous programming.
# 10. Method Functions: These are functions that are associated with objects and are defined within a class. They operate on the data contained within the object and can access its attributes and other methods.
# 11. Static Functions: These are functions that are defined within a class but do not operate on instance data. They are defined using the @staticmethod decorator in Python and can be called without creating an instance of the class.
# 12. Class Functions: These are functions that are defined within a class and operate on class-level data. They are defined using the @classmethod decorator in Python and can be called on the class itself rather than on an instance of the class.


#Example of each function type wrtten above 

# Built-in Function
print("Hello, World!")  # Using the built-in print() function

# User-Defined Function
def add(a, b):
    return a + b    
print(add(3, 5))  # Output: 8

# Anonymous Function (Lambda Function)
square = lambda x: x ** 2
print(square(4))  # Output: 16
# Recursive Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

# Higher-Order Function
def apply_function(func, value):
    return func(value)  
print(apply_function(lambda x: x * 2, 5))  # Output: 10
# Generator Function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for number in count_up_to(5):
    print(number)  # Output: 1 2 3 4 5
# Decorator Function
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Before calling the original function")
        result = original_function(*args, **kwargs)
        print("After calling the original function")
        return result
    return wrapper_function
@decorator_function
def greet(name):
    print(f"Hello, {name}!")    

greet("Alice")
# Output:
# Before calling the original function
# Hello, Alice!
# After calling the original function

# Asynchronous Function
import asyncio  
async def async_function():
    print("Start")
    await asyncio.sleep(1)
    print("End")
asyncio.run(async_function())  # Output: Start (waits 1 second) End
# Callback Function
def callback_function(message):
    print(f"Callback received: {message}")
def perform_action(action, message):
    action(message)
perform_action(callback_function, "Hello from callback!")  # Output: Callback received: Hello from callback!
# Method Function
class MyClass:
    def __init__(self, value):
        self.value = value
    def display_value(self):
        print(f"Value: {self.value}")
obj = MyClass(10)
obj.display_value()  # Output: Value: 10

# Static Function
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
print(MathOperations.add(3, 5))  # Output: 8

# Class Function
class Counter:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count
print(Counter.increment())  # Output: 1
print(Counter.increment())  # Output: 2 




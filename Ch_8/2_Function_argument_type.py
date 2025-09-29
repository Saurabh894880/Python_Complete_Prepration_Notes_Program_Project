# Function Arguments : Different Types
# Functions in Python can accept different types of arguments. Here are some common types of function arguments


# 1. Positional Arguments: These are the most common type of arguments where the values are passed to the function in the same order as the parameters are defined.
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet("Alice", 30)  # Output: Hello, Alice! You are 30 years old.
greet("Bob", 25)    # Output: Hello, Bob! You are 25 years old.


# 2. Keyword Arguments: These arguments are passed to the function using the parameter names, allowing you to specify the values in any order.
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")   
greet(age=30, name="Alice")  # Output: Hello, Alice! You are 30 years old.
greet(name="Bob", age=25)    # Output: Hello, Bob! You are 25 years old.


# 3. Default Arguments: These arguments have default values assigned to them in the function definition
def greet(name, age=18):
    print(f"Hello, {name}! You are {age} years old.")
greet("Alice")        # Output: Hello, Alice! You are 18 years old.
greet("Bob", 25)     # Output: Hello, Bob! You are 25 years old.

# 4. Variable-Length Arguments: These arguments allow you to pass a variable number of values to the function. In Python, you can use *args for positional variable-length arguments and **kwargs for keyword variable-length arguments.
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_numbers(1, 2, 3))        # Output: 6
print(sum_numbers(4, 5, 6, 7, 8))  # Output: 30

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")    

display_info(name="Alice", age=30, city="New York")
# Output:   # name: Alice
#           age: 30
#           city: New York
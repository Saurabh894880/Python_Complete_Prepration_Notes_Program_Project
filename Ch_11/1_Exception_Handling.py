#   Exception Handling in Python :

# Python Exception Handling allows a program to gracefully handle unexpected events
#  (like invalid input or missing files) without crashing.
#  Instead of terminating abruptly, Python lets you detect the problem, 
# respond to it, and continue execution when possible.

# Example of a simple exception:

n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")


# Difference between Errors and Exceptions:

# - Errors are issues that prevent the program from running correctly.
#   Examples: SyntaxError, NameError, TypeError, etc.

# - Exceptions are errors that occur during the execution of a program.
#   Examples: ZeroDivisionError, FileNotFoundError, etc.

# Example :

# Syntax Error (Error)

# print("Hello world"  # Missing closing parenthesis

# ZeroDivisionError (Exception)

n = 10
# res = n / 0

# Synatx :
'''
try:
      # Code 
except SomeException:
      # Code 
else:
     # Code 
finally:
    # Code

'''

# try: Runs the risky code that might cause an error.
# except : Catches and handles the error if one occurs.
# else: Executes if no error occurs in the try block.
# finally: Always executes, whether an error occurred or not.


# Example:
try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")

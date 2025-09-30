# Raise an Exception :
# We raise an exception in Python using the raise keyword followed by an instance of the exception class that we want to trigger.
#  We can choose from built-in exceptions or define our own custom exceptions by inheriting from Python's built-in Exception class.

#Syntax : raise ExceptionName(message)

# Example :
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)
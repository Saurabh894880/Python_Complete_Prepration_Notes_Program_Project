# #1. Catching Specific Exceptions
# Catching specific exceptions makes code to respond to different exception types differently.
#  It precisely makes your code safer and easier to debug.
#  It avoids masking bugs by only reacting to the exact problems you expect.

try:
    x = int("str")  # This will cause ValueError
    inv = 1 / x   # Inverse calculation
    
except ValueError:
    print("Not Valid!")
    
except ZeroDivisionError:
    print("Zero has no inverse!")
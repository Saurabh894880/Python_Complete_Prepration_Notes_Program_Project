# #2. Catching Multiple Exceptions
# We can catch multiple exceptions in a single block if we need to handle them in the same way
#  or we can separate them if different types of exceptions require different handling.

a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")
# Recursion : A function that calls itself
# Example of a recursive function to calculate factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

# Example of a recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))  # Output: 8 (0, 1, 1, 2, 3, 5, 8)
print(fibonacci(10)) # Output: 55
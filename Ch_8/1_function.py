#   functions : block of code that performs a specific task
#  def function_name(parameters):
#      function_body
#      return value


def is_prime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False
print(is_prime(11))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
print(is_prime(-3))  # False

#properties of functions
# 1. Reusability: Functions allow you to reuse code by calling the function multiple times without rewriting it.
# 2. Modularity: Functions help break down complex problems into smaller, manageable parts.
# 3. Readability: Functions improve code readability by providing meaningful names that describe their purpose.
# 4. Maintainability: Functions make it easier to maintain and update code since changes can
#    be made in one place rather than throughout the codebase.
# 5. Abstraction: Functions provide a level of abstraction, allowing you to focus on higher-level concepts without getting bogged down in implementation details.
# 6. Parameterization: Functions can accept parameters, allowing you to pass different values and customize their behavior.
# 7. Return Values: Functions can return values, enabling you to capture and use the
#    results of computations or operations.
# 8. Scope: Functions have their own scope, meaning variables defined within a function are
#    local to that function and do not interfere with variables in the global scope.
# 9. Recursion: Functions can call themselves, enabling recursive algorithms to solve problems.
# 10. Documentation: Functions can be documented with docstrings, providing information about their purpose, parameters, and return values.
# 11. Higher-Order Functions: Functions can accept other functions as arguments or return functions as results, enabling functional programming techniques.
# 12. Built-in Functions: Python provides a rich set of built-in functions that can be used directly without the need for custom implementation.
# 13. Anonymous Functions: Python supports anonymous functions (lambda functions) for short, throwaway functions.
# 14. Default Arguments: Functions can have default argument values, allowing you to call them with fewer arguments.
# 15. Variable-Length Arguments: Functions can accept a variable number of arguments using *args and **kwargs.
# 16. Decorators: Functions can be modified or enhanced using decorators, which are functions that wrap other functions.
# 17. Closures: Functions can capture and remember the environment in which they were created, allowing for data encapsulation and state retention.
# 18. Error Handling: Functions can include error handling mechanisms to manage exceptions and ensure robust execution.
# 19. Testing: Functions can be easily tested in isolation, making it simpler to verify their correctness and behavior.
# 20. Performance Optimization: Functions can be optimized for performance, allowing for efficient execution of specific tasks.


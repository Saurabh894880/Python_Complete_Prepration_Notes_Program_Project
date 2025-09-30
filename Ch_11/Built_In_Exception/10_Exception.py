# 3. ArithmeticError
# - The ArithmeticError class is the base for all errors related to mathematical operations.
# - You don’t usually raise it directly, but it provides a way to catch all math-related errors in one block.

try:
    raise ArithmeticError("Arithmetic error occurred")
except ArithmeticError as e:
    print(e)
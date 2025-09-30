# 1. BaseException
# - The BaseException class is the root of Python’s exception hierarchy.
# - All other exceptions directly or indirectly inherit from it.
# - While it is rarely used directly in code,
# - it is important because it forms the foundation of Python’s error-handling system.

try:
    raise BaseException("This is a BaseException")
except BaseException as e:
    print(e)
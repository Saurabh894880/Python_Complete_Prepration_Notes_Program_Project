# 2. Exception
# - The Exception class is the base for all non-exit exceptions.
# - You will often catch Exception in general error-handling code when you are not targeting a specific error type.

try:
    raise Exception("This is a generic exception")
except Exception as e:
    print(e)
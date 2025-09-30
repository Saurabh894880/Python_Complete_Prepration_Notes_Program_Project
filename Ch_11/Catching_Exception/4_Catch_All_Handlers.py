# 3. Catch-All Handlers and Their Risks
# Sometimes we may use a catch-all handler to catch any exception,

try :
    res='100'/20

except ArithmeticError :
    print("Airthmetic Problem")
except :
    print("Something went wrong.")


# Output : Something went wrong.

# Explanation:
# - A TypeError occurs because you can’t divide a string by a number.
# - The bare except catches it, but this can make debugging harder since the actual error type is hidden.
# - Use bare except only as a last-resort safety net.
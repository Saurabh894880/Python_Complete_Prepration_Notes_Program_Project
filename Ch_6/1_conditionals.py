# Conditional Statements in Python :

# If, Elif, Else Statements
a = 33
b = 200
if b > a:
    print("b is greater than a")
# Output: b is greater than a

# Elif
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
# Output: a and b are equal
# Else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
# Output: a is greater than b

# Short Hand If
if a > b: print("a is greater than b")  
# Output: a is greater than b

# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")
# Output: B

# And
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
# Output: Both conditions are True
# Or
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
# Output: At least one of the conditions is True
# Nested If

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
# Output:
# Above ten,
# and also above 20!
# The pass Statement
a = 33
b = 200
if b > a:
    pass
# pass is used as a placeholder for future code.
# It allows you to write empty blocks of code without causing syntax errors.
# In this example, since b is greater than a, the if statement is true, but nothing happens because of the pass statement.
# This can be useful when you are working on a code structure and want to implement the logic later.
# Output: (No output, as pass does nothing)

# Theory of Conditional Statements:
# Conditional statements are used to perform different actions based on different conditions.
# In Python, the primary conditional statements are if, elif, and else.

# The if statement is used to test a specific condition. If the condition evaluates to True, the block of code within the if statement is executed.

# The elif (short for "else if") statement allows you to check multiple conditions. If the first condition is False, the program checks the next condition in the elif statement.

# The else statement is used to execute a block of code when none of the previous conditions are True.

# You can also use logical operators like and, or, and not to combine multiple conditions.

# Nested if statements allow you to place an if statement inside another if statement, enabling more complex decision-making.

# Short-hand if and if-else statements provide a more concise way to write simple conditional statements.

# The pass statement is a placeholder that does nothing. It is useful when you need to create a block of code but haven't implemented it yet.

# Conditional statements are fundamental in programming as they allow for decision-making and control flow in the code.
# They enable the program to respond differently based on varying inputs or states.
# Understanding and effectively using conditional statements is crucial for writing efficient and logical code.
# Example of a simple conditional statement:
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# Output: You are eligible to vote.
# In this example, the program checks if the age is 18 or older. If true, it prints that the person is eligible to vote; otherwise, it states they are not eligible.

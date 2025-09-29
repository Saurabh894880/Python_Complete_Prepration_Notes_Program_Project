# type() in python
print(type(5))          # <class 'int'>
print(type(5.0))        # <class 'float'>
print(type("Hello"))    # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>
print(type({1, 2, 3}))  # <class 'set'>
print(type({1: "one", 2: "two"}))  # <class 'dict'>

# Type Casting in Python
# Implicit Type Casting
a = 5       # int
b = 2.0     # float
c = a + b   # int is converted to float
print(c)          # 7.0
print(type(c))    # <class 'float'>

# Explicit Type Casting
x = 5       # int   
y = 2.0     # float
# Converting float to int
z = int(y)  # Explicitly converting float to int
print(z)          # 2
print(type(z))    # <class 'int'>

# Converting int to float
w = float(x)  # Explicitly converting int to float
print(w)          # 5.0

print(type(w))    # <class 'float'>

# Converting int to string
s = str(x)    # Explicitly converting int to string
print(s)          # "5"
print(type(s))    # <class 'str'>



# Data Types in Python
# 1. Numeric
#    - int (integer)
#    - float (floating point)
#    - complex (complex numbers)
# 2. Sequence
#    - list
#    - tuple
#    - range
# 3. Text
#    - str (string)
# 4. Mapping
#    - dict (dictionary)
# 5. Set
#    - set
#    - frozenset
# 6. Boolean
#    - bool
# 7. Binary
#    - bytes
#    - bytearray
#    - memoryview
# Example:
a=5 # a is an integer
b=3.14 # b is a float
c=2+3j # c is a complex number

d=[1, 2, 3] # d is a list
e=(1, 2, 3) # e is a tuple
f=range(5) # f is a range object

g="Hello, World!" # g is a string

h={"name": "Alice", "age": 25} # h is a dictionary

i={1, 2, 3} # i is a set
j=frozenset([1, 2, 3]) # j is a frozenset

k=True # k is a boolean
l=False # l is a boolean

m=b'Hello' # m is a bytes object
n=bytearray(b'Hello') # n is a bytearray
o=memoryview(b'Hello') # o is a memoryview object

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))
print(type(o))
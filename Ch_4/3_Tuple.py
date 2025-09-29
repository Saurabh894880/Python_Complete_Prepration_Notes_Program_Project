# Tuple : Immutable sequence of elements
my_tuple = (1, 2, 3)
print(my_tuple)

# empty tuple
empty_tuple = ()

# single element tuple
single_element_tuple = (1,)
print(single_element_tuple)
# multiple data types
mixed_tuple = (1, "Hello", 3.4, True)
print(mixed_tuple)

#Mutibility : Tuples are immutable that means once created, their elements cannot be changed.
# my_tuple[0] = 10  # This will raise a TypeError

# Accessing elements
print(my_tuple[0])  # First element
print(my_tuple[-1]) # Last element  
print(my_tuple[1:3]) # Slicing
print(my_tuple[::2]) # Slicing with step
print(my_tuple[::-1]) # Reversing a tuple
print(len(my_tuple))  # Length of the tuple
# Tuple unpacking

a, b, c = my_tuple
print(a, b, c)

# Nested tuples

nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple)

# Nested tuple unpacking

x, (y, z), (p, q, r) = nested_tuple
print(x, y, z, p, q, r)


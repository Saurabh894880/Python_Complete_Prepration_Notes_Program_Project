# Tuple Operators in Python
# 1. Concatenation (+): Combines two tuples into one.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3,4, 5, 6)
# 2. Repetition (*): Repeats the elements of a tuple a specified number
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
# 3. Membership (in, not in): Checks if an element exists in a tuple    
is_in_tuple = 2 in tuple1
print(is_in_tuple)  # Output: True
is_not_in_tuple = 5 not in tuple1
print(is_not_in_tuple)  # Output: True
# 4. Indexing ([]): Accesses elements of a tuple by their index.
first_element = tuple1[0]

#Note: these all can be used with lists as well .
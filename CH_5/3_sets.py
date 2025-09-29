# sets : A set is an unordered collection of unique elements.
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating a set from a list (duplicates will be removed)
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set_from_list = set(my_list) 
print(my_set_from_list)  # Output: {1, 2, 3, 4, 5}

#empty set
empty_set = set()
print(empty_set, type(empty_set))  # Output: set() <class 'set'>

#Properties of sets
# 1. Unordered: Sets do not maintain any order for the elements.
# 2. Mutable: You can add or remove elements from a set after it is created.
# 3. Unique elements: Sets automatically remove duplicate elements.
# 4. Dynamic size: Sets can grow and shrink in size as you add or remove elements.
# 5. Heterogeneous: Sets can store elements of different data types, including other sets (as long as they are immutable).
# 6. Iterable: You can iterate over the elements in a set using loops.
# 7. No indexing: Sets do not support indexing or slicing like lists or tuples.
# 8. Set operations: Sets support mathematical set operations like union, intersection, difference, and symmetric difference.       
# 9. Membership testing: You can check if an element is in a set using the 'in' keyword.
# 10. Frozenset: Python also provides a frozenset type, which is an immutable version of a set. Frozensets cannot be modified after creation.
# Example of set operations:
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5}
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3}
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

#Accessing elements in a set:
# Since sets are unordered, you cannot access elements by index. However, you can iterate over the elements:
for element in my_set:
    print(element)

# Adding elements to a set:
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
my_set.add(3)  # Adding a duplicate element (will have no effect)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
# Removing elements from a set:
my_set.remove(4)
print(my_set)  # Output: {1, 2, 3, 5, 6}
my_set.discard(10)  # Removing a non-existent element (will have no effect)
print(my_set)  # Output: {1, 2, 3, 5, 6}
popped_element = my_set.pop()  # Removes and returns an arbitrary element   
print(popped_element)
print(my_set)  # Output: {2, 3, 5, 6} (the actual output may vary)
my_set.clear()  # Removes all elements from the set
print(my_set)  # Output: set()



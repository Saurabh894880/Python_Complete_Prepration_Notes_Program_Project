# All methods of sets in python with syntax, description and examples:
# 1. add(): Adds an element to the set. If the element already exists, it has no effect.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
my_set.add(2)  # Adding a duplicate element (will have no effect)
print(my_set)  # Output: {1, 2, 3, 4}

# 2. clear(): Removes all elements from the set. 
my_set.clear()
print(my_set)  # Output: set()

my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# 3. copy(): Returns a shallow copy of the set.
my_set_copy = my_set.copy()
print(my_set_copy)  # Output: {1, 2, 3, 4}

# Notes: The copy is shallow, meaning that if the set contains nested objects (like lists or other sets), the references to those objects are copied, not the objects themselves.
# that means changes made to nested objects in the copied set will affect the original set and vice versa.
# if use clear method on copy it will not affect original set beacause clear method removes all items from the set but does not affect the reference of the original set.   

my_set_copy.clear()
print(my_set)  # Output: {1, 2, 3, 4}

# 4. difference(): Returns a new set containing elements that are in the set but not in the specified set(s).
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}

# 5. difference_update(): Removes elements found in the specified set(s) from the original set.
set_a.difference_update(set_b)
print(set_a)  # Output: {1, 2}

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}

# 6. discard(): Removes a specified element from the set. If the element is not found, it has no effect.
set_a.discard(3)
print(set_a)  # Output: {1, 2, 4}
set_a.discard(10)  # Removing a non-existent element (will have no effect)
print(set_a)  # Output: {1, 2, 4}

# 7. intersection(): Returns a new set containing elements that are common to the set and the specified set(s).
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3, 4}
# 8. intersection_update(): Updates the original set to keep only elements found in it and the specified set(s).
set_a.intersection_update(set_b)
print(set_a)  # Output: {3, 4}
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}
# 9. isdisjoint(): Returns True if the set has no elements in common with the specified set(s), otherwise False.
set_c = {6, 7}
is_disjoint = set_a.isdisjoint(set_c)
print(is_disjoint)  # Output: True
is_disjoint = set_a.isdisjoint(set_b)
print(is_disjoint)  # Output: False

# 10. issubset(): Returns True if all elements of the set are in the specified set, otherwise False.
set_d = {3, 4}
is_subset = set_d.issubset(set_a)
print(is_subset)  # Output: True
is_subset = set_b.issubset(set_a)
print(is_subset)  # Output: False

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}

# 11. issuperset(): Returns True if all elements of the specified set are in the set, otherwise False.
is_superset = set_a.issuperset(set_d)
print(is_superset)  # Output: True

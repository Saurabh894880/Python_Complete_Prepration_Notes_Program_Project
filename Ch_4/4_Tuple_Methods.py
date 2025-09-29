# All tuple methods with syntax , description and example

# Tuple Methods in Python 
# 1. count(x): Returns the number of times x appears in the tuple.
my_tuple = (1, 2, 3, 2, 4, 2)
count_of_2 = my_tuple.count(2)
print(count_of_2)
# Output: 3
# 2. index(x[, start[, end]]): Returns the index of the first item whose value is x.
index_of_3 = my_tuple.index(3)  
print(index_of_3)
# Output: 2
# 3. len(): Returns the number of items in the tuple.
length_of_tuple = len(my_tuple)
print(length_of_tuple)
# Output: 6
# 4. sum(): Returns the sum of all items in the tuple.
sum_of_tuple = sum((1, 2, 3, 4, 5))
print(sum_of_tuple)
# Output: 15
# 5. min(): Returns the smallest item in the tuple.
min_of_tuple = min(my_tuple)
print(min_of_tuple)
# Output: 1
# 6. max(): Returns the largest item in the tuple.
max_of_tuple = max(my_tuple)
print(max_of_tuple)
# Output: 4
# 7. sorted(iterable, key=None, reverse=False): Returns a new sorted list from the elements of the tuple.
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)
# Output: [1, 2, 2, 2, 3, 4]
# 8. any(): Returns True if any element of the tuple is true.
any_true = any((0, "", None, 5))
print(any_true)
# Output: True
# 9. all(): Returns True if all elements of the tuple are true.
all_true = all((1, 2, 3))
print(all_true)
# Output: True
# Note: Tuples are immutable, so they do not have methods that modify the tuple in place like lists do.
# However, you can use functions that return new values based on the tuple's contents.
# Example of using these methods
example_tuple = (10, 20, 30, 20, 40)
print("Count of 20:", example_tuple.count(20))  # Output: 2
print("Index of 30:", example_tuple.index(30))  # Output: 2
print("Length:", len(example_tuple))  # Output: 5
print("Sum:", sum(example_tuple))  # Output: 120
print("Min:", min(example_tuple))  # Output: 10
print("Max:", max(example_tuple))  # Output: 40
print("Sorted:", sorted(example_tuple))  # Output: [10, 20, 20, 30, 40]
print("Any true:", any(example_tuple))  # Output: True
print("All true:", all(example_tuple))  # Output: True
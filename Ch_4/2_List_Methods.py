
# ALL methods with synatx and description and example

# List Methods in Python
# 1. append(x): Adds an item x to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4
# 2. extend(iterable): Extends the list by appending elements from the iterable.
my_list.extend([5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
# 3. insert(i, x): Inserts an item x at a given position i.
my_list.insert(0, 0)
print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6]
# 4. remove(x): Removes the first item from the list whose value is x.
my_list.remove(3)
print(my_list)  # Output: [0, 1, 2, 4, 5, 6]
# 5. pop([i]): Removes and returns the item at the given position i.
popped_item = my_list.pop()
print(popped_item)  # Output: 6
print(my_list)  # Output: [0, 1, 2, 4, 5]
# 6. clear(): Removes all items from the list.
my_list.clear()
print(my_list)  # Output: []
# 7. index(x[, start[, end]]): Returns the index of the first item
my_list = [1, 2, 3, 4, 5]
index_of_3 = my_list.index(3)
print(index_of_3)  # Output: 2
# 8. count(x): Returns the number of times x appears in the list.
count_of_2 = my_list.count(2)
print(count_of_2)  # Output: 1
# 9. sort(key=None, reverse=False): Sorts the items of the list in place.
my_list.sort(reverse=True)
print(my_list)  # Output: [5, 4, 3, 2, 1]   
# 10. reverse(): Reverses the elements of the list in place.
my_list.reverse()
print(my_list)  # Output: [1, 2, 3, 4, 5]
# 11. copy(): Returns a shallow copy of the list.
copied_list = my_list.copy()
print(copied_list)  # Output: [1, 2, 3, 4, 5]
# 12. len(): Returns the number of items in the list.
length_of_list = len(my_list)
print(length_of_list)  # Output: 5
# 13. sum(): Returns the sum of all items in the list.
sum_of_list = sum(my_list)
print(sum_of_list)  # Output: 15
# 14. min(): Returns the smallest item in the list.
min_of_list = min(my_list)
print(min_of_list)  # Output: 1
# 15. max(): Returns the largest item in the list.
max_of_list = max(my_list)
print(max_of_list)  # Output: 5
# 16. sorted(iterable, key=None, reverse=False): Returns a new sorted list
sorted_list = sorted(my_list, reverse=True)
print(sorted_list)  # Output: [5, 4, 3, 2, 1]
# 17. any(): Returns True if any element of the list is true.
any_true = any(my_list)
print(any_true)  # Output: True
# 18. all(): Returns True if all elements of the list are true.
all_true = all(my_list)
print(all_true)  # Output: False
# 19. enumerate(iterable, start=0): Returns an enumerate object.
for index, value in enumerate(my_list):
    print(index, value) 
# Output:
# 0 1
# 1 2
# 2 3       
# 3 4
# 4 5
# 20. zip(*iterables): Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# 21. list(): Converts an iterable (like a string or tuple) to a list.
string = "hello"
list_from_string = list(string)
print(list_from_string)  # Output: ['h', 'e', 'l', 'l', 'o']
# 22. slice(): Returns a slice object representing the set of indices specified by range(start, stop, step).
slice_obj = slice(1, 5, 2)
sliced_list = my_list[slice_obj]    
print(sliced_list)  # Output: [2, 4]
# 23. filter(function, iterable): Constructs an iterator from those elements of iterable for which
filtered = filter(lambda x: x % 2 == 0, my_list)
print(list(filtered))  # Output: [2, 4]
# the function returns true.
# 24. map(function, iterable): Applies function to every item of iterable and returns a list of the results.
mapped = map(lambda x: x * 2, my_list)
print(list(mapped))  # Output: [2, 4, 6, 8, 10]  # Output: [1, 2, 3, 4, 5]
# 25. reduce(function, iterable): Applies function of two arguments cumulatively to the items of iterable, from left to right, to reduce the iterable to a single value.
from functools import reduce
reduced = reduce(lambda x, y: x + y, my_list)
print(reduced)  # Output: 15
# Output: [1, 2, 3, 4, 5]
# 26. chr(): Returns the string representing a character whose Unicode code point is the integer i.
char_list = [chr(i) for i in range(97, 102)]
print(char_list)  # Output: ['a', 'b', 'c', 'd', 'e']
# 27. ord(): Returns an integer representing the Unicode code point of the given Unicode character
ord_list = [ord(c) for c in 'abcde']
print(ord_list)  # Output: [97, 98, 99, 100, 101]
# 28. format(): Returns a formatted version of the given value controlled by the format specifier.
formatted_list = ["{:.2f}".format(x) for x in [1.234, 2.345, 3.456]]
print(formatted_list)  # Output: ['1.23', '2.35', '3.46']
# 29. repr(): Returns a string containing a printable representation of an object.
repr_list = [repr(x) for x in my_list]
print(repr_list)  # Output: ['1', '2', '3', '4', '5']
# 30. str(): Returns a string version of an object.
str_list = [str(x) for x in my_list]
print(str_list)  # Output: ['1', '2', '3', '4', '5']
# 31. type(): Returns the type of an object.
type_list = [type(x) for x in my_list]
print(type_list)  # Output: [<class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>]
# 32. id(): Returns the identity of an object.
id_list = [id(x) for x in my_list]
print(id_list)  # Output: [140703303123456, 140703303123488, 140703303123520, 140703303123552, 140703303123584]
# 33. help(): Invokes the built-in help system. This is not typically used in list operations but can be used to get help on list methods.
help_list = help(list)  
print(help_list)  # Output: Help on class list in module builtins:
# 34. dir(): Returns a list of the attributes and methods of any object (functions, modules, etc.)
dir_list = dir(my_list)
print(dir_list)  # Output: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
#'__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
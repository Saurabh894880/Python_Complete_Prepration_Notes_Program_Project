#All dictionary methods with syntax , description and examples:
# 1. clear(): Removes all items from the dictionary.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
my_dict.clear() 
print(my_dict)  # Output: {}

# 2. copy(): Returns a shallow copy of the dictionary.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
my_dict_copy.clear()
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
#Notes:  The copy is shallow, meaning that if the dictionary contains nested objects (like lists or other dictionaries), the references to those objects are copied, not the objects themselves.
# that means changes made to nested objects in the copied dictionary will affect the original dictionary and vice versa.
# if use clear method on copy it will not affect original dictionary beacause clear method removes all items from the dictionary but does not affect the reference of the original dictionary.

# 3. fromkeys(): Creates a new dictionary with keys from an iterable and values set to a specified value.
keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# 4. get(): Returns the value for a specified key. If the key is not found, it returns a default value (None if not specified).
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("country", "USA"))  # Output: USA

# 5. items(): Returns a view object that displays a list of a dictionary's key-value tuple pairs.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
for key, value in items:
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 30
# city: New York

# 6. keys(): Returns a view object that displays a list of all the keys in the dictionary.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city'])
for key in keys:
    print(key)  
# Output:
# name  
# age
# city

# 7. pop(): Removes the item with the specified key and returns its value. If the key is not found, it raises a KeyError.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
age = my_dict.pop("age")
print(age)  # Output: 30
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}
# age = my_dict.pop("country")  # Raises KeyError because "country" key does not exist

# 8. popitem(): Removes and returns the last inserted key-value pair as a tuple. Raises a KeyError if the dictionary is empty.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
last_item = my_dict.popitem()
print(last_item)  # Output: ('city', 'New York')
print(my_dict)  # Output: {'name': 'Alice', 'age': 30}

# 9. setdefault(): Returns the value of a specified key. If the key does not exist, it inserts the key with a specified default value.
my_dict = {"name": "Alice", "age": 30}  
city = my_dict.setdefault("city", "New York")
print(city)  # Output: New York
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
country = my_dict.setdefault("country")
print(country)  # Output: None
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': None}

# 10. update(): Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.
my_dict = {"name": "Alice", "age": 30}
update_dict = {"age": 31, "city": "New York"}
my_dict.update(update_dict)
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
#if both have different keys then it will add new key-value pair to the original dictionary
# if both have same keys then it will update the value of the key in the original dictionary
my_dict.update([("country", "USA"), ("profession", "Engineer")])
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA', 'profession': 'Engineer'}

# 11. values(): Returns a view object that displays a list of all the values in the dictionary.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
values = my_dict.values()   
print(values)  # Output: dict_values(['Alice', 30, 'New York'])
for value in values:
    print(value)
# Output:
# Alice
# 30
# New York

# Note: The view objects returned by items(), keys(), and values() are dynamic and reflect changes made to the dictionary.

# Example:
my_dict = {"name": "Alice", "age": 30}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age'])
my_dict["city"] = "New York"
print(keys)  # Output: dict_keys(['name', 'age', 'city'])
# The keys view object automatically updates to reflect the addition of the "city" key.
# Similarly, items() and values() view objects will also reflect changes made to the dictionary.
# These methods provide powerful ways to manipulate and interact with dictionaries in Python.

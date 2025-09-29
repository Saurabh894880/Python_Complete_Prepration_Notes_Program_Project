# Dictionary in Python : 
# A dictionary is a collection of key-value pairs. Each key is unique and is used to access the corresponding value.
# Dictionaries are mutable, meaning you can change their content without changing their identity.
# Dictionaries are defined using curly braces {} with key-value pairs separated by commas.
# Example of a dictionary:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict,type(my_dict))

# Accessing values in a dictionary:
print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 30
# Adding or updating key-value pairs:
my_dict["email"] = "alice@example.com"
my_dict["age"] = 31  # Update age
print(my_dict)  

# Removing key-value pairs:
del my_dict["city"]
print(my_dict)
age = my_dict.pop("age")
print(age)  # Output: 31
print(my_dict)

#properties of dictionary
# 1. Unordered: Dictionaries do not maintain any order for the key-value pairs.
# 2. Mutable: You can change, add, or remove key-value pairs after the dictionary is created.
# 3. Keys must be unique: Each key in a dictionary must be unique. If
# you try to use a duplicate key, the last value will overwrite the previous one.
# 4. Keys must be immutable: Keys must be of an immutable data type, such
# as strings, numbers, or tuples. Lists or other dictionaries cannot be used as keys.
# 5. Dynamic size: Dictionaries can grow and shrink in size as you add or remove key-value pairs.
# 6. Heterogeneous: Dictionaries can store values of different data types, including other dictionaries.
# 7. Iterable: You can iterate over the keys, values, or key-value pairs in a dictionary using loops.


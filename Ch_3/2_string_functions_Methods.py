# All string functions and methods in python
my_string = "Hello World"
print(my_string)
print(type(my_string)) #<class 'str'> #str is the class for string
print(dir(my_string)) # lists all string methods

# len function
print(len(my_string)) #11 returns the length of the string

# string methods
# 1. my_string.lower() - converts all characters to lowercase
# 2. my_string.upper() - converts all characters to uppercase
# 3. my_string.split() - splits the string into a list of words
# 4. my_string.replace(old, new) - replaces occurrences of old with new
# 5. my_string.strip() - removes leading and trailing whitespace
# 6. my_string.find(sub) - returns the lowest index of the substring sub
# 7. my_string.count(sub) - returns the number of occurrences of substring sub
# 8. my_string.startswith(sub) - returns True if the string starts with sub
# 9. my_string.endswith(sub) - returns True if the string ends with sub
# 10. my_string.isalpha() - returns True if all characters are alphabetic
# 11. my_string.isdigit() - returns True if all characters are digits
# 12. my_string.isalnum() - returns True if all characters are alphanumeric
# 13. my_string.join(iterable) - joins elements of iterable with the string as separator
# 14. my_string.capitalize() - capitalizes the first character of the string
# 15. my_string.title() - capitalizes the first character of each word in the string
# 16. my_string.center(width) - centers the string in a field of given width
# 17. my_string.ljust(width) - left justifies the string in a field of given width
# 18. my_string.rjust(width) - right justifies the string in a field
# 19. my_string.zfill(width) - pads the string with zeros on the left to fill the width
# 20. my_string.partition(sep) - splits the string at the first occurrence of sep
# 21. my_string.rpartition(sep) - splits the string at the last occurrence of sep
# 22. my_string.splitlines() - splits the string at line breaks
# 23. my_string.swapcase() - swaps the case of all characters in the string
# 24. my_string.encode(encoding) - encodes the string using the specified encoding
# 25. my_string.format(*args, **kwargs) - formats the string using the given arguments
# 26. my_string.format_map(mapping) - formats the string using a mapping
# 27. my_string.removeprefix(prefix) - removes the specified prefix from the
# 28. my_string.removesuffix(suffix) - removes the specified suffix from the string
# 29. my_string.translate(table) - translates the string using the given translation table
# 30. my_string.maketrans(x, y, z) - creates a translation table for use with translate()
# 31. my_string.islower() - returns True if all cased characters are lowercase
# 32. my_string.isupper() - returns True if all cased characters are uppercase
# 33. my_string.isspace() - returns True if all characters are whitespace
# 34. my_string.isprintable() - returns True if all characters are printable
# 35. my_string.isidentifier() - returns True if the string is a valid identifier
# 36. my_string.encode(encoding='utf-8', errors='strict') - encodes the string using the specified encoding
# 37. my_string.expandtabs(tabsize=8) - replaces tabs with spaces
# 38. my_string.index(sub, start=0, end=len(my_string)) - returns the lowest index of the substring sub
# 39. my_string.rindex(sub, start=0, end=len(my_string)) - returns the highest index of the substring sub
# 40. my_string.lstrip() - removes leading whitespace
# 41. my_string.rstrip() - removes trailing whitespace
# 42. my_string.partition(sep) - splits the string at the first occurrence of sep
# 43. my_string.rpartition(sep) - splits the string at the last occurrence of sep
# 44. my_string.split(sep=None, maxsplit=-1) - splits the

#Examples of string methods
print(my_string.lower()) #hello world
print(my_string.upper()) #HELLO WORLD   
print(my_string.split()) #['Hello', 'World']
print(my_string.replace('World', 'Everyone')) #Hello Everyone   
print(my_string.strip()) #Hello World (removes leading and trailing whitespace)
print(my_string.find('o')) #4 (index of first occurrence of 'o')
print(my_string.count('o')) #2 (number of occurrences of 'o')
print(my_string.startswith('Hello')) #True
print(my_string.endswith('World')) #True string at each occurrence of sep

print(my_string.isalpha()) #False (contains space)
print(my_string.isdigit()) #False       
print(my_string.isalnum()) #False (contains space)
print('-'.join(['Hello', 'World'])) #Hello-World    
print(my_string.capitalize()) #Hello world
print(my_string.title()) #Hello World
print(my_string.center(20)) #    Hello World    
print(my_string.ljust(20)) #Hello World
print(my_string.rjust(20)) #       Hello World
print(my_string.zfill(20)) #0000000000Hello World


print(my_string.partition(' ')) #('Hello', ' ', 'World')
print(my_string.rpartition(' ')) #('Hello', ' ', 'World')

#Escape sequences in strings
print("Hello\nWorld") #Hello (new line) World
print("Hello\tWorld") #Hello    World (tab space)
print("Hello\\World") #Hello\World (backslash)
print('He said, "Hello World"') #He said, "Hello World" (double quotes inside single quotes)
print("It's a beautiful day") #It's a beautiful day (single quote inside double quotes)
print("Hello\rWorld") #World (carriage return)
print("Hello\bWorld") #HellWorld (backspace)
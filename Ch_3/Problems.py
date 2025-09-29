#Display a user entered name 
name = input("Enter your name: ")
print("Hello " + name)
print(f"Hello {name}") #using f-string #f-string is faster than concatenation

# find the index of double spaces in a string
my_string = "Hello  World"
index = my_string.find("  ")
print(f"Index of double spaces: {index}")

#Replace the double spaces with single space
new_string = my_string.replace("  ", " ")
print(f"String after replacing double spaces: '{new_string}'") 

# strings are immutable - cannot change a character in a string
# my_string[0] = 'h' #this will give an error
# print(my_string)  

#format a string to display a name and age
name = "Alice"
age = 30
print("My name is {} and I am {} years old".format(name, age))
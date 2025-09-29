#Wap to insert a dictionary in which key is a hindi word and value is its english meaning.
hindi_english_dict = {
    "Namaste": "Hello",
    "Pustak": "Book",
    "Vidhyalay": "School",
    "Khushi": "Happiness",
    "Parivar": "Family"
}
print(hindi_english_dict)

#Wap to insert 8 numbers from user and display the unique numbers.
user_numbers = set()
for i in range(8):
    number = int(input("Enter a number: "))
    user_numbers.add(number)
print(user_numbers)

# can we have a set with 18(int) and "18"(str) as elements? if yes then write a code to prove it.
my_set = {18, "18"}
print(my_set)  # Output: {18, '18'}
print(type(my_set))  # Output: <class 'set'>

# what wil be the length of above set?
print(len(my_set))  # Output: 2

#Create an empty dictionary . Allow 4 friends to enter their favorite language as value and their name as key to the dictionary. Assume that the names are unique.
favorite_languages = {}
for i in range(4):
    name = input("Enter your name: ")
    language = input("Enter your favorite language: ")
    favorite_languages[name] = language

print(favorite_languages)


#If two students have the same names, how will you manage that using dictionary?
# If two students have the same name, we can manage that by using a list to store multiple languages for the same name.
favorite_languages = {}
for i in range(4):
    name = input("Enter your name: ")
    language = input("Enter your favorite language: ")
    if name in favorite_languages:
        favorite_languages[name].append(language)
    else:
        favorite_languages[name] = [language]

# can you change the values inside a list which is present in a set?
# No, you cannot change the values inside a list which is present in a set because lists are mutable and sets require their elements to be immutable (hashable).
# Example to prove it:  
my_set = {1, 2, (3, 4)}  # A set with integers and a tuple (which is immutable)
print(my_set)  # Output: {1, 2, (3, 4)}
# my_set.add([5, 6])  # Trying to add a list (which is mutable) will raise a TypeError
# print(my_set)  # This line will not be executed due to the error above   

s = set()
s.add(1)
s.add(1.0)
s.add('1')
print(len(s))
print(s)
#Note: 1 and 1.0 are considered the same in a set because they are equal in value and have the same hash value. However, '1' is a string and is distinct from both 1 and 1.0. Therefore, the set will contain two unique elements: {1, '1'}. The length of the set will be 2.
#Output: 2
#Output: {1, '1'}
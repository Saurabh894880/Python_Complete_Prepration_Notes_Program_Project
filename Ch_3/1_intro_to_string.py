#string : a sequence of characters
my_string = "Hello World"
print(my_string)

#accessing characters in a string
print(my_string[0]) #H
print(my_string[1]) #e
print(my_string[2]) #l
print(my_string[3]) #l
print(my_string[4]) #o
print(my_string[5]) # (space)
print(my_string[6]) #W
print(my_string[7]) #o
print(my_string[8]) #r
print(my_string[9]) #l
print(my_string[10]) #d

#string slicing
print(my_string[0:5]) #Hello
print(my_string[6:11]) #World
print(my_string[:5]) #Hello

print(my_string[6:]) #World
print(my_string[:]) #Hello World
print(my_string[::2]) #HloWrd
print(my_string[1::2]) #el ol  runs every second character

# Negative indexing slicing
print(my_string[-1]) #d
print(my_string[-2]) #l
print(my_string[-3]) #r
print(my_string[-4]) #o
print(my_string[-5]) #W
print(my_string[-6]) # (space)
print(my_string[-7]) #o
print(my_string[-8]) #l
print(my_string[-9]) #l
print(my_string[-10]) #e
print(my_string[-11]) #H

print(my_string[-5:]) #World
print(my_string[:-6]) #Hello
print(my_string[-11:-6]) #Hello
print(my_string[-6:]) # World
print(my_string[-11:]) #Hello World
print(my_string[-11:-1]) #Hello Worl
print(my_string[::-1]) #dlroW olleH reverses the string 


#string methods
print(my_string.lower()) #hello world converts to lowercase
print(my_string.upper()) #HELLO WORLD converts to uppercase
print(my_string.split()) #['Hello', 'World'] splits the string into a list
print(my_string.split('o')) #['Hell', ' W', 'rld'] splits the string at each 'o'
print(my_string.replace('World', 'Everyone')) #Hello Everyone replaces 'World' with 'Everyone'  
print('Hello' in my_string) #True checks if 'Hello' is in the string
print('hello' in my_string) #False checks if 'hello' is in the string
print('World' not in my_string) #False checks if 'World' is not in the string
print('hello' not in my_string) #True checks if 'hello' is not in

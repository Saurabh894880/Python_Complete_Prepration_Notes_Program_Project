# List : A collection of items
my_list1 = [1, 2, 3, 4, 5]
print(my_list1)

#multiple data types
my_list2 = [1, "Hello", 3.4, True]
print(my_list2)

#Mutable
my_list3 = [1, 2, 3]    
my_list3[0] = 10
print(my_list3)

# Accessing elements
print(my_list1[0])  # First element
print(my_list1[-1]) # Last element  
print(my_list1[1:4]) # Slicing
print(my_list1[::2]) # Slicing with step
print(my_list1[::-1]) # Reversing a list
print(len(my_list1))  # Length of the list
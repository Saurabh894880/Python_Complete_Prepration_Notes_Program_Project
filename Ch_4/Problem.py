# WAP to enter the 7 fruits names in a list and display.
fruits=["apple","banana","cherry","date","elderberry","fig","grape"]
print("Fruits: ",fruits)

# WAP to enter the 5 subjects marks in a list and display them in a sorted order.
marks=[50,60,90,100,99]
marks.sort()
print("Sorted marks: ",marks)

# Check tuple contains a specific value.
my_tuple = (1, 2, 3, 4, 5)
#my_tuple[0]=10
print(my_tuple)

#WAP to find the sum of all items in a tuple.
my_tuple = (1, 2, 3, 4, 5)
sum_of_tuple = sum(my_tuple)
print("Sum of tuple items: ",sum_of_tuple)

#Wap to find the frequency of a number in tuple and list
my_list = [1, 2, 3, 2, 4, 2]
count_of_2_list = my_list.count(2)
my_tuple = (1, 2, 3, 2, 4, 2)
count_of_2_tuple = my_tuple.count(2)
print("Count of 2 in list: ",count_of_2_list)
print("Count of 2 in tuple: ",count_of_2_tuple)
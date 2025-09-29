#8. Write a python function to print multiplication table of a given number.
def printTable(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")

num=int(input("Enter the number : "))
printTable(num)
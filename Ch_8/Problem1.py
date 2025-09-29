#1. Write a program using functions to find greatest of three numbers.

def findGreatest(a,b,c):
    if(a>b and a>b) :
        return a
    elif b>a and b>c :
        return b
    else :
        return c

a= int(input("Enter first number : "))
b= int(input("Enter first number : "))
c= int(input("Enter first number : "))

print("The greatest number is : ",findGreatest(a,b,c))


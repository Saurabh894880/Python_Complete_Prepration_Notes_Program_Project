#4. Write a recursive function to calculate the sum of first n natural numbers.
def sum(n):
    if n==1 :
        return 1
    else :
        return n+sum(n-1)

num=int(input("Enter the number of natural numbers : "))
print(f"Sum of {num} natural number is : {sum(num)}")
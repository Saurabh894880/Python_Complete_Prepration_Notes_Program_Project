'''
5. Write a python function to print first n lines of the following pattern:

   ```
   ***
   **
   *
   ```

   – for n = 3
'''

def pattern(n):
    for i in range(n):
        print("*"*(n-i))

n=int(input("Enter the number of rows : "))
pattern(n)
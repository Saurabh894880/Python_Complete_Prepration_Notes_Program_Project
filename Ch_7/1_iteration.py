# Iteration : Iteration can be defined as the process of repeating a set of instructions
# until a specific condition is met. In Python, iteration is commonly achieved using loops,
# such as for loops and while loops.    
# Example of Iteration using a for loop
for i in range(5):
    print("Iteration number:", i)
# Example of Iteration using a while loop
count = 0   
while count < 5:
    print("Count is:", count)
    count += 1
# Example of Iteration using a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Example of Iteration using a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
# Example of Iteration using a string
message = "Hello"
for char in message:
    print("Character:", char)
# Example of Iteration using a set
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print("Unique number:", number)
# Example of Iteration using a tuple
coordinates = (10, 20)
for coord in coordinates:
    print("Coordinate:", coord)

#Break Statement : The break statement in Python is used to exit a loop prematurely when a certain condition is met.
# When the break statement is encountered inside a loop, the loop is immediately terminated,
# and the program continues executing the code that follows the loop.
# Example of using break statement in a for loop
for i in range(10):
    if i == 5:
        break
    print("Current number:", i)
# Example of using break statement in a while loop
count = 0
while count < 10:
    if count == 5:
        break
    print("Count is:", count)
    count += 1

# Continue Statement : The continue statement in Python is used to skip the current iteration of a loop and move on to the next iteration.
# When the continue statement is encountered inside a loop, the remaining code in the current iteration is skipped,
# and the loop proceeds to the next iteration.
# Example of using continue statement in a for loop
for i in range(10):
    if i == 5:
        continue
    print("Current number:", i)
# Example of using continue statement in a while loop
count = 0
while count < 10:
    count += 1
    if count == 5:
        continue
    print("Count is:", count)

# Nested Loops : Nested loops are loops that exist within another loop. In Python, you can create nested loops by placing one loop inside the body of another loop.
# The inner loop will complete all its iterations for each iteration of the outer loop.
# Example of nested loops using for loops
for i in range(3):  
    for j in range(2):
        print(f"Outer loop i={i}, Inner loop j={j}")
# Example of nested loops using a for loop and a while loop
for i in range(3):
    count = 0
    while count < 2:
        print(f"Outer loop i={i}, Inner loop count={count}")
        count += 1
# Example of nested loops using while loops
outer_count = 0 
while outer_count < 3:
    inner_count = 0
    while inner_count < 2:
        print(f"Outer count={outer_count}, Inner count={inner_count}")
        inner_count += 1
    outer_count += 1

#3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files.
#  Place these files in a folder for a 13 – year old.
import os
for i in range(2, 21):
    file_path = os.path.join("Tables", f"Multiplication_table_{i}.txt")
    with open(file_path,"w") as f:
        f.write(f"Multiplication table of {i}\n")
        for j in range(1,11) :
            f.write(f"{i} * {j} = {i*j}\n")

# 7. Write a program to find out the line number where python is present from ques 6.
with open('log.txt','r') as f :
    lines=f.readlines()

i=1
for line in lines :
    if 'python' in line.lower():
        print(f"Python is present in line {i}")
        break
    i+=1
else:
    print(f"Python is not present in log file")
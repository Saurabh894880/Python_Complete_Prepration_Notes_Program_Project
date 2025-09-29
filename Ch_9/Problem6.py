# 6. Write a program to mine a log file and find out whether it contains ‘python’.
with open('log.txt','r') as f:
    file_content = f.read()

if 'python' in file_content.lower():
    print('The log file contains the word "python".')
else :
    print('The log file does not contain the word "python".')
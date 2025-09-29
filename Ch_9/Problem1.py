#1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
with open('poems.txt','r') as f:
    file_content=f.read()


if 'twinkle' in file_content:
    print('The text contains the word "twinkle".')
else : 
    print('The text does not contain the word "twinkle".')
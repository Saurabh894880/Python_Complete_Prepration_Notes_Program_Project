# 4. A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.
with open('text_file.txt', 'r') as f:
    data = f.read()
data = data.replace('Donkey', '#####')
with open('text_file.txt', 'w') as f:
    f.write(data)


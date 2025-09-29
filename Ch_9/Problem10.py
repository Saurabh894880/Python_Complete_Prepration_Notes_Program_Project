# 10. Write a program to wipe out the content of a file using python.
def wipe_file(file_path):
    with open(file_path,'w') as f:
        f.write('')

wipe_file('text_file.txt')
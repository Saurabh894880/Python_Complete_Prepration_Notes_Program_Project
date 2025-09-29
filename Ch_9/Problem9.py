#9. Write a program to find out whether a file is identical & matches the content of another file.
def compare_files(file1,file2):
    with open(file1,'r') as f1, open(file2,'r') as f2:
        if f1.read()== f2.read():
            return True
        else :
            return False

f=compare_files('this.txt','copy_this.txt')
if f:
    print("The files are identical and match the content of each other.")
else:
    print("The files are not identical or do not match the content of each other.")
# 8. Write a program to make a copy of a text file “this.txt”
with open('this.txt','w') as f:
    content='i am your friend. \n'
    f.write(content)

def copy_file(src,dest):
    with open(src,'r') as f:
        content=f.read()
        with open(dest,'w') as f:
            f.write(content)

copy_file('this.txt','copy_this.txt')
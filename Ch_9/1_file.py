f = open("data.txt", "w") #opening the file in write mode
f.write("This is a new file.") #writing data to the file
f.close() #closing the file

f=open("data.txt", "r") #opening the file in read mode
file_content = f.read() #reading data from the file
f.close() #closing the file

# print(file_content) #printing the content of the file

f=open("data.txt", "a") #opening the file in append mode
f.write("\nThis is added data.") #writing data to the file at the end
f.close() #closing the file

f=open("data.txt","r") #opening the file in read mode again
file_content1=f.read() #reading data from the file as a string

f.seek(0) #resetting the file pointer to the start
file_content2=f.readline() #reading the next line from the file as a string

f.seek(0) #resetting the file pointer to the start
file_content3=f.readlines() #reading all lines from the file as a list
f.close() #closing the file

print(file_content1)
print(file_content2)
print(file_content3)
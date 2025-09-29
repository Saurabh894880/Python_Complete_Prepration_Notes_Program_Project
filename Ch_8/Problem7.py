#7. Write a python function to remove a given word from a list and strip it at the same time.
def removeWord(list,word) :
    word=word.strip()
    if word in list :
        list.remove(word)
        print(f"{word} is removed successfully")
    else :
        print(f"{word } is not present in list ")
list=['Ram','Mohan','sita','raju']
word=input("Enter the word to remove from list : ")
print("Original list :",list)
removeWord(list,word)

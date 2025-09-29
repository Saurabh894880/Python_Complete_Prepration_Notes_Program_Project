#WAp to check whether a given name is present in a list or not.
name_list = ["Alice", "Bob", "Charlie", "David"]
name = input("Enter a name to check: ")
if name in name_list:
    print(f"{name} is present in the list.")
else:
    print(f"{name} is not present in the list.")
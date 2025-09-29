# 11. Write a python program to rename a file to “renamed_by_ python.txt.
import os
def rename_file(old_file_name, new_file_name):
    try:
        os.rename(old_file_name, new_file_name)
        print(f"File '{old_file_name}' renamed to '{new_file_name}'.")
    except FileNotFoundError:
        print(f"File '{old_file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to rename '{old_file_name}'.")

rename_file('text_file.txt','ranmed_by_python.txt')
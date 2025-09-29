# 5. Repeat program 4 for a list of such words to be censored.

# List of words to censor
censored_words = ["Donkey", "stupid", "lazy", "fool"]

# Read the original file
with open('text_file1.txt', 'r') as f:
    data = f.read()

# Replace each word in the list with '#####'
for word in censored_words:
    data = data.replace(word, '#'*len(word))

# Write the updated content back to the same file
with open('text_file1.txt', 'w') as f:
    f.write(data)

print("Censored words replaced successfully!")

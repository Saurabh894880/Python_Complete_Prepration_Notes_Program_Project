# 2. The game() function in a program lets a user play a game and returns the score as an integer. 
# You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score.
#  You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import random

def game():
    return random.randint(1, 100)

current_score = game()

# Open the file in read+write mode without truncating
try:
    with open('Hi-score.txt', 'r') as f:
        file_content = f.read().strip()  # Read the previous hi-score
        hi_score = int(file_content) if file_content else 0
except FileNotFoundError:
    hi_score = 0  # If the file doesn't exist, hi-score is 0

# Update hi-score if current_score is greater
if current_score > hi_score:
    hi_score = current_score
    with open('Hi-score.txt', 'w') as f:
        f.write(str(hi_score))

print(f"Current Score: {current_score}")
print(f"Hi-Score: {hi_score}")

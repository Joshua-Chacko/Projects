# Randomly selects a secret word from a list of secret words. import the random library
# Grab the word from a text file
# Create a counter that calculates the total # of lives - 1 per mistakes
# Given the # of characters in the word + 2 lives
import random, string

# Open the text file "randomFile.txt"
# From the file grab a random word 
# Return the word 
def openFile() -> str:
    words = []  # Store all words from the file
    with open('randomFile.txt', 'r') as file:
        for line in file:  # Use 'line' instead of 'strWord' for clarity
            words.extend(line.split())  # Add all words from each line to the list
    if words:  # Ensure the list is not empty before choosing a word
        return random.choice(words)
    else:
        return None  # Handle empty file case


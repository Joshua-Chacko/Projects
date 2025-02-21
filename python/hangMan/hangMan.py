import random
from token import STRING



# The random word from a list of words in a file
def openFile():
    try:
        with open("randomFile.txt", 'r') as file:
            words = file.read().splitlines()
            if words:
                return random.choice(words)
            else:
                return ""
    except FileNotFoundError:
        return ""

# The wrong choices in word
def answerIsWrong(answer, word):
    

# The right choice in a word 



print("=========================")
print("   WELCOME TO HANGMAN    ")
print("=========================")


choice = input("Do you wish to play the Game (Y|N): ")
if choice.lower() == "y":
    word = str(openFile())
    print(f"The Word contains {len(word) * "_"}")

    answer = " " # start with an empty string to start the while loop
    counter = 1 
    while answer is not word: # 
        answer = input(f"Your Guess {counter}: ")
        counter += 1
        if answer is not word:
            answerIsWrong(answer, word)
            print("")
            continue
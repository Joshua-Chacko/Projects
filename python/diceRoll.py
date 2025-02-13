import random

def randomDice():
    value = random.randint(1, 6)
    return value

print("=== Welcome to Dice Roll ===")
while True:
    pick = input("Do you wish to roll the dice. (Y|N): \n")
    if pick.lower() == "y":
        print(randomDice())
    else:
        print("HOPE YOU RETURN")
        break
    
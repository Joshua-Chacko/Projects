import json

def load_habits(habits: list) -> list:
    try:
        with open("habits.json", 'r') as file:
            habits = json.load(file)
            view_habits(habits)
            return habits
    except FileNotFoundError:
        print("No Prior Data...")
        return []

def save_habits(habits: list) -> None:
    print("Saving:", habits)
    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=4) 

def add_habits(habits: list) -> list:
    newHabit = input("Enter Habit: ")
    habits.append(newHabit)
    return habits

def delete_habits(habits: list) -> list:
    view_habits(habits)
    try:
        removeHabit = int(input("Choose Habit number to remove: "))
        habits.pop(removeHabit - 1)
    except (ValueError, IndexError):
        print("Invalid choice.")
    return habits

def view_habits(habits: list) -> None:
    print("")
    for idx, habit in enumerate(habits, start=1):
        print(f"{idx}. {habit}")
    print("")

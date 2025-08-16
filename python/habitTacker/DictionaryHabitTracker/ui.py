import storage
from datetime import datetime

def show_menu():
    print("1. Load Habits")
    print("2. Add Habit")
    print("3. Delete Habit")
    print("4. View Habits")
    print("5. Save Habits")
    print("Exit")

def handle_choices(Habits: list) -> list[dict]:
    choice_actions = {
    '1': storage.load_habits,
    '2': add_habits,
    '3': delete_habits,
    '4': view_habits,
    '5': storage.save_habits,
    'exit': exit_prg
    }
    choice = input("Enter Choice from menu: ").lower()
    while True:
        if choice not in choice_actions:
            print("Invalid Entry...")
            choice = input("Enter Choice from menu: ").lowe()
        elif choice in ['4']:  # view_habits
            choice_actions[choice](Habits)  # just call it
            break
        else:
            Habits = choice_actions[choice](Habits)  # functions that modify habits
            break
    return Habits

def add_habits(Habits: list[dict]) -> list[dict]:
    habit = {}
    habit["name"] = input("Enter Habit: ")
    habit["streak"] = 0
    habit["Last_completed"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Habits.append(habit)
    return Habits


def delete_habits(Habits: list[dict]) -> list[dict]:
    view_habits(Habits)
    delete_word = input("Enter the Habit to Delete: ")

    for idx, habit in enumerate(Habits):
        if delete_word in habit["name"]:
            Habits.remove(habit)


def view_habits(Habits: list[dict]) -> None:
    print("")
    for idx, habit in enumerate(Habits, start=1):
        print(f'{idx}. {habit["name"]}')
    print("")
    

def exit_prg(Habits: list[dict]) -> None:
    view_habits(Habits)
    storage.save_habits(Habits)
    quit()
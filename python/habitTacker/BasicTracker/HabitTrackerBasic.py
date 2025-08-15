# creating a habit tracker to work on Python syntax
# starting with basic user input into a list for different habits
# including adding, deleting, and re-list the differnt habbits
import json

def main() -> None:
    return_habits = input("Do you want to load saved habits? (y/n): ")
    if return_habits.lower() == 'y':
        Habits = load_habits()
        if Habits is None:
            Habits = []
        else:
            print("Loaded saved habits:")
            list_habits(Habits)
    else:
        Habits = []
    choice = input("Do You Want to add/delete/list habits (a/d/l): ")
    while True:
        match choice:
            case 'a':
                Habits.append(input("Enter A Habit: "))
            case 'd':
                list_habits(Habits)
                habits_input = input("Enter A Habit: ")
                if habits_input in Habits:
                    Habits.remove(habits_input)
                else:
                    print("Not a habit")
            case 'l':
                list_habits(Habits)
            case 'q':
                print("Quitting the habit tracker.")
                print("Saveing Habits...")
                list_habits(Habits)
                save_habits(Habits)
                quit()
            case _:
                print("Not an option! (a/d/l)")
        choice = input("Do You Want to add/delete/list habits (a/d/l) or enter q to quit: ")

def save_habits(habits: list) -> None:
    habitsdict = {i: n for i, n in enumerate(habits)}
        
    with open("habits.json", "w") as file:
        json.dump(habitsdict, file, indent=4, ensure_ascii=False)

def load_habits() -> list:
    try:
        with open('habits.json', 'r') as file:
            data = json.load(file)
            return list(data.values()) 
    except FileNotFoundError:
        print("No saved habits found.")
        return

def list_habits(habits: list) -> None:
    for i in habits:
        print(i)


if __name__ == "__main__":
    main()
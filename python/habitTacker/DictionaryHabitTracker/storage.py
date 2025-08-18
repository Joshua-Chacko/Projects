import json


def load_habits(habits: dict) -> dict:
    try:
        with open("habits.json", 'r') as file:
            habits = json.load(file)
            print(habits)
            view_habits(habits)
            return habits
    except FileNotFoundError:
        print("No Prior Data...")
        return {}

def save_habits(habits: dict) -> None:
    print("Saving:", habits)
    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=4) 
        return habits
    
    
def view_habits(Habits: list[dict]):
    print("------------------------------------")
    for idx, habit in enumerate(Habits, start=1):
        print(f'{idx}. {habit["name"]}')
    print("------------------------------------")
    return Habits
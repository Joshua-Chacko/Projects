import json
import ui

def load_habits(habits: dict) -> dict:
    try:
        with open("habits.json", 'r') as file:
            habits = json.load(file)
            ui.view_habits(habits.values())
            return habits
    except FileNotFoundError:
        print("No Prior Data...")
        return {}

def save_habits(habits: dict) -> None:
    print("Saving:", habits)
    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=4) 

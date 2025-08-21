def show_menu():
    print("1. Load Habits")
    print("2. Add Habit")
    print("3. Delete Habit")
    print("4. View Habits")
    print("5. Completed Habit")
    print("6. Show Streak")
    print("7. Save Habits")
    print("exit")


def handle_choices(manager) -> None:
    choice_actions = {
        '1': manager.load_habits,
        '2': lambda: manager.add_habit(input("Enter new habit name: ")),
        '3': lambda: manager.delete_habit(input("Enter habit name to delete: ")),
        '4': manager.view_habits,
        '5': lambda: mark_completed_ui(manager),
        '6': lambda: show_streak_ui(manager),
        '7': manager.save_habits,
        'exit': lambda: exit_prg(manager)
    }

    while True:
        choice = input("Enter Choice from menu: ").lower()
        if choice not in choice_actions:
            print("Invalid Entry...")
        else:
            choice_actions[choice]()  # call the function


def mark_completed_ui(manager):
    name = input("Enter habit name to mark completed: ")
    for habit in manager.habits:
        if habit.name == name:
            habit.mark_completed()
            print(f"{name} marked as completed!")
            return
    print("Habit not found.")


def show_streak_ui(manager):
    name = input("Enter habit name to show streak: ")
    for habit in manager.habits:
        if habit.name == name:
            print(f"{name} streak: {habit.get_streak()}")
            return
    print("Habit not found.")


def exit_prg(manager) -> None:
    manager.view_habits()
    manager.save_habits()
    quit()

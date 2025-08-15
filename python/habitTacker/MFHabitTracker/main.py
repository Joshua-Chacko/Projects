import storage

def show_menu() -> None:
    print("1. Load Habits")
    print("2. Add Habit")
    print("3. Delete Habit")
    print("4. View Habits")
    print("Exit")

def handle_choices(choice: str, habits: list) -> list:
    if choice == "2":
        habits = storage.add_habits(habits)
    elif choice == "3":
        habits = storage.delete_habits(habits)
    elif choice == "4":
        storage.view_habits(habits)
    elif choice == "1":
        habits = storage.load_habits(habits)
    else:
        print("System Shutting Down...")
        storage.save_habits(habits)
        quit()
    return habits


def main() -> None:
    Habits = [] 
    while True:
        show_menu()
        Habits = handle_choices(input("Choose from the menu: "), Habits)    

if __name__ == '__main__':
    main()
# creating a habit tracker to work on Python syntax
# starting with basic user input into a list for different habits
# including adding, deleting, and re-list the differnt habbits

def main() -> None:
    choice = input("Do You Want to add/delete/list habits (a/d/l): ")
    Habits = []
    while choice != 'q':
        match choice:
            case 'a':
                list_habits(Habits)
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
            case _:
                print("Not an option! (a/d/l)")
        choice = input("Do You Want to add/delete/list habits (a/d/l) or enter q to quit: ")

def list_habits(habits: list) -> None:
    for i in habits:
        print(i)


main()
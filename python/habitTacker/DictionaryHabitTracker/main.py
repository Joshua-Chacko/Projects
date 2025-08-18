from ui import *
from datetime import datetime

def main() -> None:
    Habits = []
    Habits = load_habits(Habits)
    while True:           
        show_menu()
        Habits = handle_choices(Habits)

if __name__ == '__main__':
    main()
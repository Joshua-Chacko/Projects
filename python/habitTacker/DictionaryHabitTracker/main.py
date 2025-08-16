import ui
from storage import save_habits, load_habits
from datetime import datetime

def main() -> None:
    Habits = []
    while True:
        ui.show_menu()
        Habits = ui.handle_choices(Habits)

if __name__ == '__main__':
    main()
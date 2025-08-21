from habits import HabitManager
import ui

def main():
    manager = HabitManager()  # keep ONE manager across the loop
    while True:
        ui.show_menu()
        ui.handle_choices(manager)

if __name__ == "__main__":
    main()

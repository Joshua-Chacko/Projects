import json

class HabitManager:
    """Manages collection of multiple Habits objects"""
    def __init__(self):
        self.habits = []

    def add_habit(self, name: str):
        new_habit = Habits(name)
        self.habits.append(new_habit)

    def delete_habit(self, name: str):
        self.habits = [h for h in self.habits if h.name != name]

    def load_habits(self):
        try:
            with open('habits.json', 'r') as file:
                content = file.read().strip()
                if not content:  # <-- file is empty
                    print("No data in habits.json, starting fresh...")
                    self.habits = []
                    return
                data = json.loads(content)
                self.habits = [Habits.from_dict(h) for h in data]
                print("Habits loaded successfully.")
        except FileNotFoundError:
            print("No Prior Data...")
            self.habits = []
  

    def save_habits(self):
        with open('habits.json', 'w') as file:
            json.dump([h.to_dict() for h in self.habits], file, indent=4)
            print("Habits saved successfully.")

    def view_habits(self):
        if not self.habits:
            print("No habits found.")
        else:
            for h in self.habits:
                print(h)


class Habits:
    """Individual habit object with its own methods"""
    def __init__(self, name, streak=0, time_completed=None):
        self.name = name
        self.streak = streak
        self.time_completed = time_completed

    def mark_completed(self):
        self.streak += 1

    def get_streak(self):
        return self.streak

    def __str__(self):
        return f"Habit {self.name}, streak {self.streak}, completed at {self.time_completed}"

    # 🔑 conversion helpers
    def to_dict(self):
        return {
            "name": self.name,
            "streak": self.streak,
            "time_completed": self.time_completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data.get("streak", 0), data.get("time_completed"))

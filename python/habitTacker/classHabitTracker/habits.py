class HabitManager:
    """Manages collection of multiple Habits objects"""
    def __init__(self):
        self.habits = []

        def add_habits(self, name):
            ...
        
        def delete_habits(self, name):
            ...

        def load_habits(self):
            ...

        def save_habits(self):
            ...      


class Habits:
    """Individual habit object with its own methods"""
    def __init__(self, name):
        self.name = name
        self.streak = 0
        self.time_completed = None

    def mark_completed(self):
        ...

    def get_streak(self):
        ...

    def __str__(self):
        return print(f"Habit {self.name}, with streak of {self.streak}, completed at {self.time_completed}")
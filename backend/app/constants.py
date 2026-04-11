from enum import Enum

class Occurance(str, Enum):
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"

class HabitType(str, Enum):
    binary = "binary"
    duration = "duration"  # can be used for habits like "meditate for 10 minutes", "exercise for 30 minutes" where the user can log the duration instead of just completed/not completed
    numeric = "numeric"  # can be used for habits like "drink 8 glasses of water", where the user can log a number instead of just completed/not completed</content>

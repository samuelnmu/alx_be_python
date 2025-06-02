task = input("Enter your task: ")
priority = input("Enter the priority level (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        message = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        message = f"Reminder: '{task}' is a LOW priority task."
    case _:
        message = f"Reminder: '{task}' has an UNKNOWN priority level."

if time_bound == "yes":
    message += " It requires immediate attention today!"

print(message)

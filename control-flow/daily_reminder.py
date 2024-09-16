#task reminder

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

#match cases
match priority:
    case "high":
        if time_bound == 'yes':
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
    case "low":
        print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case "medium":
        print(f"Reminder: {task} is a {priority} priority task. Consider completing it when you have free time")
    case _:
        print("Invalid input. Please enter yes or no.")
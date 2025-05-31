task_d = input("Enter task description: ")
task_p = input("Enter task priority: (high, medium, low) ")

time_bound = input("Is the task time bound: (yes or no) ")

match task_p:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task_d}' is a {task_p} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task_d}' is a {task_p} priority task. Consider completing it when you have free.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task_d}' is a {task_p} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task_d}' is a {task_p} priority task. Consider completing it when you have free.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task_d}' is a {task_p} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task_d}' is a {task_p} priority task. Consider completing it when you have free.")

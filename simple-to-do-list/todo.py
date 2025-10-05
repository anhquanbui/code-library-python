# Simple in-memory to-do list (no files, no menus)
# Type tasks one by one; press Enter on an empty line to finish.

todos = []  # this will store tasks in memory

print("Enter tasks (press Enter on an empty line to finish):")
while True:
    task = input("Task: ").strip()
    if not task:           # stop when the input is empty
        break
    todos.append(task)     # store the task in the list

# Print the result
print("\nYour To-Do List:")
for i, t in enumerate(todos, start=1):   # enumerate gives (index, value)
    print(f"{i}. {t}")

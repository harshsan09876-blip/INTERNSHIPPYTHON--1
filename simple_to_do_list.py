#simple - to - do - list
# use list methods
# # ============================================
# Day 8 - Simple To-Do List
# Veda Technology - Python Programming Internship
# ============================================

# PSEUDOCODE / LOGIC:
# 1. Create a list to store tasks
# 2. Display a menu to the user
# 3. Ask the user to enter a choice
# 4. If choice is 1:
#       Take a new task
#       Add it to the list
# 5. If choice is 2:
#       Display all tasks using a loop
# 6. If choice is 3:
#       Ask which task to update
#       Ask for the new task
#       Replace the old task
# 7. If choice is 4:
#       Ask which task to remove
#       Remove it from the list
# 8. If choice is 5:
#       Exit the program
# 9. Otherwise:
#       Display "Invalid choice"
# 10. Repeat the menu until the user chooses Exit


# LIST:
# Your original idea:
# tasks = ["Shahi paneer", "malai kofta", "naan", "sundaye"]

tasks = ["Shahi paneer", "malai kofta", "naan", "sundaye"]


# MENU:
# while True keeps displaying the menu
# until the user chooses option 5.

while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

    user = input("Enter the choice: ")


    # ============================================
    # CREATE - ADD TASK
    # ============================================

    # Your idea:
    # new_task = input("Enter a new task: ")
    # tasks.append(new_task)

    if user == "1":

        new_task = input("Enter a new task: ")

        tasks.append(new_task)

        print("Task added successfully!")


    # ============================================
    # READ - VIEW TASKS
    # ============================================

    # Your idea:
    # for task in tasks:
    #     print(task)

    elif user == "2":

        print("\nYour Tasks:")

        for task in tasks:
            print(task)


    # ============================================
    # UPDATE TASK
    # ============================================

    # Your idea:
    # update_task = input(...)
    # new_task = input(...)
    # tasks.remove(update_task)
    # tasks.append(new_task)

    elif user == "3":

        update_task = input("Enter the task you want to update: ")
        new_task = input("Enter the new task: ")

        # Find the old task and replace it
        if update_task in tasks:

            index = tasks.index(update_task)
            tasks[index] = new_task

            print("Task updated successfully!")

        else:
            print("Task not found!")


    # ============================================
    # DELETE - REMOVE TASK
    # ============================================

    # Your idea:
    # remove_task = input("Enter the task to remove: ")
    # tasks.remove(remove_task)

    elif user == "4":

        remove_task = input("Enter the task to remove: ")

        if remove_task in tasks:

            tasks.remove(remove_task)

            print("Task removed successfully!")

        else:
            print("Task not found!")


    # ============================================
    # EXIT
    # ============================================

    # Your idea:
    # elif user == "5":
    #     exit()

    # We use break to stop the while loop.

    elif user == "5":

        print("Exiting To-Do List...")
        break


    # ============================================
    # INVALID CHOICE
    # ============================================

    # Your idea:
    # try / except / catch invalid error
    #
    # For the menu, we can simply use else
    # because the input is being treated as text.

    else:

        print("Invalid choice! Please enter 1-5.")
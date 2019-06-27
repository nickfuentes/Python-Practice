# Created a function to show the menu to the user when app runs

todos = []


def print_menu():
    print("----- Todo App Menu -----")
    print("Press (1) to add task")
    print("Press (2) to delete task")
    print("Press (3) to view all tasks")
    print("Press (q) to quit")
    print("-------------------------")


user_input = ""

while user_input != "q":
    print_menu()
    user_input = input("What would you like to do? ")

    if user_input == "1":
        title = input("Please enter a title: ")
        priority = input("Please enter priority: ")

        todo = {
            "title": title,
            "priority": priority
        }
        todos.append(todo)
        print("***** You have added a todo! *****")
        print(todo)

    elif user_input == "2":
        print("***** Here is your Todo list: *****")
        for index in range(0, len(todos), 1):
                print(index, todos[index])
        delete_todo = int(
            input("Enter the index of the task you want to delete? "))
        del todos[delete_todo]

    elif user_input == "3":
        print("***** Here is your Todo list: *****")
        for index in range(0, len(todos), 1):
            print(index, todos[index])


# Steps to create todo app

# Show user menu option
# Ask the user what they would like to do
# Create option to add task, ask for title and priority of the task (high, medium and low)
# Create option to delete task that show all the task along with the index number so they can type in the nuber to delete
# Create an option to view all tasks to the user, in the format of 1 - Wash the car - high

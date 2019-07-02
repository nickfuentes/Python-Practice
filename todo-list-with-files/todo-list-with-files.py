import json
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
        print("***** You have added a Todo! *****")
        print(todo)
        with open("todo-list-with-files.json", "w") as file_object:
            json.dump(todos, file_object)

    elif user_input == "2":
        print("***** Here is your Todo List! *****")
        for index in range(0, len(todos), 1):
            print(index, todos[index])
        delete_todo = int(
            input("Enter the index of the task you want to delete: "))
        del todos[delete_todo]
        with open("todo-list-with-files.json", "w") as file_object:
            json.dump(todos, file_object)
    elif user_input == "3":
        print("***** Here is your Todo List! *****")
        for index in range(0, len(todos), 1):
            print(index, todos[index])

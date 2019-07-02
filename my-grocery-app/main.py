from shopping_list import ShoppingList
from grocery_item import GroceryItem

shopping_lists = []

shopping_lists.append(shopping_list)
shopping_lists.append(shopping_list2)
shopping_list = ShoppingList("HEB", "1200 Richmond")
shopping_list2 = ShoppingList("Walmart", "345 Harvin")


def print_menu():
    print("----- Todo App Menu -----")
    print("Press (1) Create List")
    print("Press (2) Add Items To List")
    print("Press (3) View All Lists")
    print("Press (q) To Quit")
    print("-------------------------")


print_menu()

user_input = ""

while user_input != "q":
    print_menu()
    user_input = input("What would you like to do? ")

    if user_input == "1":
        title = input("Please enter store name: ")
        address = input("Please enter store address: ")

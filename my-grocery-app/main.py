# pulling classes from other files and making it avaiable in main.py
from shopping_list import ShoppingList
from grocery_item import GroceryItem


def print_menu():
    print("--------------------------------")
    print("******* Grocery App Menu *******")
    print("--------------------------------")
    print("Press (1) Create Grocery List")
    print("Press (2) Add Grocery Items")
    print("Press (3) View Shopping List")
    print("Press (q) to quit")
    print("--------------------------------")


# list of shopping lists
shopping_lists = []
user_input = ""

while user_input != "q":
    print_menu()
    user_input = input("What would you like to do? ")

    if user_input == "1":
        store_name = input("Enter a store name: ")
        store_address = input("Enter a store address: ")
        shopping_list = ShoppingList(store_name, store_address)
        shopping_lists.append(shopping_list)
        while user_input != "n":
            item_name = input("Enter item name: ")
            item_price = input("Enter item price: ")
            item_quantity = input("Enter item quanity: ")
            grocery_item = GroceryItem(item_name, item_price, item_quantity)
            shopping_list.grocery_items.append(grocery_item)
            user_input = input(
                "Would you like to add another item? yes = [y] / no = [n] ")
        for shopping_list in shopping_lists:
            print("--------------------------------")
            print("***** Grocery List Created *****")
            print("--------------------------------")
            print(
                f"{shopping_list.name} {shopping_list.address}")
        for item in shopping_list.grocery_items:
            print(f"Item: {item.name}")
            print(f"Price: {item.price}")
            print(f"Quantity: {item.quantity}")
    elif user_input == "2":
        print("--------------------------------")
        print("****** Your Shopping Lists *****")
        print("--------------------------------")
        for list in shopping_lists:
            print(f"Store: {list.name}")
            print(f"Address: {list.address}")
            print("Items:")
            for item in list.grocery_items:
                print(f"{item.name} Price: {item.price} Quantity: {item.quantity}")
            print("--------------------------------")
        while user_input != "n":
            item_name = input("Enter item name: ")
            item_price = input("Enter item price: ")
            item_quantity = input("Enter item quanity: ")
            grocery_item = GroceryItem(item_name, item_price, item_quantity)
            shopping_list.grocery_items.append(grocery_item)
            user_input = input(
                "Would you like to add another item? yes = [y] / no = [n] ")
    elif user_input == "3":
        print("--------------------------------")
        print("****** Your Shopping Lists *****")
        print("--------------------------------")
        for list in shopping_lists:
            print(f"Store: {list.name}")
            print(f"Address: {list.address}")
            print("Items:")
            for item in list.grocery_items:
                print(f"{item.name} Price: {item.price} Quantity: {item.quantity}")
            print("--------------------------------")

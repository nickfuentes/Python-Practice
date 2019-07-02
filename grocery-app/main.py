# from modulename import Class or Function
from shopping_list import ShoppingList
from grocery_item import GroceryItem

# keep track of all shopping lists
shopping_lists = []

shopping_list = ShoppingList("HEB", "1200 Richmond")
shopping_list2 = ShoppingList("Walmart", "345 Harvin")

# add the shopping list to the array
shopping_lists.append(shopping_list)
shopping_lists.append(shopping_list2)

# display all shopping lists
for index in range(0, len(shopping_lists)):
    print(
        f"{index+1} - {shopping_lists[index].name} - {shopping_lists[index].address}")

shopping_list_number = int(
    input("Enter the shopping list number to add items to: "))

shopping_list_to_add_items = shopping_lists[shopping_list_number - 1]

grocery_item = GroceryItem("Milk", 10, 2)

shopping_list_to_add_items.grocery_items.append(grocery_item)

print(shopping_lists[0].grocery_items[0].name)

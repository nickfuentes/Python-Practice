import json  # import json module to work with json

names = ["Mary", "Alex", "John"]

# writing json to customer.json file
with open("customers.json", "w") as file_object:
    json.dump(names, file_object)  # writing an array

# Reading the contents of customers.json file
with open("customers.json") as file_object:
    customers = json.load(file_object)  # getting back an array

print(customers)


# write a dictionary to json

person = {"name": "John", "age": 34, "occupation": "Developer"}
person2 = {"name": "Mary", "age": 45, "occupation": "Developer"}

person_list = [person, person2]  # array of two people

with open("persons.json", "w") as file_object:
    json.dump(person_list, file_object)

with open("persons.json") as file_object:
    customers = json.load(file_object)  # getting back an array

print(customers)

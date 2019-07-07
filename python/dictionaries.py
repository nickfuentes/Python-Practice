# Dictionaries
grocery = {
    "name": "Milk",
    "quantity": 2,
    "address": "122200 Richmond",
    "phone": "453-343-3423"
}

airports = {"IAH": "Intercontinal Airpot Houston"}


# adding values to the dictionary
grocery["storeNumber"] = "STORE0000"

# update the value of a dictionary
grocery["quality"] = 12


# deleting from the dictionary
del grocery["address"]

# iterate through the dictionary
for (key, value) in grocery.items():
    print(key, value)

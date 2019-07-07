
cars = []  # empty array

user_input = ""

while user_input != "q":
    make = input("Enter make: ")
    model = input("Enter model: ")
    color = input("Enter color: ")
    # add a car in the cars array
    car = {
        "make": make,
        "model": model,
        "color": color
    }

    cars.append(car)  # add dictionary to the array
    print(cars)

    user_input = input("Press q to quit or anything to continue! ")

   # what do you think item at 0 ?

cars = []


# creating the Car class
class Car:
    # constructor or initializer
    def __init__(self, make, model, color):
        self.make = make  # set property make to the arguement make
        self.model = model
        self.color = color

# Passing self makes the the drive function availble to thte Car Objects
    def drive(self):
        print("Driving the car")


make = input("Enter make: ")
model = input("Enter model: ")


car = Car("Toyota", "Corrola", "Black")
#car.make = make
#car.model = model

cars.append(car)
print(cars)

# drive the car, calling the drive car class
# car.drive()

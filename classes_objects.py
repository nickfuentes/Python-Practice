# Creating the car class
class Car:
    # Constructor or intializer, to create the car object
    # This is the blue print to collected the data
    def _int_(self):
        self.make = ""
        self.model = ""
        self.color = ""

    def drive(self):
        print("Driving the car")

# Creating the object of the car class


car = Car()
car.make = "BMW"
car.model = "Series 3"
car.color = "White"

car2 = Car()
car2.make = "Honda"
car2.model = "Accord"
car2.color = "Black"

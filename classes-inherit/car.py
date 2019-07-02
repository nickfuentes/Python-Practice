class Car: 
    def __init__(self,make,model): 
        self.make = make 
        self.model = model 
        self.vin = ""
        self.noOfCylinders = 2 
        #self.properyname

    def drive(self): 
        print("Car is driving!")

    def fillUp(self): 
        print("Fill Up Gas")

class ElectricCar(Car): # inherit from the Car class  
    def __init__(self,make,model, battery_range): 
        super().__init__(make,model) # super is the base/parent class
        self.range = battery_range
    
    def fillUp(self): 
        print("Charge the car with an outlet!")



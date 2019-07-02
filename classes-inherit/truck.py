# from module (car.py) import Car (Class)
from car import Car 

class Truck(Car): 
    def __init__(self,make,model): 
        super().__init__(make,model)
    
    # overriding the default parent/super/base implementation of the fillUp function
    def fillUp(self): 
        print("Fill up with Diesal")
    
    
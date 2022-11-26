# Class Inheritance
"""Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.Create a Bus class that inherits from the Vehicle class. 
   Give the capacity argument of Bus.seating_capacity() a default value of 50."""
""" not use inheritance
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
a=Vehicle("volvo",50,89)
print(a)
def seating_capacity(self, capacity):
    
    return f"The seating capacity of a bus {self.name} in {capacity} passengers"
b=seating_capacity(a,50)
print(b)"""


# use inheritance

class Vehicle:
    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):

        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    
    def seating_capacity(self,capacity=50):
        
        return super().seating_capacity(capacity=50)
school_bus=Bus("volvo",180,60)
print(school_bus.seating_capacity())
print(school_bus)


    
        



        
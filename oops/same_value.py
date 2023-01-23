# Define a property that must have the same value for every class instance (object)

class Vehicle:

    color = "white "

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

same_value_car1=Bus("audi","200","10")
print("Colour:",same_value_car1.color,"Car name:",same_value_car1.name,"maximim speed:",same_value_car1.max_speed,"Milage:",same_value_car1.mileage)

same_value_car2=Car("mersidese banze","200","10")
print("Colour:",same_value_car2.color,"Car name:",same_value_car2.name,"maximim speed:",same_value_car2.max_speed,"Milage:",same_value_car2.mileage)

# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class


class Vehical:
    
        def __init__(self,name,max_speed,milage):
            self.speed=max_speed
            self.milage=milage
            self.name=name

class Bus(Vehical):
    pass

info=Bus("volvo",100,50)
print("Vehical name :",info.name,",maximum speed :",info.speed,",Milage :",info.milage)
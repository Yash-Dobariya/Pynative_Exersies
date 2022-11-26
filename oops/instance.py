# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.


class Vehical:
    pass

    def __init__(self,max_speed,mileage):
        self.max_speed= max_speed
        self.mileage = mileage
test=Vehical(40,50)
print(test.max_speed,test.mileage)

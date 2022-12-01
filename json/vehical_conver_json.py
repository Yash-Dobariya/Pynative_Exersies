# Convert the following Vehicle Object into JSON


import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
        
class VehicleEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

convert_obj=json.dumps(vehicle , indent=4, cls=VehicleEncoder)
print(convert_obj)
#HWhite- M3 Case Study: Lists, Functions, and Classes
#create vehicle superclss with vehicle type attribute.
class Vehicle:
    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type
#create automobile class with year, make, mode, doors, and roof attributes.
class Automobile (Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        
#get attributes and assign to vehicle1
vehicle_type = input("Enter vehicle type:")
year = input("Enter vehicle year:")
make= input("Enter vehicle make:")
model = input("Enter vehicle model:")
doors= input("Enter vehicle doors (2 or 4):")
roof= input("Enter vehicle roof(solid or sun roof):")
vehicle1 = Automobile(vehicle_type,year,make,model,doors,roof)

#print attribites of vehicle1
print("Vehicle type:", vehicle1.vehicle_type)
print("Year:", vehicle1.year)
print("Make:", vehicle1.make)
print("Model:", vehicle1.model)
print("Number of doors:", vehicle1.doors)
print("Type of roof:", vehicle1.roof)
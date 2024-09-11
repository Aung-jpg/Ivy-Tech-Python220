class Vehicle:
    def __init__(self, vehicle_type: str):
        self.vehicle_type = vehicle_type.title()

    def show_vehicle_type(self):
        print(self.vehicle_type)

class Automobile(Vehicle):
    def __init__(self, year: int, make: str, model: str, doors: int, roof: str):
        super().__init__("car")
        self.year = year
        self.make = make.title()
        self.model = model.title()
        self.doors = doors
        if self.doors not in [2, 4]:
            raise ValueError("The amount of doors has to be 2 or 4")
        self.roof = roof
        if self.roof.lower() not in ['solid', 'sun roof']:
            raise ValueError("The roof has to be a solid or sun roof")
        
    def show_data(self):
        print(f"vehicle type: {self.vehicle_type}\nyear: {self.year}\nmake: {self.make}\nmodel: {self.model}\ndoors: {self.doors}\nroof: {self.roof}\n")
        
def main():
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")
    car = Automobile(year, make, model, doors, roof)
    car.show_data()

main()
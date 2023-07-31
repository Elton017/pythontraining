class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

class Truck(Vehicle):
    pass

class Customer:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def purchase_vehicle(self, vehicle):      
        self.vehicles.append(vehicle)


# Test your classes here:
car1 = Car("Toyota", "Camry", 2022)
motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2021)
truck1 = Truck("Ford", "F-150", 2020)

customer1 = Customer("John Doe")
customer1.purchase_vehicle(car1)
customer1.purchase_vehicle(motorcycle1)
customer1.purchase_vehicle(truck1)

print(f"{customer1.name} owns the following vehicles:")
for vehicle in customer1.vehicles:
    vehicle.display_info()
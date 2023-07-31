class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
    
    def __str__(self):
        return f'Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage {self.mileage}'
    
    def drive(self, distance):
        self.mileage = self.mileage + distance
        return self.mileage
    
car1 = Car("Toyota", "Camry", 2022, 15000.5)
print(str(car1))

car1.drive(100.25)
print(str(car1))
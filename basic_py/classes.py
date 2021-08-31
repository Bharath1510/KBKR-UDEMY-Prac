class Car:
    def __init__(self, name, gear, mileage):
        self.name = name
        self.gear = gear
        self.mileage = mileage

    def drive(self, miles):
        self.mileage += miles

    def shift_gear(self, gear):
        self.gear = gear


car = Car("Toyota", 5, 10)
car.shift_gear(2)
car.drive(233)
print(car.mileage) 
print(car.gear)
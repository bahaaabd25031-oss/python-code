class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def driving(self):
        print(f'{self.brand} is driving')
    def describe(self):
        print(f'{self.brand} made in {self.year}')

class car(Vehicle):
    def honk(self):
        print(f'{self.brand} says : honk honk!')
class bike(Vehicle):
    def ring_bell(self):
        print(f'{self.brand} rings the bell')

car1 = car('toyota','1999')
bike1 = bike('yamaha','2020')

for vehicle in [car1,bike1]:
    vehicle.describe()
    vehicle.driving()
else:
    car1.honk()
    bike1.ring_bell()
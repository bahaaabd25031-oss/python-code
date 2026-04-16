class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

i = 0
cars = []
while i<3:
   brand = input("Enter brand: ")
   model = input("Enter model: ")
   car = Car(brand, model)
   cars.append(car)
   i=i+1


for x in cars:
  print(x.brand)
  print(x.model)
  x.move()

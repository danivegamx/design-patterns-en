"""
 Design Patterns v1

 Design -> Creational -> Factory Pattern
 Python
 Daniel Vega Ceja, 2015
"""
# The layers, are representations of car building.

# Importing abstract class.
from abc import ABCMeta

# Product
class Car(metaclass=ABCMeta):
    def __init__(self):
        self.name = None
        self.maxSpeed = None

    def __str__(self):
        return "Name is {:s}. Max-speed is {:s}".format(self.name, self.maxSpeed)

# Defining type of product.
class SportCar(Car):
    def __init__(self):
        self.name = "Sport"
        self.maxSpeed = "250 km/h"

class FamilyCar(Car):
    def __init__(self):
        self.name = "Family"
        self.maxSpeed = "150 km/h"

# Building the object.
class MyFactory:
    def createCar(self, carType):
        self.car = None
        if carType == "sport":
            self.car = SportCar()
        elif carType == "family":
            self.car = FamilyCar()
        else:
            print("Car type {:s} is not defined... Yet.".format(carType))
        return self.car

    # Action or testing the factory.
    def doSomething(self):
        print(self.car)

if __name__ == "__main__":
    # Calling the factory.
    myFactory = MyFactory()

    # Define types of product.
    s = myFactory.createCar("sport")
    f = myFactory.createCar("family")
    h = myFactory.createCar("hybrid")

    print(s)
    print(f)
    print(h)

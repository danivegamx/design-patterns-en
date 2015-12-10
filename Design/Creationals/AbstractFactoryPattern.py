"""
 Design Patterns v1

 Design -> Creational -> AbstractFactory Pattern
 Python
 Daniel Vega Ceja, 2015
"""
# The layers, are representations of car building.

# Import abstract class.
from abc import ABCMeta, abstractmethod

# Product.
class Car(metaclass=ABCMeta):
    def __init__(self):
        self.name = None
        self.maxSpeed = None

    def __str__(self):
        return "Name is {:s}. Max-speed is {:s}".format(self.name, self.maxSpeed);

# Define types of product.
class SportCar(Car):
    def __init__(self):
        self.name = "Sport"
        self.maxSpeed = "250 km/h"

class FamilyCar(Car):
    def __init__(self):
        self.name = "Family"
        self.maxSpeed = "150 km/h"

# Abstract factory -> Define families of the final product. (car)
class AbstractFactory(metaclass=ABCMeta):
    def __init__(self):
        self.manufacturer = None

    def __str__(self):
        return "Manufacturer is {:s}".format(self.manufacturer)

    # Passing the carType to the family.
    @abstractmethod
    def createCar(self, carType): pass

    @staticmethod
    def getFactory(factoryName):
        if factoryName == "vw":
            return VWFactory()
        elif factoryName == "bmw":
            return BMWFactory()
        elif factoryName == "mb":
            return MBFactory()

# Defining the product's families.
class VWFactory(AbstractFactory):
    def __init__(self):
        self.manufacturer = "Volks Wagen"

    def createCar(self, carType):
        self.car = None
        if carType == "sport":
            self.car = SportCar()
        elif carType == "family":
            self.car = FamilyCar()
        else:
            print("Car type {:s} is not defined... Yet.".format(carType))
        return self.car

    def doSomething(self):
        print(self.car)

class BMWFactory(AbstractFactory):
    def __init__(self):
        self.manufacturer = "BMW"

    def createCar(self, carType):
        self.car = None
        if carType == "sport":
            self.car = SportCar()
        elif carType == "family":
            self.car = FamilyCar()
        else:
            print("Car type {:s} is not defined... Yet.".format(carType))
        return self.car

    def doSomething(self):
        print(self.car)

class MBFactory(AbstractFactory):
    def __init__(self):
        self.manufacturer = "Mercedes Benz"

    def createCar(self, carType):
        self.car = None
        if carType == "sport":
            self.car = SportCar()
        elif carType == "family":
            self.car = FamilyCar()
        else:
            print("Car type {:s} is not defined... Yet.".format(carType))
        return self.car

    def doSomething(self):
        print(self.car)

if __name__ == "__main__":
    # Getting the family.
    myAbsFactory = AbstractFactory.getFactory("bmw")

    print(myAbsFactory)

    # Build cars from the family.
    s = myAbsFactory.createCar("sport")
    f = myAbsFactory.createCar("family")

    print(s)
    print(f)

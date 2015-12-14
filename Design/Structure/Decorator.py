"""
 Design Patterns v1

 Design -> Structure -> Facade
 Python
 Daniel Vega Ceja, 2015
"""

from abc import ABCMeta

class Car(metaclass=ABCMeta):
    def draw(self):
        pass

class Sport(Shape):
    def draw(self):
        print("I am a sport car")

class Family(Shape):
    def draw(self):
        print("I am a family car")

class CarDecorator(Shape):
    def __init__(self, decoratedShape):
        self.decoratedShape = decoratedShape

    def draw(self):
        self.decoratedShape.draw()

    def doSomethingElse(self):
        pass

class ColorRedCarDecorator(ShapeDecorator):
    def draw(self):
        self.doSomethingElse()
        self.decoratedShape.draw()

    def doSomethingElse(self):
        print("Color red")

if __name__ == "__main__":
    car = Sport()
    redCar = ColorRedCarDecorator( Sport() )

    car.draw()
    print("--------------------------------")
    redCar.draw()

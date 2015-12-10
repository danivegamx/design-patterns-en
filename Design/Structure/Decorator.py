"""
 Design Patterns v1

 Design -> Structure -> Facade
 Python
 Daniel Vega Ceja, 2015
"""

from abc import ABCMeta

class Shape(metaclass=ABCMeta):
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("I am a circle")

class Rectangle(Shape):
    def draw(self):
        print("I am a rectangle")

class ShapeDecorator(Shape):
    def __init__(self, decoratedShape):
        self.decoratedShape = decoratedShape

    def draw(self):
        self.decoratedShape.draw()

    def doSomethingElse(self):
        pass

class ColorRedShapeDecorator(ShapeDecorator):
    def draw(self):
        self.doSomethingElse()
        self.decoratedShape.draw()

    def doSomethingElse(self):
        print("Color red")

if __name__ == "__main__":
    circle = Circle()
    redCircle = ColorRedShapeDecorator( Circle() )

    circle.draw()
    print("--------------------------------")
    redCircle.draw()

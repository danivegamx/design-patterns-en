"""
 Design Patterns v1

 Design -> Behavior -> Stategy Pattern
 Python
 Daniel Vega Ceja, 2015
"""

from abc import ABCMeta, abstractmethod

class TextFinder(metaclass=ABCMeta):
	def find(self, text):
		pass

class PlatziFinder(TextFinder):
	def find(self, text):
		return " {:s} fue encontrado".format(text)

class MyOtherFinder(TextFinder):
	def find(self, text):
		return " {:s} was found".format(text)

if __name__ == "__main__":
	finderOne = PlatziFinder()
	finderTwo = MyOtherFinder()

	print(finderOne.find("abc"))

	print(finderTwo.find("abc"))

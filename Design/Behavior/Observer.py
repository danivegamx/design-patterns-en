"""
 Design Patterns v1

 Design -> Behavior -> Observer Pattern
 Python
 Daniel Vega Ceja, 2015
"""

# Forum / Blog posting.

from abc import ABCMeta, abstractmethod

class Publisher(metaclass=ABCMeta):
	# Observable
	def __init__(self):
		pass

	def addObserver(self, observer):
		pass

	def removeObserver(self, observer):
		pass

	def notifyAll(self):
		pass

class DaniForum(Publisher):
	def __init__(self):
		self.usersList = []
		self.post = None

	def addObserver(self, observer):
		if observer not in self.usersList:
			self.usersList.append(observer)

	def removeObserver(self, observer):
		self.usersList.remove(observer)

	def notifyAll(self):
		for observer in self.usersList:
			observer.notify(self.post)

	def writePost(self, text):
		self.post = text
		self.notifyAll()


class Subscriber:
	def __init__(self):
		pass
	def notify(self, post):
		pass

class UserA(Subscriber):

	def __init__(self):
		pass
	def notify(self, post):
		print("UserA has been notified %s" % post)

class UserB(Subscriber):

	def __init__(self):
		pass
	def notify(self, post):
		print("UserB has been notified %s" % post)

if __name__ == "__main__":
	foroDani = DaniForum()
	user1 = UserA()
	user2 = UserB()

	foroDani.addObserver(user1)
	foroDani.addObserver(user2)

	foroDani.writePost("mi primer post en Dani")

	foroDani.removeObserver(user2)

	foroDani.writePost("mi segundo post ")

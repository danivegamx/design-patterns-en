"""
 Design Patterns v1

 Design -> Behavior -> Command Pattern
 Python
 Daniel Vega Ceja, 2015
"""

# Representation of a light on/off.

from abc import ABCMeta

class Command(metaclass=ABCMeta):
	def execute(self):
		pass


class Light:
	""" clase Receiver"""
	def turnOn(self):
		print("Light On!")

	def turnOff(self):
		print("Light Off!")


class Switch:
	# Invoker
	def __init__(self, onCommand, offCommand):
		self._onCommand = onCommand
		self._offCommand = offCommand


	def on(self):
		self._onCommand.execute();

	def off(self):
		self._offCommand.execute();


class OnCommand(Command):
	def __init__(self, light):
		self._light = light

	def execute(self):
		self._light.turnOn()

class OffCommand(Command):
	def __init__(self, light):
		self._light = light

	def execute(self):
		self._light.turnOff()


class LightSwitch:
	# Client
	def __init__(self):
		self._foco = Light()
		self._switchUp = OnCommand(self._foco)
		self._switchDown = OffCommand(self._foco)
		self._switch = Switch(self._switchUp, self._switchDown)

	def operation(self, cmd):
		if cmd =="ON":
			self._switch.on()
		elif cmd =="OFF":
			self._switch.off()
		else:
			print("Invalid operation")

if __name__ == "__main__":
	client = LightSwitch()
	print("Testing ON command")
	client.operation("ON")
	print("Testing OFF command")
	client.operation("OFF")

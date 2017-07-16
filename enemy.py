from entity import *
from pygame.math import *
import movement
import pattern
from collections import namedtuple

class Enemy(Entity):
	def __init__(self, rect, surf):
		Entity.__init__(self, rect, surf)
		#self.pattern = pattern.patternSquare(self)
		self.pattern = pattern.Pattern3(self)

	def update(self, timePassed):
		self.timePassed+=timePassed
		self.updateMovement()
		self.updateRect()
		self.animation()
		self.timePassed = 0

	def updateMovement(self):
		self.pattern.update(self.timePassed)

	#def setType(self, Type):
		#self.Type = Type

	def updateRect(self):
		Entity.updateRect(self)

class enemyType():
	def __init__(self, data):
		Movement = namedtuple("Movement","direction delay")
		self.movements = []
		self.name = data["name"]
		for a in data['movements']:
			self.movements.append(Movement(direction=Vector2(a['x'],a['y']),delay=a['delay']))

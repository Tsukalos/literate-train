from entity import *
from pygame.math import *
import movement
import pattern
from collections import namedtuple

class Enemy(Entity):
	def __init__(self, rect, surf):
		Entity.__init__(self, rect, surf)
		#self.pattern = pattern.patternSquare(self)
		#self.pattern = pattern.Pattern3(self)

	def update(self, timePassed):
		self.timePassed+=timePassed
		self.updateMovement()
		self.updateRect()
		self.animation()
		self.timePassed = 0

	def updateMovement(self):
		self.pattern.update(self.timePassed)

	def loadPattern(self, pattern):
		self.pattern = pattern

	#def setType(self, Type):
		#self.Type = Type

	def updateRect(self):
		Entity.updateRect(self)

class enemyType():
	def __init__(self):
		pass

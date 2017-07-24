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
		self.updateMovementPattern()
		self.updateRect()
		self.animation()
		self.timePassed = 0

	def updateMovementPattern(self):
		self.movementPattern.update(self.timePassed)

	def loadEnemy(self, pattern, name):
		self.movementPattern = pattern
		self.name = name

	#def setType(self, Type):
		#self.Type = Type

	def updateRect(self):
		Entity.updateRect(self)


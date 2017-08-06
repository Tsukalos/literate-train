from entity import *
from pygame.math import *
from collections import namedtuple
import bulletpattern

class Enemy(Entity):
	def __init__(self, rect, surf, mask, tileSize, animationInterval):
		Entity.__init__(self, rect, surf, mask)
		self.tileSize = tileSize
		if animationInterval != None:
			self.animationTime = animationInterval
		#self.pattern = pattern.patternSquare(self)
		#self.pattern = pattern.Pattern3(self)
		#self.bulletPattern = bulletpattern.Pattern2()
		self.lastHitIndex = []

	def update(self, timePassed, target, bulletList):
		self.timePassed+=timePassed
		self.updateMovementPattern()
		bulletList += self.updateBulletPattern(target)
		self.updateRect()
		self.animation()
		self.timePassed = 0

	def updateMovementPattern(self):
		self.movementPattern.update(self.timePassed)
	
	def updateBulletPattern(self, target):
		return self.bulletPattern.update(self, target, self.timePassed)


	def loadEnemy(self, movementpattern, name, bulletpattern, hp):
		self.movementPattern = movementpattern
		self.name = name
		self.bulletPattern = bulletpattern
		self.hp = hp

	#def setType(self, Type):
		#self.Type = Type

	def updateRect(self):
		Entity.updateRect(self)


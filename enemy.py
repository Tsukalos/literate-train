from entity import *
from pygame.math import *
from collections import namedtuple

class Enemy(Entity):
	def __init__(self, rect, surf):
		Entity.__init__(self, rect, surf)
		self.direction = Vector2(0,0)
		self.moveC = 0
		self.movementTimer = 0

	def update(self, timePassed):
		self.timePassed+=timePassed
		self.updateMovement()
		self.updateRect()
		self.animation()
		self.timePassed = 0

	def updateMovement(self):
		self.movementTimer+=self.timePassed
		self.currentMove = self.Type.movements[self.moveC]
		if(self.currentMove.delay > self.movementTimer):
			self.direction = self.currentMove.direction
		else:
			self.movementTimer = 0
			if(self.moveC == len(self.Type.movements)-1):
				self.moveC = 0
			else:
				self.moveC+=1

	def setType(self, Type):
		self.Type = Type

	def updateRect(self):
		self.direction.normalize_ip()
		self.x += self.direction.x
		self.y += self.direction.y
		Entity.updateRect(self)

class enemyType():
	def __init__(self, data):
		Movement = namedtuple("Movement","direction delay")
		self.movements = []
		self.name = data["name"]
		for a in data['movements']:
			self.movements.append(Movement(direction=Vector2(a['x'],a['y']),delay=a['delay']))

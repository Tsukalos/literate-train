from entity import *
from pygame.math import *
import movement
from collections import namedtuple

class Enemy(Entity):
	def __init__(self, rect, surf):
		Entity.__init__(self, rect, surf)
		self.movement = movement.Line(Vector2(1,1),1.2)

	def update(self, timePassed):
		self.timePassed+=timePassed
		self.updateMovement()
		self.updateRect()
		self.animation()
		self.timePassed = 0

	def updateMovement(self):
		self.movement.update(self.x, self.y)

	#def setType(self, Type):
		#self.Type = Type

	def updateRect(self):
		if(self.direction != Vector2(0,0)):
			self.direction.normalize_ip()
		Entity.updateRect(self)

class enemyType():
	def __init__(self, data):
		Movement = namedtuple("Movement","direction delay")
		self.movements = []
		self.name = data["name"]
		for a in data['movements']:
			self.movements.append(Movement(direction=Vector2(a['x'],a['y']),delay=a['delay']))

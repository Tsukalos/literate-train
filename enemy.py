from entity import *
from pygame.math import *
from collections import namedtuple

class Enemy(Entity):
	def __init__(self, rect, surf):
		Entity.__init__(self, rect, surf)

	def update(self, timePassed):
		self.updateMovement()
		self.updateRect()
		self.animation(timePassed)
		#self.draw(update_list, screen)

	def updateMovement(self):
		pass

	def setType(self, Type):
		self.Type = Type

class enemyType():
	def __init__(self, data):
		Movement = namedtuple("Movement","direction delay")
		self.movements = []
		self.name = data["name"]
		for a in data['movements']:
			self.movements.append(Movement(direction=Vector2(a['x'],a['y']),delay=a['delay']))

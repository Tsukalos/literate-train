from pygame.math import *

class Line():
	def __init__(self, direction, speed):
		self.direction = direction
		self.direction.normalize_ip()
		self.speed = speed
		self.timer = 0
		
	def update(self, entity):
		entity.x += self.direction.x*self.speed
		entity.y += self.direction.y*self.speed
		
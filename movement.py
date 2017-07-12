from pygame.math import *

class Line():
	def __init__(self, direction, speed):
		self.direction = direction
		self.direction.normalize_ip()
		self.speed = speed
		self.timer = 0
		
	def update(self, x, y):
		x += self.direction.x*speed
		y += self.direction.y*speed
		
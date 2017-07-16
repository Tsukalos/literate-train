from pygame.math import *
import math

class Line():
	'''
		direction -> Vector2

		speed -> float speed value
	'''
	def __init__(self, direction, speed):
		self.direction = direction
		self.direction.normalize_ip()
		self.speed = speed
		self.timer = 0
		
	def update(self, entity):
		'''
			entity -> Entity class

			Projects entity into the init direction
		'''
		entity.x += self.direction.x*self.speed
		entity.y += self.direction.y*self.speed
		
class HorizontalSenoid():
	def __init__(self, direction, speed, amp, len):
		self.direction = direction
		self.direction.normalize_ip()
		self.speed = speed
		self.amp = amp
		self.len = len
		self.timer = 0
		
	def update(self, entity):
		self.timer+=1
		entity.x += self.direction.x*self.speed
		entity.y += math.sin(self.timer/60*self.len)*self.amp
		
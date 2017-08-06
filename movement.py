from pygame.math import *
import math
		
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


'''
	TODO remove std Line class
'''
class Line():
	def __init__(self, direction, speed, acc, limitspd):
		self.direction = direction
		self.direction.normalize_ip()
		self.speed = speed
		self.acc = acc
		self.limitspd = limitspd
		self.timer = 0

	def update(self, entity):
		if(self.acc != 0):
			self.timer +=1
			self.speed += (self.timer/60)*self.acc/100
			if(self.acc > 0):
				if(self.speed > self.limitspd):
					self.speed = self.limitspd
			else:
				if(self.speed < self.limitspd):
					self.speed = self.limitspd
		entity.x += self.direction.x*self.speed
		entity.y += self.direction.y*self.speed

class Circle1FullTurn():
	def __init__(self, radius, isClockwise, speed):
		self.radius = radius
		self.isClockwise = isClockwise
		self.speed = speed
		self.timer = 0
		self.timePassed = 0
		self.ang = 0

	def update(self, entity):
		#self.timer+=1
		#if self.timePassed >= 100:
		self.ang+=2*math.pi/100
		if self.ang >= round(2*math.pi):
				return False
		entity.x += math.cos(self.ang)*self.radius
		entity.y += math.sin(self.ang)*self.radius
		
		return True
		
	

		
		
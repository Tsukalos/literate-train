from pygame.math import *
import pygame.image
from pygame.rect import *
import movement, bullet

class PatternSpiral4Origin():
	def __init__(self):
		self.timePassed = 0
		self.c = 0
		self.v1 = Vector2(1,0) * 10
		self.v2 = Vector2(-1,0) * 10
		self.v3 = Vector2(0,1) * 10
		self.v4 = Vector2(0,-1) * 10
		self.surf1 = pygame.image.load("data/bullet.png").convert()
		pass

	def update(self, origin, target, timePassed):
		self.timePassed += timePassed
		bulletlist = []
		if self.timePassed % 100 != self.timePassed:
			self.helper(bulletlist, self.v1, origin)
			self.helper(bulletlist, self.v2, origin)
			self.helper(bulletlist, self.v3, origin)
			self.helper(bulletlist, self.v4, origin)
			self.timePassed = 0

        
		return bulletlist

	def helper(self, bulletlist, vet, origin):
		posx = origin.rect.centerx
		posy = origin.rect.centery 
		posx += vet.x
		posy += vet.y
		bulletlist.append(bullet.Bullet(Rect(posx,posy,self.surf1.get_width(),self.surf1.get_height()),self.surf1,movement.Line(Vector2(vet.x, vet.y),0.3,1,6)))
		vet.rotate_ip(10)


class Pattern2():
	def __init__(self):
		self.timePassed = 0
		self.c = 0
		self.vet = Vector2(1,0) * 10
		self.surf1 = pygame.image.load("data/bullet.png").convert()
		pass

	def update(self, origin, target, timePassed):
		self.timePassed += timePassed
		bulletlist = []
		if self.timePassed % 250 != self.timePassed:
			posx = origin.rect.centerx
			posy = origin.rect.centery 
			posx += self.vet.x
			posy += self.vet.y
			for i in range(0,24):
				posx = origin.rect.centerx
				posy = origin.rect.centery 
				posx += self.vet.x
				posy += self.vet.y
				bulletlist.append(bullet.Bullet(Rect(posx,posy,self.surf1.get_width(),self.surf1.get_height()),self.surf1,movement.Line(Vector2(self.vet.x, self.vet.y),0.3,2,6)))
				self.vet.rotate_ip(15)
			self.timePassed = 0

		
		return bulletlist
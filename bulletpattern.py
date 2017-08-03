from pygame.math import *
import pygame.image
from pygame.rect import *
from pygame.mask import *
import pygame.mask
import movement, bullet

class PlayerPattern1():
	def __init__(self):
		self.v = Vector2(0,-1)
		self.surf1 = pygame.image.load("data/pbullet.png").convert_alpha()
		self.surf1.set_colorkey((255,255,255))
		self.mask1 = pygame.mask.from_surface(self.surf1)
		self.damage = 3
		self.timePassed = 0

	def update(self, origin, timepassed):
		self.timePassed += timepassed
		bulletlist = []
		if (self.timePassed >= 20):
			r = Rect(0,0,self.surf1.get_width(),self.surf1.get_height())
			r.center = (origin.rect.centerx+self.v.x,origin.rect.centery+self.v.y)
			bulletlist.append(bullet.Bullet(r,self.surf1,movement.Line(self.v,15,0,10),self.mask1))
			self.timePassed = 0
		return bulletlist
		



class PatternSpiral4Origin():
	def __init__(self):
		self.timePassed = 0
		self.c = 0
		self.v1 = Vector2(1,0) * 40
		self.v2 = Vector2(-1,0) * 40
		self.v3 = Vector2(0,1) * 40
		self.v4 = Vector2(0,-1) * 40
		self.surf1 = pygame.image.load("data/bullet.png").convert()
		self.surf1.set_colorkey((255,255,255))
		self.mask1 = pygame.mask.from_surface(self.surf1)
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
		r = Rect(posx,posy,self.surf1.get_width(),self.surf1.get_height())
		r.center = (posx,posy)
		bulletlist.append(bullet.Bullet(r,self.surf1,movement.Line(Vector2(vet.x, vet.y),5,-10,1),self.mask1))
		vet.rotate_ip(10)


class Pattern2():
	def __init__(self):
		self.timePassed = 0
		self.c = 0
		self.vet = Vector2(1,0) * 10
		self.surf1 = pygame.image.load("data/bullet.png").convert()
		self.surf1.set_colorkey((255,255,255))
		self.mask1 = pygame.mask.from_surface(self.surf1)
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
				r = Rect(posx,posy,self.surf1.get_width(),self.surf1.get_height())
				r.center = (posx, posy)
				bulletlist.append(bullet.Bullet(r,self.surf1,movement.Line(Vector2(self.vet.x, self.vet.y),0.6,4,6),self.mask1))
				self.vet.rotate_ip(15)
			self.timePassed = 0

		
		return bulletlist

class Pattern3():
	def __init__(self):
		self.timePassed = 0
		self.c = 0
		self.vet = Vector2(1,0) * 10
		self.surf1 = pygame.image.load("data/bullet.png").convert()
		self.surf1.set_colorkey((255,255,255))
		self.mask1 = pygame.mask.from_surface(self.surf1)
		pass

	def update(self, origin, target, timePassed):
		self.timePassed += timePassed
		bulletlist = []
		if self.timePassed % 2000 != self.timePassed:
			posx = origin.rect.centerx
			posy = origin.rect.centery 
			posx += self.vet.x
			posy += self.vet.y
			r = Rect(posx,posy,self.surf1.get_width(),self.surf1.get_height())
			r.center = (posx, posy)
			bulletlist.append(bullet.Bullet(r,self.surf1,movement.Line(Vector2(self.vet.x, self.vet.y),0.6,0,6),self.mask1))
			self.timePassed = 0

		
		return bulletlist
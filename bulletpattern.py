from pygame.math import *
import pygame.image
from pygame.rect import *
import movement, bullet

class Pattern1():
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
            bulletlist.append(bullet.Bullet(Rect(posx,posy,self.surf1.get_width(),self.surf1.get_height()),self.surf1,movement.Line(Vector2(self.vet.x, self.vet.y),0.3,1,6)))
            self.vet.rotate_ip(10)
            self.timePassed = 0

        
        return bulletlist
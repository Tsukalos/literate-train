import pygame.image, movementpattern,bulletpattern
from enemy import *
class Type1(Enemy):
    def __init__(self, pos, movementpattern):
        s = pygame.image.load("data/eSprite.png").convert()
        s.set_colorkey((255,255,255))
        Enemy.__init__(
                    self,
                    Rect(pos[0],pos[1],20,20),
                    s, 
                    pygame.mask.from_surface(s),
                    s.get_height(),
                    250
                )
        self.movementpattern = movementpattern
        self.movementpattern.setEntity(self)
        self.loadEnemy(self.movementpattern, "Enemy1", bulletpattern.PatternSpiral4Origin(),50)
    
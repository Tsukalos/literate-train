from entity import *
from pygame.math import *
from collections import namedtuple

class Bullet(Entity):
    def __init__(self,rect,surf,movement, mask):
        Entity.__init__(self,rect,surf, mask)
        self.movement = movement
        self.timePassed = 0

    def update(self):
        self.movement.update(self)
        self.updateRect()

    def draw(self, update_list, screen):
        screen.blit(self.surface, self.rect)
        update_list.append(self.rect.copy())
        


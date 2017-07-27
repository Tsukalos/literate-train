from entity import *
from pygame.math import *
from collections import namedtuple

class Bullet(Entity):
    def __init__(self,rect,surf,movement):
        Entity.__init__(self,rect,surf)
        self.movement = movement
        self.timePassed = 0

    def update(self):
        self.movement.update(self)
        self.updateRect()


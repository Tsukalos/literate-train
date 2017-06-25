from entity import *
from pygame.math import *
from collections import namedtuple

class Bullet(Entity):
    def __init__(self,rect,surf):
        Entity.__init__(self,rect,surf)

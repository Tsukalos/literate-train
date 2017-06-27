from entity import *
from pygame.math import *
from collections import namedtuple
import bulletPatterns

class Bullet(Entity):
    def __init__(self,rect,surf):
        Entity.__init__(self,rect,surf)
        self.timePassed = 0
        self.movementTimer = 0

    def update(self, timePassed, Player):
        self.timePassed += timePassed

        updateMovement(Player)

        self.timePassed = 0

    def updateMovement(self, Player):
        self.movementTimer+=self.timePassed
        #pos = self.Pattern.update(movementTimer, Player)

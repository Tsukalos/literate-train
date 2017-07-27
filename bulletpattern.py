from pygame.math import *
import movement, bullet

class Pattern1():
    def __init__(self):
        self.timePassed = 0
        pass

    def update(self, origin, target, timePassed):
        self.timePassed += timePassed
        bulletlist = []
        return bulletlist
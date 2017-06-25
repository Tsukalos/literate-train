from entity import *
import pygame

class Player(Entity):
    def __init__(self, rect, surf):
        Entity.__init__(self, rect, surf)
        self.firing = False

    def updateRect(self):
        Entity.updateRect(self)

    def update(self, keypress, timePassed):
        self.timePassed+=timePassed
        self.updateMovement(keypress)
        self.updateRect()
        self.animation()
        self.timePassed = 0

    def updateMovement(self, keypress):
        if keypress[K_w]:
            self.y -= 1
        if keypress[K_a]:
            self.x -= 1
        if keypress[K_s]:
            self.y += 1
        if keypress[K_d]:
            self.x += 1

        if keypress[K_z]:
            firing = True
        else:
            firing = False

from entity import *
import pygame

class Player(Entity):
    def __init__(self, rect, surf):
        Entity.__init__(self, rect, surf)

    def updateRect(self):
        Entity.updateRect(self)

    def update(self, keypress, timePassed):
        self.timePassed+=timePassed
        self.updateMovement(keypress)
        self.updateRect()
        self.animation()
        self.timePassed = 0

    def updateMovement(self, keypress):

        if keypress[119]:
            self.y -= 1
        if keypress[97]:
            self.x -= 1
        if keypress[115]:
            self.y += 1
        if keypress[100]:
            self.x += 1

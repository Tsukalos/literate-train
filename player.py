from entity import *
import pygame, bulletpattern

class Player(Entity):
    def __init__(self, rect, surf):
        Entity.__init__(self, rect, surf)
        self.firing = False
        self.name = "Player"
        self.firingpattern = bulletpattern.PlayerPattern1()


    def updateRect(self):
        Entity.updateRect(self)

    def update(self, keypress, timePassed, bulletList):
        self.timePassed+=timePassed
        self.updateMovement(keypress)
        if(self.firing):
            bulletList += self.updateFiring()
        self.updateRect()
        self.animation()
        self.timePassed = 0

    def updateMovement(self, keypress):
        if keypress[K_UP]:
            self.y -= 3
        if keypress[K_LEFT]:
            self.x -= 3
        if keypress[K_DOWN]:
            self.y += 3
        if keypress[K_RIGHT]:
            self.x += 3

        if keypress[K_z]:
            self.firing = True
        else:
            self.firing = False

    def updateFiring(self):
        return self.firingpattern.update(self, self.timePassed)
        pass
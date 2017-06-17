from entity import *
import pygame

class Player(Entity):
    def __init__(self, rect, surf):
        Entity.__init__(self, rect, surf)

    def updateRect(self):
        Entity.updateRect(self)

    def update(self, keypress, update_list, screen, background):
        self.updateMovement(keypress, update_list, screen, background)
        self.updateRect()
        self.draw(update_list, screen)

    def updateMovement(self, keypress, update_list, screen, background):
        Entity.updateMovement(self, update_list, screen, background)
        if keypress[119]:
            self.y -= 1
        if keypress[97]:
            self.x -= 1
        if keypress[115]:
            self.y += 1
        if keypress[100]:
            self.x += 1

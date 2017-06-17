import pygame
from pygame.locals import *
class Entity():
    def __init__(self,rect,surf):
        self.x = rect.x
        self.y = rect.y
        self.rect = rect
        self.surface = surf

    def updateMovement(self, update_list, screen, background):
        screen.blit(background,self.rect,self.rect)
        update_list.append(self.rect.copy())
        return

    def updateAction():
        return

    def updateState():
        return

    def loadType():
        return

    def updateRect(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def update():
        self.updateAction()
        self.updateState()
        self.updateMovement()

    def draw(self,update_list, screen):
        screen.blit(self.surface,self.rect)
        update_list.append(self.rect.copy())

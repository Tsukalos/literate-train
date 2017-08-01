from entity import *
import pygame, bulletpattern

class Player(Entity):
    def __init__(self, rect, surf, mask):
        Entity.__init__(self, rect, surf, mask)
        self.firing = False
        self.hitboxsurface = pygame.image.load("data/hitbox.png")
        self.hitboxsurface.set_colorkey((255,255,255))
        self.mask = pygame.mask.from_surface(self.hitboxsurface)
        self.hitbox = pygame.rect.Rect(0,0,self.hitboxsurface.get_width(),self.hitboxsurface.get_height())
        self.hitbox.center = self.rect.center
        self.name = "Player"
        self.focus = False
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
        if keypress[K_LSHIFT]:
            self.focus = True
            mov = 1
        else:
            self.focus = False
            mov = 3
        if keypress[K_UP]:
            self.y -= mov
        if keypress[K_LEFT]:
            self.x -= mov
        if keypress[K_DOWN]:
            self.y += mov
        if keypress[K_RIGHT]:
            self.x += mov

        if keypress[K_z]:
            self.firing = True
        else:
            self.firing = False

        

    def updateFiring(self):
        return self.firingpattern.update(self, self.timePassed)
        pass
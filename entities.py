import math
from pygame import Rect
from pygame.math import *
class Player():

    def __init__(self):
        self.hitbox = Rect(0,0,0,0)
        self.animation_interval = 150
        self.frameIndex = 0
        self.timePassed = 0.0

    def updateMovement(self, keypress):
        if keypress[119]:
            self.hitbox.y -= 1
        if keypress[97]:
            self.hitbox.x -= 1
        if keypress[115]:
            self.hitbox.y += 1
        if keypress[100]:
            self.hitbox.x += 1


    def Update(self, keypress, timePassed):
        self.updateMovement(keypress)
        self.updateAnimation(timePassed)

    def updateAnimation(self, timePassed):
        self.timePassed += timePassed
        if (self.timePassed > self.animation_interval):
            self.hitbox.w = self.frameIndex+2
            self.frameIndex += 1
            if self.frameIndex > 5:
                self.frameIndex = 0
            self.timePassed = 0.0

class Enemy():
    def __init__(self, rect, direction):
        self.hitbox = rect
        self.direction = direction
        self.speed = 1.2
        self.cooldown = 500
        self.timePassed = 0.0

    def Update(self, enemyBullets, player, timePassed):
        self.updateMovement()
        self.shootBullet(player, timePassed, enemyBullets)

    def setMovement(self, direction):
        direction.normalize_ip()
        self.direction = direction


    def updateMovement(self):
        self.hitbox.x += self.direction.x*self.speed
        self.hitbox.y += self.direction.y*self.speed

    def shootBullet(self, target, timePassed, enemyBullets):
        self.timePassed += timePassed
        if (self.timePassed > self.cooldown):
            borigin = self.hitbox
            enemyBullets.append(Bullet(borigin,target))
            self.timePassed = 0


class Bullet():
    def __init__(self, origin, target):
        self.x = origin.x
        self.y = origin.y
        self.tx = target.hitbox.x
        self.ty = target.hitbox.y
        self.speed = 2
        self.direction = math.atan2((self.ty - self.y ), (self.tx - self.x ))
        self.dirx = math.cos(self.direction)
        self.diry = math.sin(self.direction)

    def Update(self):
        self.x +=self.dirx*self.speed
        self.y +=self.diry*self.speed

from pygame import Rect
class Player():

    def __init__(self):
        self.hitbox = Rect(0,0,0,0)

    def updateMovement(self, keypress):
        if keypress[119]:
            self.hitbox.y -= 1
        if keypress[97]:
            self.hitbox.x -= 1
        if keypress[115]:
            self.hitbox.y += 1
        if keypress[100]:
            self.hitbox.x += 1


    def Update(self, keypress):
        self.updateMovement(keypress)


class Enemy():
    def __init__(self):
        self.hitbox = Rect(0,0,0,0)



    def Update(self):
        pass

class Bullet():
    def __init__(self):
        self.hitbox - Rect(0,0,2,2)

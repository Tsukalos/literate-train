from entity import *
class Enemy(Entity):
    def __init__(self, rect, surf):
        Entity.__init__(self, rect, surf)

    def update(self, update_list, screen, background):
        self.updateMovement(update_list, screen, background)
        self.updateRect()
        self.draw(update_list, screen)

    def updateMovement(self, update_list, screen, background):
        Entity.updateMovement(self, update_list, screen, background)
      
		
class enemyType():
	def __init__(self, name, movements):
		self.name = name
		self.movements = movements

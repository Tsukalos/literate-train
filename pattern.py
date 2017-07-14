from pygame.math import *
import movement

class patternSquare():
	def __init__(self, entity):
		self.timer = 0
		self.entity = entity
		self.movePointer = 0
		self.move_list = [(movement.Line(Vector2(1,1),1.0),1000), (movement.Line(Vector2(1,-1),1.0),1000)]
		pass

	
	
	def update(self, timePassed):
		self.timer+=timePassed
		if(self.timer > self.move_list[self.movePointer][1]):
			self.movePointer+=1
			if(self.movePointer == len(self.move_list)):
				self.movePointer = 0
			self.timer = 0
		self.move_list[self.movePointer][0].update(self.entity)

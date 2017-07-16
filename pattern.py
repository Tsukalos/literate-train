from pygame.math import *
import movement

class Pattern():
	def __init__(self, entity):
		self.timer = 0
		self.entity = entity
		self.movePointer = 0
		self.move_list = []
		
	def update(self, timePassed):
		self.timer+=timePassed
		if(self.timer > self.move_list[self.movePointer][1]):
			self.movePointer+=1
			if(self.movePointer == len(self.move_list)):
				self.movePointer = 0
			self.timer = 0
		self.move_list[self.movePointer][0].update(self.entity)
		
		
class patternSquare(Pattern):
	def __init__(self, entity):
		Pattern.__init__(self, entity)
		self.move_list = [(movement.Line(Vector2(1,1),1.0),1000), (movement.Line(Vector2(1,-1),1.0),1000)]

class Senoid(Pattern):
	def __init__(self, entity):
		Pattern.__init__(self, entity)
		self.move_list = [(movement.HorizontalSenoid(Vector2(1,1),2,1,0.7),3000)]

class Pattern3(Pattern):
	def __init__(self, entity):
		Pattern.__init__(self, entity)
		self.move_list = [(movement.Line(Vector2(1,1),0.3),1000),(movement.Line(Vector2(-1,1),0.72),1000)]

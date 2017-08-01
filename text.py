from pygame import surface, rect
from pygame import freetype
from entity import Entity

class Text(Entity):
    def __init__(self, font):
        surf = surface.Surface((0,0))
        r = rect.Rect(0,0,0,0)
        Entity.__init__(self, r, surf, None)
        self.font = font
        self.txt = ""
    
    def setText(self, txt):
        self.txt = txt

    def setFont(self, font):
        self.font = font

    def update(self, txt, position):
        self.txt = txt
        t = self.font.render(self.txt)
        self.surface = t[0]
        self.surface.convert()
        self.x = position.x
        self.rect.w = t[1].w
        self.y = position.y
        self.rect.h = t[1].h
        self.updateRect()
        
    
    def draw(self, update_list, screen):
        screen.blit(self.surface,self.rect)
        update_list.append(self.rect.copy())

    

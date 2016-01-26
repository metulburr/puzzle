import pygame as pg
from .. import prepare, tools

class ImageDrop:
    def __init__(self, size, pos):
        self.color_full = (255,0,0)
        self.color_empty = (255,255,255)
        self.color = self.color_full
        self.border = 10
        size = list(size)
        size[0], size[1] = size[0]+self.border, size[1]+self.border
        self.size = size
        self.image = pg.Surface(self.size).convert()
        self.image.fill((255,0,255))
        self.image.set_colorkey((255,0,255))
        self.draw_rect()
        self.rect_orig = self.image.get_rect(center=pos)
        self.rect = self.rect_orig.inflate((self.border,self.border))
        self.contains = None
        
    def draw_rect(self):
        pg.draw.rect(self.image, self.color, pg.Rect((0,0),self.size), self.border)
        
    def get_event(self, event, obj):
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            col = self.rect.colliderect(obj.rect)
            if col and not self.contains:
                obj.rect.topleft = self.rect_orig.topleft #position to centers, messed up from inflating
                self.contains = True
                #self.color = self.color_full
            else:
                self.contains = False
                #self.color = self.color_empty
        
    def update(self):
        self.draw_rect()
        
    def render(self, surf):
        surf.blit(self.image, self.rect)
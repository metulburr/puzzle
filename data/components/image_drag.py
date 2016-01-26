import pygame as pg
from .. import prepare, tools

class ImageDrag(object):
    def __init__(self, image, pos=(10,10)):
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.click = False
        self.scale = None
        self.true_pos = list(self.rect.center)
        
    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.check_click(event.pos)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.click = False

    def check_click(self, pos):
        scaled_pos = tools.scaled_pos(pos, self.scale)
        if self.rect.collidepoint(scaled_pos):
            self.click = True
            pg.mouse.get_rel()

    def update(self, screen_rect, pos, scale):
        self.scale = scale
        if self.click:
            self.rect.center = tools.scaled_mouse_rel(self.true_pos, scale)
            if not screen_rect.contains(self.rect):
                self.rect.clamp_ip(screen_rect)
                self.true_pos = list(self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

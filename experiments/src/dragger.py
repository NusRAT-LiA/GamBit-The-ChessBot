import pygame
from const import *

class Dragger:
    def __init__(self):
        self.mouseX, self.mouseY = 0,0
        self.initial_row, self.initial_col = 0,0
        self.piece = None
        self.dragging = False 

    def update_mouse(self,pos):
        self.mouseX, self.mouseY = pos
    
    def save_initial(self, pos):
        self.initial_col = pos[0]//SQSIZE
        self.initial_row = pos[1]//SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False



    def update_blit(self, surface):
        self.piece.set_texture(size = 128)
        texture_or_path = self.piece.texture

        img = pygame.image.load(texture_or_path)
        img_center = (self.mouseX, self.mouseY)

        self.piece.texture_rect = img.get_rect(center = img_center)
        surface.blit(img, self.piece.texture_rect)
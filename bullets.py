import pygame
from settings import BULLET_SPEED

class Bullets(object):
    def __init__(self, position:pygame.Vector2, direction:pygame.Vector2):
        self.position:pygame.Vector2=position
        self.direction:pygame.Vector2=direction
        self.velocity=BULLET_SPEED*self.direction
        self.blast:pygame.Surface=pygame.image.load("Képek/blast.png").convert_alpha()

    def draw(self, screen:pygame.Surface):
        blast_rect:pygame.Rect=self.blast.get_rect(center=self.blast.get_rect(center=self.position).center)
        screen.blit(self.blast, blast_rect)

    def move(self):
        self.position= self.position+self.velocity

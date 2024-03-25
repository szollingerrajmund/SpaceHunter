import pygame
from settings import BULLET_SPEED,UP

class Bullets(object):
    def __init__(self, position:pygame.Vector2,direction:pygame.Vector2):
        self.position:pygame.Vector2=position
        self.direction:pygame.Vector2=direction
        self.velocity=BULLET_SPEED*self.direction
        self.image:pygame.Surface=pygame.image.load("Képek/blast.png").convert_alpha()

    def draw(self, screen:pygame.Surface):
        angle = self.direction.angle_to(UP)
        rotated_image: pygame.Surface = pygame.transform.rotate(self.image, angle)
        rotated_rect: pygame.Rect = rotated_image.get_rect(center=self.image.get_rect(center=self.position).center)
        screen.blit(rotated_image, rotated_rect)

    def move(self):
        self.position= self.position+self.velocity

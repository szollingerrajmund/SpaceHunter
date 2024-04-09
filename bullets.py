import pygame
from settings import BULLET_SPEED


class Bullets(object):
    def __init__(self, position: pygame.Vector2, direction: pygame.Vector2):
        self.position: pygame.Vector2 = pygame.Vector2(position)
        self.direction: pygame.Vector2 = direction
        self.velocity = BULLET_SPEED * self.direction
        self.frame: float = 0
        self.changing: float = 0.8
        self.images: list[pygame.Surface] = []
        self.images.append(pygame.image.load("Képek/Blast/blast-0.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Blast/blast-1.png").convert_alpha())
        self.image: pygame.Surface = self.images[self.frame]

    def update(self, screen: pygame.Surface):
        self.animation()
        self.draw(screen)
        self.move()

    def draw(self, screen: pygame.Surface):
        blast_rect:pygame.Rect=self.image.get_rect(center=self.position)
        screen.blit(self.image, blast_rect)

    def animation(self):
        self.frame += self.changing
        if self.frame >= len(self.images):
            self.frame = 0
        self.image = self.images[int(self.frame)]

    def move(self):
        self.position = self.position + self.velocity

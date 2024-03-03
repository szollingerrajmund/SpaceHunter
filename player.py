import pygame
from settings import MANEUVERABILITY,UP


class Player:
    def __init__(self, x: int, y: int, velocity:pygame.Vector2) -> None:
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(velocity)
        self.direction:pygame.Vector2=pygame.Vector2(UP)
        self.images: list[pygame.Surface] = []
        self.images.append(pygame.image.load("Képek/player-0.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/player-1.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/player-2.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/player-3.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/player-4.png").convert_alpha())
        self.frame: float = 0
        self.changing: float = 0.2
        self.image:pygame.Surface=pygame.transform.scale(self.images[self.frame],(50,50))

    def rotate(self, clockwise:bool=True):
        sign = 1 if clockwise else -1
        angle = MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, screen: pygame.Surface) -> None:
        angle = self.direction.angle_to(UP)
        rotated_surface:pygame.Surface = pygame.transform.rotozoom(self.image, angle, 1.0)
        rotated_surface_size:pygame.Vector2 = pygame.Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        screen.blit(rotated_surface, blit_position)

    def update(self, screen: pygame.Surface) -> None:
        self.animation()
        self.draw(screen)

    def animation(self) -> None:
        self.frame += self.changing
        if self.frame >= len(self.images):
            self.frame = 0
        self.image = self.images[int(self.frame)]

    def move(self):
        self.position+=self.velocity

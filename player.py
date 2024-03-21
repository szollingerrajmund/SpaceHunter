from ctypes.wintypes import RGB
import pygame
from bullets import Bullets
from settings import MANEUVERABILITY, UP, SPEED, MAX_SPEED


class Player:
    def __init__(self, x: int, y: int, velocity: pygame.Vector2) -> None:
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(velocity)
        self.direction: pygame.Vector2 = pygame.Vector2(UP)
        self.images: list[pygame.Surface] = []
        self.images.append(pygame.image.load("Képek/player-0.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/player-1.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/player-2.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/player-3.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/player-4.png").convert_alpha())
        self.frame: float = 0
        self.changing: float = 0.2
        self.fly: bool = True
        self.standing_image: pygame.Surface = pygame.image.load("Képek/player_stand.png").convert_alpha()
        self.bullet_list:list[Bullets]=[]
        self.blast:Bullets=Bullets(self.position//2, self.direction)
        self.image: pygame.Surface = self.images[self.frame]

    def rotate(self, clockwise: bool = True):
        turn = 1 if clockwise else -1
        angle = MANEUVERABILITY * turn
        self.direction.rotate_ip(angle)

    def draw(self, screen: pygame.Surface):
        angle = self.direction.angle_to(UP)
        rotated_image: pygame.Surface = pygame.transform.rotate(self.image, angle)
        rotated_rect: pygame.Rect = rotated_image.get_rect(
            center=self.image.get_rect(center=self.position).center
        )
        screen.blit(rotated_image, rotated_rect)
        pygame.draw.rect(screen, RGB(0, 0, 255), rotated_rect, 3)

    def update(self, screen: pygame.Surface):
        self.animation()
        self.move()
        self.draw(screen)
        for Bullets in self.bullet_list:
            Bullets.draw(screen)

    def animation(self) -> None:
        if self.fly:
            self.frame += self.changing
            if self.frame >= len(self.images):
                self.frame = 0
            self.image = pygame.transform.scale(
                self.images[int(self.frame)], (100, 100)
            )
        else:
            self.image = pygame.transform.scale(self.standing_image, (100, 100))
        self.fly = False

    def move(self):
        self.position = self.wrap_position(self.position + self.velocity)

    def speed_up(self):
        self.velocity += self.direction * SPEED
        self.velocity = self.velocity.clamp_magnitude(MAX_SPEED)
        self.fly = True

    def wrap_position(self, position: pygame.Vector2):
        x, y = position
        w, h = (1650, 910)
        return pygame.Vector2(x % w, y % h)

    def shoot(self):
        if len(self.bullet_list) < 5:
            self.bullet_list.append(self.blast)

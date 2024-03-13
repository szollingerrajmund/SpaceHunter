from ctypes.wintypes import RGB
import pygame
from settings import HEIGHT, MANEUVERABILITY, UP, SPEED, MAX_SPEED, WIDTH


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
        self.image: pygame.Surface = self.images[self.frame]
        self.out = False

    def rotate(self, clockwise: bool = True):
        turn = 1 if clockwise else -1
        angle = MANEUVERABILITY * turn
        self.direction.rotate_ip(angle)

    def draw(self, screen: pygame.Surface) -> None:
        angle = self.direction.angle_to(UP)
        rotated_image: pygame.Surface = pygame.transform.rotate(self.image, angle)
        rotated_rect: pygame.Rect = rotated_image.get_rect(center=self.image.get_rect(center=self.position).center)
        screen.blit(rotated_image, rotated_rect)
        pygame.draw.rect(screen, RGB(0, 0, 255), rotated_rect, 3)

    def update(self, screen: pygame.Surface) -> None:
        self.animation()
        self.move()
        self.draw(screen)
        self.out_of_screen()

    def animation(self) -> None:
        if self.fly:
            self.frame += self.changing
            if self.frame >= len(self.images):
                self.frame = 0
            self.image = pygame.transform.scale(self.images[int(self.frame)], (100, 100))
        else:
            self.image = pygame.transform.scale(self.standing_image, (100, 100))
        self.fly = False

    def move(self):
        if self.out:
            return
        self.position = self.position + self.velocity


    def speed_up(self):
        self.velocity += self.direction * SPEED
        self.velocity = self.velocity.clamp_magnitude(MAX_SPEED)
        self.fly = True

    def out_of_screen(self):
        if (self.position.x+50 > WIDTH or self.position.x-50 < 0 or self.position.y+50 > HEIGHT or self.position.y-50 < 0):
            self.out = True

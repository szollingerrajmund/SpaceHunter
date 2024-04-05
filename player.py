import pygame
from settings import MANEUVERABILITY, UP, SPEED, MAX_SPEED
from sound import Sound


class Player:
    def __init__(self, x: int, y: int, velocity: pygame.Vector2) -> None:
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(velocity)
        self.direction: pygame.Vector2 = pygame.Vector2(UP)
        self.images: list[pygame.Surface] = []
        self.images.append(pygame.image.load("Képek/Player/player-0.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Player/player-1.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Player/player-2.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Player/player-3.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Player/player-4.png").convert_alpha())
        self.frame: float = 0
        self.changing: float = 0.2
        self.fly: bool = True
        self.standing_image: pygame.Surface = pygame.image.load("Képek/Player/player_stand.png").convert_alpha()
        self.image: pygame.Surface = self.images[self.frame]
        self.soundeffect: Sound = Sound()
        self.engine=self.soundeffect.load_sound("engine")

    def rotate(self, clockwise: bool = True):
        turn = 1 if clockwise else -1
        angle = MANEUVERABILITY * turn
        self.direction.rotate_ip(angle)

    def reset_rotation(self):
        self.direction = pygame.Vector2(UP)

    def draw(self, screen: pygame.Surface):
        angle = self.direction.angle_to(UP)
        rotated_image: pygame.Surface = pygame.transform.rotate(self.image, angle)
        rotated_rect: pygame.Rect = rotated_image.get_rect(center=self.image.get_rect(center=self.position).center)
        screen.blit(rotated_image, rotated_rect)

    def update(self, screen: pygame.Surface):
        self.animation()
        self.move()
        self.draw(screen)

    def animation(self) -> None:
        if self.fly:
            self.frame += self.changing
            if self.frame >= len(self.images):
                self.frame = 0
            self.image: pygame.Surface = self.images[int(self.frame)]
        else:
            self.image: pygame.Surface = self.standing_image
        self.fly = False

    def move(self):
        self.position = self.wrap_position(self.position + self.velocity)

    def speed_up(self):
        self.velocity += self.direction * SPEED
        self.velocity = self.velocity.clamp_magnitude(MAX_SPEED)
        self.fly = True
        self.engine.play()
        self.engine.set_volume(0.2)

    def wrap_position(self, position: pygame.Vector2):
        x, y = position
        w, h = (1700, 950)
        return pygame.Vector2((x + 70) % w - 70, (y + 70) % h - 70)

    
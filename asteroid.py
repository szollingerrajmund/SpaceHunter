from ctypes.wintypes import RGB
import pygame
import random


class Asteroid(object):
    def __init__(self, x: int, y: int, velocity: float) -> None:
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(velocity)
        self.images: list[pygame.Surface] = []
        self.load_images()
        self.frame: float = 0
        self.hitbox: pygame.Rect = pygame.rect.Rect(0, 0, 200, 200)
        self.changing: float = 0.35
        self.image: pygame.Surface = self.images[int(self.frame)]

    def load_images(self) -> None:
        for i in range(1, 11):
            try:
                image_src = "Képek/Asteroid/{}.png".format(i)
                image = pygame.image.load(image_src).convert_alpha()
                self.images.append(image)
            except Exception as e:
                print("Ez a kép nem tud betölteni: {}, Hiba: {}".format(image_src, e))

    def draw(self, screen: pygame.Surface) -> None:

        blit_position: pygame.Rect = self.image.get_rect(
            center=(self.position[0] - 15, self.position[1] + 10)
        )
        self.hitbox.center = self.position
        screen.blit(self.image, blit_position)
        pygame.draw.rect(screen, RGB(0, 255, 255), self.hitbox, 3)

    def update(self, screen: pygame.Surface) -> None:
        self.animation()
        self.draw(screen)
        self.moving(screen)

    def animation(self) -> None:
        self.frame += self.changing
        if self.frame >= len(self.images):
            self.frame = 0
        self.image = pygame.transform.scale(self.images[int(self.frame)], (300, 300))

    def moving(self, screen: pygame.Surface):
        self.position = self.wrap_position(self.position + self.velocity, screen)

    def wrap_position(self, position: pygame.Vector2, screen: pygame.Surface):
        x, y = position
        w, h = (1700, 950)
        return pygame.Vector2(x % w + 0.05, y % h + 0.05)




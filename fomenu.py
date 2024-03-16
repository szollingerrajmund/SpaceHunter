import pygame
from settings import HEIGHT, WIDTH


class Kezdo:
    def __init__(self, x: int, y: int):
        pygame.init()
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.screen_res: tuple[int, int] = (WIDTH, HEIGHT)
        self.screen: pygame.Surface = pygame.display.set_mode(self.screen_res)
        self.images: list[pygame.Surface] = []
        self.images.append(
            pygame.image.load("Képek/Oldalra/oldalra_1.png").convert_alpha()
        )
        self.images.append(
            pygame.image.load("Képek/Oldalra/oldalra_2.png").convert_alpha()
        )
        self.images.append(
            pygame.image.load("Képek/Oldalra/oldalra_3.png").convert_alpha()
        )
        self.images.append(
            pygame.image.load("Képek/Oldalra/oldalra_4.png").convert_alpha()
        )
        self.frame: float = 0
        self.changing: float = 0.35
        self.image: pygame.Surface = self.images[int(self.frame)]

    def draw(self, screen: pygame.Surface) -> None:
        blit_position = self.image.get_rect(center=self.position)
        screen.blit(self.image, blit_position)

    def update(self) -> None:
        self.animation()
        self.draw(self.screen)

    def animation(self) -> None:
        self.frame += self.changing
        if self.frame >= len(self.images):
            self.frame = 0
        self.image = self.images[int(self.frame)]

    def move(self):
        player_speed = 16
        self.position.x += player_speed

        if self.position.x - 180 > WIDTH:
            return False
        return True

    def draw_background(self):
        background = pygame.image.load("Képek/background.png")
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        self.screen.blit(background, (0, 0))

    def mozog(self):
        animation_running = True

        while animation_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.screen.fill((255, 255, 255))

            self.draw_background()

            animation_running = self.move()

            self.update()

            pygame.display.flip()

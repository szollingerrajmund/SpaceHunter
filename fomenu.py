import pygame
from settings import HEIGHT, WIDTH


class Kezdo:
    def __init__(self, x: int, y: int):
        pygame.init()
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.screen_res: tuple[int, int] = (WIDTH, HEIGHT)
        self.screen: pygame.Surface = pygame.display.set_mode(self.screen_res)
        self.images: list[pygame.Surface] = []
        self.images.append(pygame.image.load("Képek/Oldalra/oldalra_1.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Oldalra/oldalra_2.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Oldalra/oldalra_3.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Oldalra/oldalra_4.png").convert_alpha())
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
        # Update player position to move from left to right
        self.position.x += player_speed

        # Check if the player is out of the window
        if self.position.x - 180 > WIDTH:
            # If out of the window, stop the animation and trigger another action
            return False  # Animation stopped
        return True  # Animation continues

    def draw_background(self):
        background = pygame.image.load("Képek/background.png")
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        self.screen.blit(background, (0, 0))

    def mozog(self):
        # Flag to check if the animation is still running
        animation_running = True

        # Main game loop
        while animation_running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Clear the screen
            self.screen.fill((255, 255, 255))

            # Draw the background
            self.draw_background()

            # Update and move the player
            animation_running = self.move()

            # Update the display
            self.update()

            # Update the display
            pygame.display.flip()

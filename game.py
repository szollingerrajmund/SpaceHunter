import pygame
from settings import HEIGHT, WIDTH, FPS


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen_res: tuple[int, int] = (WIDTH, HEIGHT)
        self.screen:pygame.Surface = pygame.display.set_mode(self.screen_res)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        pygame.display.set_caption("Space Hunters")
        self.run()

    def run(self):
        while True:
            self._input_kezelés()
            self._draw()
            pygame.display.update()
            self.clock.tick(FPS)

    def _input_kezelés(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    def _draw(self):
        Háttérkép = pygame.image.load("Képek/background.png")
        Háttér=pygame.transform.scale(Háttérkép,(WIDTH,HEIGHT))
        self.screen.blit(Háttér,(0,0))
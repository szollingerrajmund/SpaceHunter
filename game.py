import pygame
from settings import HEIGHT, WIDTH
class Game(object):
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))

    def main_loop(self):
        while True:
            self._input_kezelés()
            self._process_game_logic()
            self._rajz()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Hunters")

    def _input_kezelés(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


    def _process_game_logic(self):
        pass


    def _rajz(self):
        self.screen.fill((0, 0, 255))
        pygame.display.flip()
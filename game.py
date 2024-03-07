import pygame
from settings import HEIGHT, WIDTH, FPS
from asteroid import Asteroid
from player import Player
import time
from Menu import Menu


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen_res: tuple[int, int] = (WIDTH, HEIGHT)
        self.screen: pygame.Surface = pygame.display.set_mode(self.screen_res)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.player: Player = Player(
            self.screen_res[0] // 2, self.screen_res[1] // 2, pygame.Vector2(0)
        )
        self.asteroid: Asteroid = Asteroid(800, 600, 10)
        self.game_state = "start_menu"
        self.menu: Menu = Menu()
        pygame.display.set_caption("Space Hunters")
        self.run()

    def run(self):
        while True:
            self._input_kezelés()
            if self.game_state == "start_menu":
                self.menu.start_menu()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.game_state = "game"
                elif keys[pygame.K_s]:
                    self.game_state = "help"

            elif self.game_state == "help":
                self.menu.help_menu()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.game_state = "game"

            elif self.game_state == "game":
                self.game_over = False
                self._draw()
                self.player.update(self.screen)
                self.asteroid.update(self.screen)
                self._time()
                self._points()

            elif self.game_state == "game_over":
                self.menu.game_over_menu()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    self.game_state = "start_menu"
                if keys[pygame.K_k]:
                    quit()

            pygame.display.update()
            self.clock.tick(FPS)

    def _input_kezelés(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                quit()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.rotate(clockwise=True)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.rotate(clockwise=False)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player.speed_up()

    def _draw(self):
        Háttérkép = pygame.image.load("Képek/background.png")
        Háttér = pygame.transform.scale(Háttérkép, (WIDTH, HEIGHT))
        self.screen.blit(Háttér, (0, 0))

    def _time(self):
        game_font = pygame.font.SysFont("Trebuchet", 52)
        if not hasattr(self, "time_start"):
            self.time_start = time.time()
        game_time = str(int(time.time() - self.time_start))
        time_surf = game_font.render("Idő: " + game_time, True, (255, 255, 255))
        time_rect = time_surf.get_rect(topleft=(10, 10))
        self.screen.blit(time_surf, time_rect)

    def _points(self):
        score = 0
        score_increment = 1
        player = pygame.Rect(100, 200, 50, 50)
        obstacle = pygame.Rect(200, 200, 50, 50)
        if player.colliderect(obstacle):
            score += score_increment
        game_font = pygame.font.SysFont("Trebuchet", 52)
        score_text = game_font.render(f"Pontszám: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topleft=(WIDTH - 260, 10))

        self.screen.blit(score_text, score_rect)
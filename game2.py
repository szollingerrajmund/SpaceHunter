import random
import pygame
from pygame.locals import QUIT, K_ESCAPE, K_LEFT, K_UP, K_a, K_w
from settings import HEIGHT, WIDTH, FPS
from asteroid import Asteroid
from player import Player
from ido import Ido
from menuk import Menu
from fomenu import Kezdo

class Game(object):
    def __init__(self):
        pygame.init()

        self.screen_res = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.screen_res)
        self.clock = pygame.time.Clock()
        self.player = Player(self.screen_res[0] // 2, self.screen_res[1] // 2, pygame.Vector2(0))
        self.asteroid = Asteroid(800, 600, 10)

        self.screen_res: tuple[int, int] = (WIDTH, HEIGHT)
        self.screen: pygame.Surface = pygame.display.set_mode(self.screen_res)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.player: Player = Player(
            self.screen_res[0] // 2, self.screen_res[1] // 2, pygame.Vector2(0)   
        )
        self.asteroid_spawn = pygame.USEREVENT + 1
        pygame.time.set_timer(self.asteroid_spawn, 2500)
        self.asteroid_list: list[Asteroid] = [Asteroid(800, 600, 0.3)]

        self.game_state = "start_menu"
        self.menu = Menu()
        self.ido = Ido()
        self.kezdo = Kezdo(0, HEIGHT // 2)
        pygame.display.set_caption("Space Hunters")
        self.run()

    def run(self):
        animation_started = False
        self.menu_started = False

        while True:
            self._input_kezeles()

            if not animation_started:
                self.kezdo.mozog()
                animation_started = True

            if self.game_state == "start_menu" and not self.menu_started:
                self.menu.start_menu()
                self.menu_started = True
            elif self.game_state != "start_menu":
                self.menu_started = False

            if self.game_state == "start_menu":
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    self.game_state = "game"
                elif keys[pygame.K_h]:
                    self.game_state = "help"

            elif self.game_state == "help":
                self.menu.help_menu()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    self.game_state = "game"

            elif self.game_state == "game":
                self.game_over = False
                self._draw()
                self.player.update(self.screen)
                for asteroid in self.asteroid_list:
                    asteroid.update(self.screen)
                self.ido.time()
                self.ido.points()

                player_rect = self.player.image.get_rect(center=self.player.position)
                asteroid_rect = self.asteroid.image.get_rect(center=self.asteroid.position)
                if player_rect.colliderect(asteroid_rect):
                    self.game_state = "game_over"
                    self.player.velocity = pygame.Vector2(0, 0)

                elif self.game_state == "game":
                    self.game_over = False
                    self._draw()
                    self.player.update(self.screen)
                    for asteroid in self.asteroid_list:
                        asteroid.update(self.screen)
                        player_rect = self.player.image.get_rect(center=self.player.position)
                        asteroid_rect = asteroid.image.get_rect(center=asteroid.position)
                        if player_rect.colliderect(asteroid_rect):
                            self.game_state = "game_over"
                            self.player.velocity = pygame.Vector2(0, 0)

            elif self.game_state == "game_over":
                self.menu.game_over_menu()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    self.player.position = pygame.Vector2(self.screen_res[0] // 2, self.screen_res[1] // 2)
                    self.asteroid.position = pygame.Vector2(800, 600)
                    self.player.velocity = pygame.Vector2(0, 0)
                    self.player.reset_rotation()
                    self.game_state = "start_menu"
                    self.ido.reset_time()
                if keys[pygame.K_k]:
                    pygame.quit()
                    quit()

            pygame.display.update()
            self.clock.tick(FPS)

    def _input_kezeles(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or keys[K_ESCAPE]:
                pygame.quit()
                quit()

            if event.type == self.asteroid_spawn:
                self.asteroid_list.append(Asteroid(0, 0, random.randint(10, 150)/50))
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.rotate(clockwise=True)
        elif keys[K_LEFT] or keys[K_a]:
            self.player.rotate(clockwise=False)
        if keys[K_UP] or keys[K_w]:
            self.player.speed_up()

    def _draw(self):
        background_image = pygame.image.load("Képek/background.png")
        background = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        self.screen.blit(background, (0, 0))

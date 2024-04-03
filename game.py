import pygame
import random
from settings import HEIGHT, WIDTH
from asteroid import Asteroid
from player import Player
from ido import Ido
from menuk import Menu
from fomenu import Kezdo


class Game(object):
    def __init__(self):
        pygame.init()
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
        self.menu: Menu = Menu()
        self.ido: Ido = Ido()
        
        self.kezdo: Kezdo = Kezdo(0, HEIGHT // 2)
        pygame.display.set_caption("Space Hunters")
        self.run()
        

    def run(self):
        animation_started = False
        self.menu_started = False

        while True:
            self._input_kezelés()

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

            elif self.game_state == "game_over":
                self.menu.game_over_menu()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    self.game_state = "start_menu"
                if keys[pygame.K_k]:
                    quit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass
                elif event.type == self.asteroid_spawn:
                    self.spawn_asteroids()
            

    def spawn_asteroids(self):
        rand_x = random.randint(0, WIDTH + 200)
        rand_y = random.randint(0, HEIGHT + 200)
        velocity = random.randint(1, 2)
        asteroid = Asteroid(rand_x, rand_y, velocity)
        self.asteroid_list.append(asteroid)
        pygame.display.update()

    def _input_kezelés(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                quit()
            if event.type == self.asteroid_spawn:
                self.asteroid_list.append(Asteroid(0, 0, random.randint(10, 150)/50))
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.rotate(clockwise=True)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.rotate(clockwise=False)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player.speed_up()

    def _draw(self):
        Háttérkép = pygame.image.load("Képek/background.png")
        Háttér = pygame.transform.scale(Háttérkép, (WIDTH, HEIGHT))
        self.screen.blit(Háttér, (0, 0))

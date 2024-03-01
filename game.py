import pygame
from settings import HEIGHT, WIDTH, FPS
from asteroid import Asteroid
from player import Player
import time

class Game(object):
    def __init__(self):
        pygame.init()
        self.screen_res: tuple[int, int] = (WIDTH, HEIGHT)
        self.screen:pygame.Surface = pygame.display.set_mode(self.screen_res)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.player:Player=Player(self.screen_res[0] // 2, self.screen_res[1] // 2,0)
        self.asteroid:Asteroid = Asteroid(800, 600, 10)
        pygame.display.set_caption("Space Hunters")
        self.run()

    def run(self):
        while True:
            self._input_kezelés()
            self._kezdőképernyő()
            self._draw()
            self.player.draw(self.screen)
            self.player.update(self.screen)
            self.asteroid.draw(self.screen)
            self.asteroid.update(self.screen)
            self._idő()
            self._pontszámláló()
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

    def _idő(self):
        game_font = pygame.font.SysFont("Trebuchet", 52)
        if not hasattr(self, "time_start"):
            self.time_start = time.time()
        game_time = str(int(time.time() - self.time_start))
        time_surf = game_font.render("Idő: " + game_time, True, (255, 255, 255))
        time_rect = time_surf.get_rect(topleft=(10, 10))
        self.screen.blit(time_surf, time_rect)

    def _pontszámláló(self):
        score = 0
        score_increment = 1
        player = pygame.Rect(100, 200, 50, 50)
        obstacle = pygame.Rect(200, 200, 50, 50)
        if player.colliderect(obstacle):
            score += score_increment
        game_font = pygame.font.SysFont("Trebuchet", 52)
        score_text = game_font.render(f'Pontszám: {score}', True, (255, 255, 255))
        score_rect = score_text.get_rect(topleft=(WIDTH - 260, 10))
        
        self.screen.blit(score_text, score_rect)

    def _kezdőképernyő(self):
        game_state = "start_menu"

        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont('Trebuchet', 66)
        title = font.render('Space Hunter', True, (255, 255, 255))
        start_button = font.render('Start', True, (255, 255, 255))
        self.screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))
        self.screen.blit(start_button, (WIDTH/2 - start_button.get_width()/2, HEIGHT/2 + start_button.get_height()/2))

        while True: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            if game_state == "start_menu":
                draw_start_menu()

            if game_state != "start_menu":
                keys = pygame.key.get_pressed()
                # rest of the code

    def _draw_start_menu(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('My Game', True, (255, 255, 255))
        start_button = font.render('Start', True, (255, 255, 255))
        self.screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))
        self.screen.blit(start_button, (WIDTH/2 - start_button.get_width()/2, HEIGHT/2 + start_button.get_height()/2))
        pygame.display.update()

    def _draw_game_over_screen(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('Game Over', True, (255, 255, 255))
        restart_button = font.render('R - Restart', True, (255, 255, 255))
        quit_button = font.render('Q - Quit', True, (255, 255, 255))
        self.screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/3))
        self.screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/1.9 + restart_button.get_height()))
        self.screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
        pygame.display.update()
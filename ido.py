import time
import pygame
from settings import HEIGHT, WIDTH


class Ido(object):
    def __init__(self):
        self.time_start = None
        pygame.init()
        self.screen_res: tuple[int, int] = (WIDTH, HEIGHT)
        self.screen: pygame.Surface = pygame.display.set_mode(self.screen_res)
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_RETURN]:
        #     if not hasattr(self, "time_start"):
        #         self.time_start = time.time()

    def time(self):
        if self.time_start is None:
            self.time_start = time.time()

        game_font = pygame.font.Font("Romulus.ttf", 52)
        game_time = str(int(time.time() - self.time_start))
        time_surf = game_font.render("Idő: " + game_time + "mp", True, (255, 255, 255))
        time_rect = time_surf.get_rect(topleft=(10, 10))
        self.screen.blit(time_surf, time_rect)

    def reset_time(self):
        self.time_start = None

    def points(self):
        score = 0
        score_increment = 1
        player = pygame.Rect(100, 200, 50, 50)
        obstacle = pygame.Rect(200, 200, 50, 50)
        if player.colliderect(obstacle):
            score += score_increment
        game_font = pygame.font.Font("Romulus.ttf", 52)
        score_text = game_font.render(f"Pontszám: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topleft=(WIDTH - 260, 10))
        self.screen.blit(score_text, score_rect)

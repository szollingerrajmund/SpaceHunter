import time
import pygame
from settings import WIDTH


class Time:
    def __init__(self, screen: pygame.Surface):
        self.screen: pygame.Surface = screen
        self.time_start = time.time()
        self.score: int = 0

    def update(self):
        self.time()
        self.points()

    def time(self):
        if self.time_start is None:
            self.time_start = time.time()
        game_font = pygame.font.Font("Romulus.ttf", 52)
        game_time = str(int(time.time() - self.time_start))
        time_surf = game_font.render("Time: " + game_time + "seconds", True, (255, 255, 255))
        time_rect = time_surf.get_rect(topleft=(10, 10))
        self.screen.blit(time_surf, time_rect)

    def reset_time(self):
        self.time_start = None

    def points(self):
        game_font = pygame.font.Font("Romulus.ttf", 52)
        score_text = game_font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topleft=(WIDTH - 300, 10))
        self.screen.blit(score_text, score_rect)

    def get_points(self):
        self.score += 10

import time
import pygame

pygame.init()
clock = pygame.time.Clock()

    #idő számlálás
game_time = str(int(time.time() - time_start))
time_surf = game_font.render('Idő: ' + game_time, True, fehér)
time_rect = time_surf.get_rect(topleft=(10,10))

screen.blit(time_surf, time_rect)

pygame.display.update()
clock.tick(60)
pygame.quit()
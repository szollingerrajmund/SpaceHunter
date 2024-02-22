import pygame
from settings import HEIGHT, WIDTH , FPS
class Game(object):

    pygame.init()
    Háttérkép = pygame.image.load("Képek/background.png")
    Háttér=pygame.transform.scale(Háttérkép,(WIDTH,HEIGHT))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
  
        screen.blit(Háttér,(0,0))
        pygame.display.update()
        clock.tick(FPS)
  
    pygame.quit()
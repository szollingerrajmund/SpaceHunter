import pygame
class Asteroid(object):

    pygame.init()

    ast1 = pygame.image.load("1.png").convert_alpha
    ast2 = pygame.image.load("2.png").convert_alpha
    ast3 = pygame.image.load("3.png").convert_alpha
    ast4 = pygame.image.load("4.png").convert_alpha
    ast5 = pygame.image.load("5.png").convert_alpha
    ast6 = pygame.image.load("6.png").convert_alpha
    ast7 = pygame.image.load("7.png").convert_alpha
    ast8 = pygame.image.load("8.png").convert_alpha

    asteroid = [ast1,ast2,ast3,ast4,ast5,ast6,ast7,ast8]
    asteroid_index = 0
    asteroid_rect = asteroid[asteroid_index].get_rect(midleft =(240, 160))


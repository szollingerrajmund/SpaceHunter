import pygame
class Asteroid(object):
    def __init__(self,x: int, y: int, velocity: float) -> None:
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(velocity)
        self.images: list[pygame.Surface] = []
        self.images.append(pygame.image.load("Képek/Asteroid/1.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Asteroid/2.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Asteroid/3.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Asteroid/4.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Asteroid/5.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Asteroid/6.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Asteroid/7.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Asteroid/8.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Asteroid/9.png").convert_alpha())
        self.images.append(pygame.image.load("Képek/Asteroid/10.png").convert_alpha())
        self.frame:float= 0
        self.changing: float = 0.25
        self.image: pygame.Surface = self.images[self.frame]


    def draw(self, screen: pygame.Surface)-> None:
        blit_position = self.image.get_rect(center = self.position)
        screen.blit(self.image, blit_position)
    
    def update(self, screen:pygame.Surface)-> None:
        self.animation()
        self.draw(screen)

    def animation(self)->None:
        self.frame+=self.changing
        if self.frame>=len(self.images):
            self.frame=0
        self.image=self.images[int(self.frame)]

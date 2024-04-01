import pygame

class Sound:
    def __init__(self):
        pygame.mixer.init()
    
    def load_sound(self,name:str):
        path=f"Hangok/{name}.wav"
        return pygame.mixer.Sound(path)
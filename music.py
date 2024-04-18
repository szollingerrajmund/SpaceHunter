import pygame


class Sound:
    def __init__(self):
        pygame.mixer.init()

    def load_sound(self, name: str):
        path = f"Music/{name}.mp3"
        return pygame.mixer.Sound(path)

    def music(self):
        pygame.mixer.music.load("Music/bg_music.mp3")
        pygame.mixer.music.set_volume(0.2)
        return pygame.mixer.music.play(-1)

import pygame
from settings import HEIGHT, WIDTH

class Menu(object):
    def __init__(self):
        pygame.init()
        self.screen_res: tuple[int, int] = (WIDTH, HEIGHT)
        self.screen: pygame.Surface = pygame.display.set_mode(self.screen_res)

    def start_menu(self):
        Háttérkép = pygame.image.load("Képek/background.png")
        Háttér = pygame.transform.scale(Háttérkép, (WIDTH, HEIGHT))
        self.screen.blit(Háttér, (0, 0))
        font = pygame.font.SysFont("Trebuchet", 186)
        font2 = pygame.font.SysFont("Trebuchet", 50)
        title = font.render("Space Hunter", True, (255, 255, 255))
        start_button = font2.render(
            "Nyomd meg az ENTER-t a játék elindításához", True, (255, 255, 255)
        )
        help_button = font2.render("H - Segítség", True, (255, 255, 255))
        self.screen.blit(
            title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height())
        )
        self.screen.blit(
            start_button,
            (
                WIDTH / 2 - start_button.get_width() / 2,
                HEIGHT / 2 + start_button.get_height() / 2,
            ),
        )
        self.screen.blit(
            help_button,
            (
                WIDTH / 2 - help_button.get_width() / 2,
                HEIGHT / 2 + help_button.get_height() * 2,
            ),
        )
        pygame.display.update()

    def help_menu(self):
        Háttérkép = pygame.image.load("Képek/background.png")
        Háttér = pygame.transform.scale(Háttérkép, (WIDTH, HEIGHT))
        self.screen.blit(Háttér, (0, 0))
        font = pygame.font.SysFont("Trebuchet", 120)
        font2 = pygame.font.SysFont("Trebuchet", 50)
        font3 = pygame.font.SysFont("Trebuchet", 54)
        title = font.render("Segítség a játékhoz", True, (255, 255, 255))
        # Átírni a szöveget a lentben!!!!
        restart_button = font2.render("R - Újra", True, (255, 255, 255))
        quit_button = font3.render(
            "Nyomd meg az ENTER-t a játék elindításához", True, (255, 255, 255)
        )
        self.screen.blit(
            title,
            (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() * 4),
        )
        self.screen.blit(
            restart_button,
            (
                WIDTH / 2 - restart_button.get_width() / 2,
                HEIGHT / 2 - restart_button.get_height(),
            ),
        )
        self.screen.blit(
            quit_button,
            (
                WIDTH / 2 - quit_button.get_width() / 2,
                HEIGHT / 2 + quit_button.get_height() * 8,
            ),
        )
        pygame.display.update()

    def game_over_menu(self):
        Háttérkép = pygame.image.load("Képek/background.png")
        Háttér = pygame.transform.scale(Háttérkép, (WIDTH, HEIGHT))
        self.screen.blit(Háttér, (0, 0))
        font = pygame.font.SysFont("Trebuchet", 130)
        font2 = pygame.font.SysFont("Trebuchet", 90)
        title = font.render("Játék Vége", True, (255, 255, 255))
        restart_button = font2.render("R - Újra", True, (255, 255, 255))
        quit_button = font2.render("K - Kilépés", True, (255, 255, 255))
        self.screen.blit(
            title,
            (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() * 4),
        )
        self.screen.blit(
            restart_button,
            (
                WIDTH / 2 - restart_button.get_width() / 2,
                HEIGHT / 2 - restart_button.get_height(),
            ),
        )
        self.screen.blit(
            quit_button,
            (
                WIDTH / 2 - quit_button.get_width() / 2,
                HEIGHT / 2 + quit_button.get_height() / 5,
            ),
        )
        pygame.display.update()
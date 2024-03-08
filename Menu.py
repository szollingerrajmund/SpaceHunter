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
        font = pygame.font.SysFont("Trebuchet", 110)
        font2 = pygame.font.SysFont("Trebuchet", 46)
        font3 = pygame.font.SysFont("Trebuchet", 54)
        title = font.render("Segítség a játékhoz", True, (255, 255, 255))
        # Átírni a szöveget a lentben!!!!
        describe_game = font2.render(
            "A különböző nyilakkal mozoghatsz", True, (255, 255, 255)
        )
        start_button = font3.render(
            "Nyomd meg az ENTER-t a játék elindításához", True, (255, 255, 255)
        )
        self.screen.blit(
            title,
            (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() * 5),
        )
        self.screen.blit(
            describe_game,
            (
                WIDTH / 2 - describe_game.get_width() / 2,
                HEIGHT / 2 - describe_game.get_height() * 7,
            ),
        )
        self.screen.blit(
            start_button,
            (
                WIDTH / 2 - start_button.get_width() / 2,
                HEIGHT / 2 + start_button.get_height() * 9,
            ),
        )
        pygame.display.update()

    def game_over_menu(self):
        Háttérkép = pygame.image.load("Képek/background.png")
        Háttér = pygame.transform.scale(Háttérkép, (WIDTH, HEIGHT))
        self.screen.blit(Háttér, (0, 0))
        font = pygame.font.SysFont("Trebuchet", 130)
        font2 = pygame.font.SysFont("Trebuchet", 80)
        font3 = pygame.font.SysFont("Trebuchet", 60)
        title = font.render("Játék Vége", True, (255, 255, 255))
        restart_button = font2.render("R - Újra", True, (255, 255, 255))
        quit_button = font2.render("K - Kilépés", True, (255, 255, 255))
        makers = font2.render("Készítők:", True, (255, 255, 255))
        maker1 = font3.render("Major Bálint István", True, (255, 255, 255))
        maker2 = font3.render("Szollinger Rajmund", True, (255, 255, 255))
        maker3 = font3.render("Baracskai Dóra", True, (255, 255, 255))
        self.screen.blit(
            title,
            (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() * 4),
        )
        self.screen.blit(
            restart_button,
            (
                WIDTH / 2 - restart_button.get_width() / 2,
                HEIGHT / 2 - restart_button.get_height() * 3,
            ),
        )
        self.screen.blit(
            quit_button,
            (
                WIDTH / 2 - quit_button.get_width() / 2,
                HEIGHT / 2 - quit_button.get_height() * 2,
            ),
        )

        self.screen.blit(
            makers,
            (
                WIDTH / 2 - makers.get_width() / 2,
                HEIGHT / 2 + makers.get_height() * 2,
            ),
        )
        self.screen.blit(
            maker1,
            (
                WIDTH / 2 - maker1.get_width() / 2,
                HEIGHT / 2 + maker1.get_height() * 4.5,
            ),
        )
        self.screen.blit(
            maker2,
            (
                WIDTH / 2 - maker2.get_width() / 2,
                HEIGHT / 2 + maker2.get_height() * 6,
            ),
        )
        self.screen.blit(
            maker3,
            (
                WIDTH / 2 - maker3.get_width() / 2,
                HEIGHT / 2 + maker3.get_height() * 8,
            ),
        )
        pygame.display.update()

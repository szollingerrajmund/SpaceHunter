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

        # Create a copy of the background with alpha channel
        background_with_alpha = Háttér.convert_alpha()

        # Text rendering
        font = pygame.font.SysFont("Trebuchet", 186)
        font2 = pygame.font.SysFont("Trebuchet", 50)
        title = font.render("Space Hunter", True, (255, 255, 255))
        start_button = font2.render(
            "Nyomd meg az ENTER-t a játék elindításához", True, (255, 255, 255)
        )
        help_button = font2.render("H - Segítség", True, (255, 255, 255))

        # Gradually increase the visibility of texts
        for alpha in range(0, 256):
            # Display the background
            self.screen.blit(background_with_alpha, (0, 0))

            # Blit texts with varying alpha values
            title_with_alpha = title.copy()
            title_with_alpha.set_alpha(alpha)
            start_button_with_alpha = start_button.copy()
            start_button_with_alpha.set_alpha(alpha)
            help_button_with_alpha = help_button.copy()
            help_button_with_alpha.set_alpha(alpha)

            # Blit texts to the screen
            self.screen.blit(
                title_with_alpha,
                (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height()),
            )
            self.screen.blit(
                start_button_with_alpha,
                (
                    WIDTH / 2 - start_button.get_width() / 2,
                    HEIGHT / 2 + start_button.get_height() / 2,
                ),
            )
            self.screen.blit(
                help_button_with_alpha,
                (
                    WIDTH / 2 - help_button.get_width() / 2,
                    HEIGHT / 2 + help_button.get_height() * 2,
                ),
            )

            # Update display
            pygame.display.update()
            # Add a delay for smooth transition

        # Display fully opaque texts
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
        fel_nyil = font2.render("A fel nyillal mehetsz előre", True, (255, 255, 255))
        oldal_nyil = font2.render(
            "A ballra nyillal balra, a jobbra nyillal jobbra fordulhatsz",
            True,
            (255, 255, 255),
        )
        speed = font2.render("DE a sebességgel nagyon vigyázz!", True, (255, 255, 255))
        describe = font2.render(
            "Éld túl a legtovább az aszteroidák kikerülésével",
            True,
            (255, 255, 255),
        )
        describe2 = font2.render(
            "és lődd szét a legtöbbet, hogy te legyél a galaxis megmentője!",
            True,
            (255, 255, 255),
        )
        start_button = font3.render(
            "Nyomd meg az ENTER-t a játék elindításához", True, (255, 255, 255)
        )

        self.screen.blit(
            title,
            (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() * 5),
        )

        self.screen.blit(
            fel_nyil,
            (
                WIDTH / 2 - fel_nyil.get_width() / 2,
                HEIGHT / 2 - fel_nyil.get_height() * 8,
            ),
        )

        self.screen.blit(
            oldal_nyil,
            (
                WIDTH / 2 - oldal_nyil.get_width() / 2,
                HEIGHT / 2 - oldal_nyil.get_height() * 6.5,
            ),
        )

        self.screen.blit(
            speed,
            (
                WIDTH / 2 - speed.get_width() / 2,
                HEIGHT / 2 - speed.get_height() * 5,
            ),
        )

        self.screen.blit(
            describe,
            (
                WIDTH / 2 - describe.get_width() / 2,
                HEIGHT / 2 + describe.get_height() * 6,
            ),
        )

        self.screen.blit(
            describe2,
            (
                WIDTH / 2 - describe2.get_width() / 2,
                HEIGHT / 2 + describe2.get_height() * 8.5,
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
        font = pygame.font.SysFont("Trebuchet", 140)
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
            (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() * 3.8),
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

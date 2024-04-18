import pygame
from settings import HEIGHT, WIDTH
from moduls import Time


class Menu:
    def __init__(self):
        self.screen_res: tuple[int, int] = (WIDTH, HEIGHT)
        self.screen: pygame.Surface = pygame.display.set_mode(self.screen_res)
        self.time: Time = Time(self.screen)

    def start_menu(self):
        background_pic = pygame.image.load("IMG/background.png")
        background = pygame.transform.scale(background_pic, (WIDTH, HEIGHT))
        background_with_alpha = background.convert_alpha()
        font = pygame.font.Font("Romulus.ttf", 200)
        font2 = pygame.font.Font("Romulus.ttf", 60)
        title = font.render("Space Hunter", True, (255, 255, 255))
        start_button = font2.render(
            "Nyomd meg az ENTER-t a játék elindításához", True, (255, 255, 255)
        )
        help_button = font2.render("H - Segítség", True, (255, 255, 255))

        for alpha in range(0, 256):
            self.screen.blit(background_with_alpha, (0, 0))

            title_with_alpha = title.copy()
            title_with_alpha.set_alpha(alpha)
            start_button_with_alpha = start_button.copy()
            start_button_with_alpha.set_alpha(alpha)
            help_button_with_alpha = help_button.copy()
            help_button_with_alpha.set_alpha(alpha)

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

            pygame.display.update()

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
        background_pic = pygame.image.load("IMG/background.png")
        background = pygame.transform.scale(background_pic, (WIDTH, HEIGHT))
        self.screen.blit(background, (0, 0))
        font = pygame.font.Font("Romulus.ttf", 110)
        font2 = pygame.font.Font("Romulus.ttf", 50)
        font3 = pygame.font.Font("Romulus.ttf", 65)
        title = font.render("Segítség a játékhoz", True, (255, 255, 255))
        up_arrow = font3.render(
            "A fel nyillal vagy w-vel mehetsz előre", True, (255, 255, 255)
        )
        side_arrow1 = font3.render(
            "A ballra nyillal vagy a-val balra fordulsz,",
            True,
            (255, 255, 255),
        )
        side_arrow2 = font3.render(
            "a jobbra nyillal vagy d-vel jobbra fordulsz",
            True,
            (255, 255, 255),
        )
        bullet = font3.render("a SPACE gombbal tüzelsz", True, (255, 255, 255))
        describe = font2.render(
            "Éld túl a legtovább az aszteroidák kikerülésével és lődd szét a legtöbbet.",
            True,
            (255, 255, 255),
        )
        describe2 = font2.render(
            "Vigyázz, csak 3 lövésed van, ha ütköznek visszakapod őket!",
            True,
            (255, 255, 255),
        )
        start_button = font3.render(
            "Nyomd meg az ENTER-t a játék elindításához", True, (255, 255, 255)
        )

        self.screen.blit(
            title,
            (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() * 4),
        )

        self.screen.blit(
            up_arrow,
            (
                WIDTH / 2 - up_arrow.get_width() / 2,
                HEIGHT / 2 - up_arrow.get_height() * 4.5,
            ),
        )

        self.screen.blit(
            side_arrow1,
            (
                WIDTH / 2 - side_arrow1.get_width() / 2,
                HEIGHT / 2 - side_arrow1.get_height() * 3.5,
            ),
        )

        self.screen.blit(
            side_arrow2,
            (
                WIDTH / 2 - side_arrow2.get_width() / 2,
                HEIGHT / 2 - side_arrow2.get_height() * 2.5,
            ),
        )

        self.screen.blit(
            bullet,
            (
                WIDTH / 2 - bullet.get_width() / 2,
                HEIGHT / 2 - bullet.get_height() * 1.5,
            ),
        )

        self.screen.blit(
            describe,
            (
                WIDTH / 2 - describe.get_width() / 2,
                HEIGHT / 2 + describe.get_height() * 3,
            ),
        )

        self.screen.blit(
            describe2,
            (
                WIDTH / 2 - describe2.get_width() / 2,
                HEIGHT / 2 + describe2.get_height() * 4,
            ),
        )

        self.screen.blit(
            start_button,
            (
                WIDTH / 2 - start_button.get_width() / 2,
                HEIGHT / 2 + start_button.get_height() * 6,
            ),
        )

        pygame.display.update()

    def game_over_menu(self):
        background_pic = pygame.image.load("IMG/background.png")
        background = pygame.transform.scale(background_pic, (WIDTH, HEIGHT))
        self.screen.blit(background, (0, 0))
        font = pygame.font.Font("Romulus.ttf", 135)
        font2 = pygame.font.Font("Romulus.ttf", 80)
        font3 = pygame.font.Font("Romulus.ttf", 60)
        font4 = pygame.font.Font("Romulus.ttf", 90)
        title = font.render("Játék Vége", True, (255, 255, 255))
        restart_button = font2.render("R - Újra", True, (255, 255, 255))
        quit_button = font2.render("K - Kilépés", True, (255, 255, 255))
        makers = font4.render("Készítők:", True, (255, 255, 255))
        maker1 = font3.render("Major Bálint István", True, (255, 255, 255))
        maker2 = font3.render("Szollinger Rajmund", True, (255, 255, 255))
        maker3 = font3.render("Baracskai Dóra", True, (255, 255, 255))
        self.screen.blit(
            title,
            (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() * 3.5),
        )
        self.screen.blit(
            restart_button,
            (
                WIDTH / 2 - restart_button.get_width() / 2,
                HEIGHT / 2 - restart_button.get_height() * 3.8,
            ),
        )
        self.screen.blit(
            quit_button,
            (
                WIDTH / 2 - quit_button.get_width() / 2,
                HEIGHT / 2 - quit_button.get_height() * 2.8,
            ),
        )
        self.screen.blit(
            makers,
            (
                WIDTH / 2 - makers.get_width() / 2,
                HEIGHT / 2 - makers.get_height() * 1.35,
            ),
        )
        self.screen.blit(
            maker1,
            (
                WIDTH / 2 - maker1.get_width() / 2,
                HEIGHT / 2 - maker1.get_height() * 0.4,
            ),
        )
        self.screen.blit(
            maker2,
            (
                WIDTH / 2 - maker2.get_width() / 2,
                HEIGHT / 2 + maker2.get_height() * 0.5,
            ),
        )
        self.screen.blit(
            maker3,
            (
                WIDTH / 2 - maker3.get_width() / 2,
                HEIGHT / 2 + maker3.get_height() * 1.4,
            ),
        )
        pygame.display.update()

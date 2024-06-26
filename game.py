import random
import pygame
from settings import HEIGHT, WIDTH, FPS
from asteroids import Asteroid
from player import Player
from moduls import Time
from menus import Menu
from menu1 import Starter
from music import Sound
from bullets import Bullets


class Game:
    def __init__(self):
        self.screen_res = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.screen_res)
        self.clock = pygame.time.Clock()
        self.player = Player( self.screen_res[0] // 2, self.screen_res[1] // 2, pygame.Vector2(0))
        self.asteroid_spawn = pygame.USEREVENT + 20
        pygame.time.set_timer(self.asteroid_spawn, 2100)
        self.asteroid_list: list[Asteroid] = []
        self.asteroid_x:int=0
        self.asteroid_y:int=0
        self.bullet_list: list[Bullets] = []
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.game_state = "start_menu"
        self.menu: Menu = Menu()
        self.time: Time = Time(self.screen)
        self.starter: Starter = Starter(0, HEIGHT // 2)
        pygame.display.set_caption("Space Hunters")
        self.soundeffect: Sound = Sound()
        self.blast_sound = self.soundeffect.load_sound("blast")
        self.music = Sound().music()
        self.run()

    def run(self):
        animation_started = False
        self.menu_started = False

        while True:
            self._input()

            if not animation_started:
                self.starter.movement()
                animation_started = True

            if self.game_state == "start_menu" and not self.menu_started:
                self.menu.start_menu()
                self.menu_started = True
            elif self.game_state != "start_menu":
                self.menu_started = False

            if self.game_state == "help":
                self.menu.help_menu()

            elif self.game_state == "game":
                self.game_over = False
                self.music = True
                self.draw()
                self.player.update(self.screen)
                for blast in self.bullet_list:
                    blast.update(self.screen)
                for asteroid in self.asteroid_list:
                    asteroid.update(self.screen)
                    player_rect: pygame.Rect = self.player.image.get_rect(center=self.player.position)
                    if player_rect.colliderect(asteroid.hitbox):
                        self.game_state = "game_over"
                        self.player.velocity = pygame.Vector2(0, 0)
                    for blast in self.bullet_list:
                        blast_rect: pygame.Rect = blast.image.get_rect(
                            center=blast.position
                        )
                        if blast_rect.colliderect(asteroid.hitbox):
                            self.asteroid_list.remove(asteroid)
                            self.bullet_list.remove(blast)
                            self.time.get_points()
                self.time.update()

            elif self.game_state == "game_over":
                self.time.get_points()
                self.menu.game_over_menu()
                pygame.mixer.music.stop()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    self.player.position = pygame.Vector2(
                        self.screen_res[0] // 2, self.screen_res[1] // 2
                    )
                    self.asteroid_list = []
                    self.player.velocity = pygame.Vector2(0, 0)
                    self.player.reset_rotation()
                    self.game_state = "start_menu"
                    pygame.mixer.music.play()
                    self.time.reset_time()
                    self.time.score = 0
                if keys[pygame.K_k]:
                    pygame.quit()
                    quit()

            pygame.display.update()
            self.clock.tick(FPS)

    def _input(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.shoot()
            elif event.type == self.asteroid_spawn:
                self.spawn_asteroids()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and self.game_state == "game":
            self.player.rotate(clockwise=True)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a] and self.game_state == "game":
            self.player.rotate(clockwise=False)
        if keys[pygame.K_UP] or keys[pygame.K_w] and self.game_state == "game":
            self.player.speed_up()

        if self.game_state == "start_menu" and keys[pygame.K_RETURN]:
            self.game_state = "game"
        elif self.game_state == "start_menu" and keys[pygame.K_h]:
            self.game_state = "help"
        elif self.game_state == "help" and keys[pygame.K_RETURN]:
            self.game_state = "game"

    def spawn_asteroids(self):
        if self.game_state == "game":
            self._spawn_place()
            velocity = random.randint(1, 2)
            asteroid: Asteroid = Asteroid(self.asteroid_x, self.asteroid_y, velocity)
            self.asteroid_list.append(asteroid)
            pygame.display.update()
        else:
            return None

    def draw(self):
        background_image:pygame.Surface = pygame.image.load("IMG/background.png")
        background = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        self.screen.blit(background, (0, 0))

    def shoot(self):
        if self.game_state == "game":
            blast: Bullets = Bullets(self.player.position, self.player.direction)
            if len(self.bullet_list) < 3:
                self.bullet_list.append(blast)
                self.blast_sound.play()
                self.blast_sound.set_volume(0.2)
            for blast in self.bullet_list:
                if (
                    blast.position.x < 1600
                    and blast.position.x > 0
                    and blast.position.y < 900
                    and blast.position.y > 0
                ):
                    blast.move()
                else:
                    self.bullet_list.remove(blast)

    def _spawn_place(self):
        _side: int = random.randint(1, 2)
        if _side == 1:
            self.asteroid_x, self.asteroid_y = (random.randint(0, WIDTH), 0)
        else:
            self.asteroid_x,self.asteroid_y = (0, random.randint(0, HEIGHT))

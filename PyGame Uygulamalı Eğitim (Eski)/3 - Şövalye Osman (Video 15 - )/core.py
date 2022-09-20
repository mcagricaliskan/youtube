import pygame
import sys
from levels.scripts.alpha import *
sys.path.append("/")


pygame.init()


class Core:
    def __init__(self):
        self.window_width = 1600
        self.window_height = 900
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Şövalye Osman")

        self.level_name = "alpha"
        self.level = Alpha(self.window_width, self.window_height, self.level_name)
        self.level_update()

        self.key = None
        self.mouse = None
        self.game_clock = pygame.time.Clock()

    def draw(self):

        self.level.draw(self.window)
        self.game_clock.tick(60)
        pygame.display.update()

    def level_update(self):

        if self.level_name == "alpha":
            self.level = Alpha(self.window_width, self.window_height, self.level_name)

        self.level_name = None

    def game_loop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_ESCAPE]:
            return "QUIT"

        self.mouse = pygame.mouse.get_pressed()

        self.level_name = self.level.game_loop(self.key, self.mouse)

        if self.level_name is not None:
            self.level_update()

        self.draw()


game = Core()

while True:
    Status = game.game_loop()
    if Status == "QUIT":
        break

pygame.quit()

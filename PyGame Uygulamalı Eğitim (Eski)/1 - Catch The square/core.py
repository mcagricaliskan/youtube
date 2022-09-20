import pygame

pygame.init()


class Core:
    def __init__(self):
        self.window_width = 1280
        self.window_height = 720
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Catch the square")
        self.clock = pygame.time.Clock()

        self.enemy = pygame.image.load("enemy.png")
        self.player = pygame.image.load("player.png")
        self.background = pygame.image.load("background.png")

        self.player_x = 500
        self.player_y = 500

    def draw(self):

        self.window.blit(self.background, (0, 0))
        self.window.blit(self.enemy, (100, 100))
        self.window.blit(self.player, (self.player_x, self.player_y))


        self.clock.tick(60)
        pygame.display.update()

    def game_loop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_ESCAPE]:
            return 0

        if self.key[pygame.K_d]:
            self.player_x += 5
        elif self.key[pygame.K_a]:
            self.player_x -= 5

        self.draw()


game = Core()

while True:
    game_status = game.game_loop()
    if game_status is not None:
        break

pygame.quit()


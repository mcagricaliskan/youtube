import pygame


def get_coin(x, y):
    coin = pygame.image.load("Levels/Materials/coin.png")
    coin = pygame.transform.scale(coin, (60, 60))
    return [coin, x, y, pygame.Rect(x + 18, y + 17, 25, 25)]

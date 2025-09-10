import pygame
import sys

pygame.init()

#size of the windpw
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nibbit")

#img loading
background = pygame.image.load("img/background.png")
happy_bun = pygame.image.load("img/happy_bun.png")
sad_bun = pygame.image.load("img/sad_bun.png")
food_img = pygame.image.load("img/food.png")
food_rect = food_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
bun_rect = happy_bun.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))


# resources.py

import pygame
import sys
from constants import WIDTH, HEIGHT

def load_images():
   #load all imges
    try:
        images = {
            'background': pygame.image.load("img/background.png"),
            'happy_bun': pygame.image.load("img/happy_bun.png"),
            'sad_bun': pygame.image.load("img/sad_bun.png"),
            'food': pygame.image.load("img/food.png")
        }
        return images
    except pygame.error as e:
        print(f"Error loading image: {e}")
        pygame.quit()
        sys.exit()

def load_fonts():
    #load fonts
    return {
        'main': pygame.font.Font(None, 36),
        'small': pygame.font.Font(None, 24)
    }

def create_rects(images):
    return {
        'food': images['food'].get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)),
        'bun': images['happy_bun'].get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    }
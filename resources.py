# resources.py

import pygame
import sys
import os
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


def load_music():
    try:
        music_path = os.path.join("mp3", "iddlebun.mp3")
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # Loop indefinitely
    except pygame.error as e:
        print(f"Error loading music: {e}")
        pygame.quit()
        sys.exit()
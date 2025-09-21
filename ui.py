# ui.py

import pygame
from constants import *

def draw_hud(screen, bun, fonts):
    #draw HUD
    health_bar_rect = pygame.Rect(20, 20, 200, 30)
    pygame.draw.rect(screen, GRAY, health_bar_rect)

    # fill based on health
    health_percentage = bun.get_health_percentage()
    health_fill_width = int((health_percentage / 100) * 198)
    health_fill_rect = pygame.Rect(21, 21, health_fill_width, 28)

    # color changing based on health level
    if health_percentage > 60:
        health_color = GREEN
    elif health_percentage > 30:
        health_color = YELLOW
    else:
        health_color = RED
    
    pygame.draw.rect(screen, health_color, health_fill_rect)

    # border and text 
    pygame.draw.rect(screen, BLACK, health_bar_rect, 2)
    health_text = fonts['main'].render(f"Health: {int(health_percentage)}%", True, BLACK)
    screen.blit(health_text, (25, 25))

    # tutorial instructions
    instructions = [
        "Press F to feed (+20 health)",
        "Press P to play (+20 health)"
    ]

    for i, instruction in enumerate(instructions):
        inst_text = fonts['small'].render(instruction, True, BLACK)
        screen.blit(inst_text, (WIDTH - 250, 20 + i * 24))

def draw_game_over(screen, fonts):
    #draw game over screen
    screen.fill(BLACK)
    game_over_text = fonts['main'].render("Just...why? :c", True, RED)
    restart_text = fonts['small'].render("Press R to Restart or Q to Quit", True, WHITE)
    
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 10))

def draw_game(screen, bun, images, rects, fonts):
    #draw main game screen
    screen.blit(images['background'], (0, 0))
    
    # bun logic
    if bun.happy:
        screen.blit(images['happy_bun'], rects['bun'])
    else:
        screen.blit(images['sad_bun'], rects['bun'])
    
    screen.blit(images['food'], rects['food'])
    draw_hud(screen, bun, fonts)
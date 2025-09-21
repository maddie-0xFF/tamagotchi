
# main.py

import pygame
import sys
from constants import WIDTH, HEIGHT, FPS
from resources import load_images, load_fonts, create_rects
from bun import Bun
from ui import draw_game, draw_game_over
from game_logic import GameLogic

def main():
    # initialize pygame and create window
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Nibbit")
    clock = pygame.time.Clock()
    
    # resources loading
    images = load_images()
    fonts = load_fonts()
    rects = create_rects(images)
    
    # bun object and game logic
    bun = Bun()
    game_logic = GameLogic(bun)
    
    # main loop
    running = True
    while running:
        delta_time = clock.tick(FPS)
        
        # EVENT management
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if game_logic.is_playing():
                game_logic.handle_playing_events(event)
            elif game_logic.is_game_over():
                running = game_logic.handle_game_over_events(event)
        
        game_logic.update(delta_time)
        
        # draw everything
        if game_logic.is_playing():
            draw_game(screen, bun, images, rects, fonts)
        elif game_logic.is_game_over():
            draw_game_over(screen, fonts)
        
        pygame.display.flip()
    
    # cleanuuup  
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
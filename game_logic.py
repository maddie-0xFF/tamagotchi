# game_logic.py

import pygame
from constants import FPS

class GameLogic:
  #principal game logic
    
    def _init_(self, bun):
        self.bun = bun
        self.game_status = "playing"
        self.interaction_timer = 0

        #EVENTS 
    def handle_playing_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  
                self.bun.feed()
                self.interaction_timer = 0
            elif event.key == pygame.K_p:  
                self.bun.play()
            elif event.key == pygame.K_r:  # TESTING - delete l8r
                self.bun.health = self.bun.max_health
                self.bun.update_mood()
    
    def handle_game_over_events(self, event):
            if event.key == pygame.K_r:  
                self.bun.reset()
                self.game_status = "playing"
            elif event.key == pygame.K_q:  
                return False
            return True
    
    def update(self, delta_time):
        if self.game_status == "playing":
            self.bun.update_health(delta_time)
            if not self.bun.is_alive():
                print("Just...why? :c")
                self.game_status = "game_over"
    
    def is_playing(self):
        return self.game_status == "playing"
    
    def is_game_over(self):
        return self.game_status == "game_over"
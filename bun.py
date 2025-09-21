# bun.py

from constants import HEALTH_DECAY_TIME, FEED_HEALTH_BOOST, PLAY_HEALTH_BOOST, HAPPY_THRESHOLD

class Bun:
    
    def _init_(self):
        self.max_health = 100
        self.health = self.max_health
        self.happy = True 
        self.health_decay_rate = self.max_health / HEALTH_DECAY_TIME
    
    def feed(self):
        print("¡Yum!")
        self.health = min(self.max_health, self.health + FEED_HEALTH_BOOST)
        self.update_mood()
    
    def play(self):
        print("‹𝟹")
        self.health = min(self.max_health, self.health + PLAY_HEALTH_BOOST)
        self.update_mood()

    def update_health(self, delta_time):
        # decay health over time
        self.health -= self.health_decay_rate * delta_time
        self.health = max(0, self.health)
        self.update_mood()

    def update_mood(self):
       # update happy state based on health
        self.happy = self.health > HAPPY_THRESHOLD
        
    def get_health_percentage(self):
        #returns health as a percentage
        return self.health / self.max_health * 100
    
    def is_alive(self):
        #is it alive?
        return self.health > 0
    
    def reset(self):
        #restart
        self.health = self.max_health
        self.update_mood()
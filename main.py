import pygame
import sys

pygame.init()

#size of the windpw
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nibbit")

# Colors for HUD
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

# Font for HUD
font = pygame.font.Font(None, 36) #define later
small_font = pygame.font.Font(None, 24) #this too

#img loading
background = pygame.image.load("img/background.png")
happy_bun = pygame.image.load("img/happy_bun.png")
sad_bun = pygame.image.load("img/sad_bun.png")
food_img = pygame.image.load("img/food.png")
food_rect = food_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
bun_rect = happy_bun.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

#here I´ll add mp3
# #bacground mp3, sleepy mp3
 
#and here scale the images

#basic emotions AND health system
class Bun:
    def __init__(self):
        self.max.health = 100
        self.health = self
        self.happy = True 
        self.health_decay_rate = 100/(60*60*100)
         # 100 health over 60 seconds
    
    def feed(self):
        print("¡Yum!")
        self.health = min(self.max.health, self.health + 20) 
        #increase health by 1/5, same in the following events
        self.update_mood()
    
    def play(self):
        print("‹𝟹")
        self.health = min(self.max.health, self.health + 20)
        self.update_mood()

    def update_health(self, delta_time):
        self.health -= self.health_decay_rate * delta_time
        self.health = max(0, self.health)
        self.update_mood()

    def update_mood(self):
        if self.health > 30:
           self.happy = True       
        else:
           self.happy = False
        
    #get health to display in hud
    def get_health_porcentage(self):
        return self.health / self.max.health * 100
    
    
    #background health bar
def draw_hud(screen, bun):
        health_bar_rect = pygame.Rect(20, 20, 200, 30)
        pygame.draw.rect(screen, GRAY, health_bar_rect)

    #health fill
        health_percentage = bun.get_health_porcentage()
        health_fill_width = int((health_percentage / 100)*198)
        health_fill_rect = pygame.Rect(21, 21, health_fill_width, 28)

    #color based on health
        if health_percentage > 60:
            health_color = GREEN
        elif health_percentage > 30:
            health_color = YELLOW
        else:
            health_color = RED
        pygame.draw.rect(screen, health_color, health_fill_rect)

        #border of the health bar
        pygame.draw.rect(screen, BLACK, health_bar_rect, 2)
        health_text = font.render(f"Health: {int(health_percentage)}%", True, BLACK)
        screen.blit(health_text, (25, 25))

        #instructions
        instructions = [
        "press F to feed (+20 health)" 
        "press P to play (+20 health)"
        ]

        for i, instruction in enumerate(instructions):
            inst_text = small_font.render(instruction, True, BLACK)
            screen.blit(inst_text, (WIDTH - 250, 20))  

bun = Bun()  

        #principal loop
clock = pygame.time.Clock()
interaction_timer = 0
while True:
    delta_time = clock.get_time() # Time since last frame in milliseconds
    
  #event keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # Feed
                bun.feed()
                interaction_timer = 0  # Reset 
            if event.key == pygame.K_p:  # Play
                bun.play()
            if event.key == pygame.K_r:  # JUST TESTING! DALETE LATER
                bun.health = bun.max.health
                bun.update_mood()


   
    bun.update_health(delta_time)
    if bun.health <= 0:
        print("Just...why? :c ") 
        pass # Game over logic here
        #missing line here hehe

    # Draw everything
    screen.blit(background, (0, 0))
    if bun.happy:
        screen.blit(happy_bun, bun_rect)
    else:
        screen.blit(sad_bun, bun_rect)
    screen.blit(food_img, food_rect)

    #draw hud
    draw_hud(screen, bun)

    pygame.display.flip()
    clock.tick(60)
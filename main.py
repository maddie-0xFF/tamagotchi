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

#here I´ll add mp3
# #bacground mp3, sleepy mp3
 
#and here scale the images

#basic emotions
class Bun:
    def __init__(self):
        self.happy = True 
    
    def feed(self):
        print("¡Yum!")
        self.happy = True
    
    def play(self):
        print("‹𝟹")
        self.happy = True
    
    def neglect(self):
        self.happy = False

bun = Bun()  

        #principal loop
clock = pygame.time.Clock()
interaction_timer = 0
while True:
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
                interaction_timer = 0

   
    interaction_timer += clock.get_time()
    if interaction_timer > 5000:  
        bun.neglect()
        
    # Draw everything
    screen.blit(background, (0, 0))
    if bun.happy:
        screen.blit(happy_bun, bun_rect)
    else:
        screen.blit(sad_bun, bun_rect)
    screen.blit(food_img, food_rect)

    pygame.display.flip()
    clock.tick(60)
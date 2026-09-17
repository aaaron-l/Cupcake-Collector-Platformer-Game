import pygame

# 1. Initialize Pygame
pygame.init()

# 2. Set up the window
HEIGHT = 980
WIDTH = 1820
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cupcake Project") # Added quotes
clock = pygame.time.Clock()

# 3. Game variables
running = True

# Player setup
# Note: Make sure 'player.png' is in the same folder as this script!
player_image = pygame.image.load("player.png").convert_alpha() # Added quotes
player_image = pygame.transform.scale(player_image, (50, 50))
player_x = 50
player_y = 300
player_dy = 0
gravity = 0.5
jump_speed = -10
on_ground = True
player_rect = pygame.Rect(
    player_x,
    player_y,
    50,
    50
)


platforms = [
    pygame.Rect(0, 350, 600, 50),
    pygame.Rect(100, 270, 150, 20),
    pygame.Rect(350, 220, 150, 20)
]


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    keys = pygame.key.get_pressed() 

    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
        
    if keys[pygame.K_UP] and on_ground:
        player_dy = jump_speed
        on_ground = False


    if not on_ground:
        player_dy += gravity
        player_y += player_dy


        #  NEW WORKING PHYSICS
        #  NEW WORKING PHYSICS (Ground kept at 300)
    if player_y >= 300:  
        player_y = 300   # Stops the player exactly at 300
        player_dy = 0    # Stops the falling speed
        on_ground = True # Allows them to jump again



    screen.fill((135, 206, 235)) 
    for platform in platforms:
        pygame.draw.rect(
            screen,
            (100, 180, 100),
            platform
        )

    screen.blit(player_image, (player_x, player_y))
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
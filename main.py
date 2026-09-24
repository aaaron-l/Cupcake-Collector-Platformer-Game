import pygame

pygame.init()

HEIGHT = 980
WIDTH = 1820
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cupcake Project")
clock = pygame.time.Clock()

running = True

player_image = pygame.image.load("player.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (50, 50))

player_x = 1200
player_y = 280
player_dy = 0

gravity = 0.5
jump_speed = -10
on_ground = False

platforms = [
    pygame.Rect(0, 930, WIDTH, 50),
    pygame.Rect(100, 840, 150, 20),
    pygame.Rect(350, 790, 150, 20),
    pygame.Rect(500, 690, 30, 240), # wall
    pygame.Rect(100, 740, 150, 20),
    pygame.Rect(350, 690, 150, 20),
    pygame.Rect(1200, 690, 30, 240),
    pygame.Rect(1230, 690, 500, 20),
    pygame.Rect(1320, 770, 500, 20),
    pygame.Rect(1230, 850, 500, 20),
    pygame.Rect(1770, 600, 50, 20),
    pygame.Rect(1670, 510, 50, 20),
    pygame.Rect(1770, 420, 50, 20),
    pygame.Rect(1200, 330, 520, 20),
    pygame.Rect(0, 330, 530, 20)
]

# Rect, speed, right_lim, left_lim
sliding_hori = [
    (pygame.Rect(530, 690, 100, 20), 5, 1200, 530)
]

# Rect, speed, top_lim, bot_lim
sliding_vert = [
    (pygame.Rect(1000, 330, 100, 20), 3, 130, 330),
    (pygame.Rect(635, 330, 100, 20), 5, 130, 330) 
]

kill_bricks = [

]

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_rect = pygame.Rect(
        player_x,
        player_y,
        50,
        50
    )

    for i, (platform, speed, right_lim, left_lim) in enumerate(sliding_hori):
        old_platform_x = platform.x

        platform.x += speed

        if platform.right >= right_lim:
            platform.right = right_lim
            speed = -abs(speed)

        elif platform.left <= left_lim:
            platform.left = left_lim
            speed = abs(speed)

        platform_dx = platform.x - old_platform_x

        if (
            player_rect.bottom <= platform.top + 5
            and player_rect.bottom >= platform.top - 5
            and player_rect.right > platform.left
            and player_rect.left < platform.right
        ):
            player_x += platform_dx

        sliding_hori[i] = (platform, speed, right_lim, left_lim)

    for i, (platform, speed, top_lim, bot_lim) in enumerate(sliding_vert):
        old_platform_y = platform.y

        platform.y += speed

        if platform.top <= top_lim:
            platform.top = top_lim
            speed = abs(speed)

        elif platform.bottom >= bot_lim:
            platform.bottom = bot_lim
            speed = -abs(speed)

        platform_dy = platform.y - old_platform_y

        if (
            player_rect.bottom <= platform.top + 5
            and player_rect.bottom >= platform.top - 5
            and player_rect.right > platform.left
            and player_rect.left < platform.right
        ):
            player_y += platform_dy

        sliding_vert[i] = (platform, speed, top_lim, bot_lim)

    keys = pygame.key.get_pressed()

    old_x = player_x

    if keys[pygame.K_LEFT]:
        player_x -= 5

    if keys[pygame.K_RIGHT]:
        player_x += 5

    player_rect = pygame.Rect(
        player_x,
        player_y,
        50,
        50
    )

    for platform in platforms:
        if player_rect.colliderect(platform):
            if player_x > old_x:
                player_rect.right = platform.left
                player_x = player_rect.x
            elif player_x < old_x:
                player_rect.left = platform.right
                player_x = player_rect.x

    for platform, speed, right_lim, left_lim in sliding_hori:
        if player_rect.colliderect(platform):
            if player_x > old_x:
                player_rect.right = platform.left
                player_x = player_rect.x
            elif player_x < old_x:
                player_rect.left = platform.right
                player_x = player_rect.x

    if keys[pygame.K_UP] and on_ground:
        player_dy = jump_speed
        on_ground = False

    player_dy += gravity
    player_y += player_dy

    player_rect = pygame.Rect(
        player_x,
        player_y,
        50,
        50
    )

    on_ground = False

    for platform in platforms:

        if player_rect.colliderect(platform):

            if player_dy > 0:
                player_rect.bottom = platform.top
                player_y = player_rect.y
                player_dy = 0
                on_ground = True

            elif player_dy < 0:
                player_rect.top = platform.bottom
                player_y = player_rect.y
                player_dy = 0

    for platform, speed, right_lim, left_lim in sliding_hori:

        if player_rect.colliderect(platform):

            if player_dy > 0:
                player_rect.bottom = platform.top
                player_y = player_rect.y
                player_dy = 0
                on_ground = True

            elif player_dy < 0:
                player_rect.top = platform.bottom
                player_y = player_rect.y
                player_dy = 0

    for platform, speed, top_lim, bot_lim in sliding_vert:

        if player_rect.colliderect(platform):

            if player_dy > 0:
                player_rect.bottom = platform.top
                player_y = player_rect.y
                player_dy = 0
                on_ground = True

            elif player_dy < 0:
                player_rect.top = platform.bottom
                player_y = player_rect.y
                player_dy = 0

    if player_rect.left < 0:
        player_rect.left = 0
        player_x = player_rect.left

    if player_rect.right > WIDTH:
        player_rect.right = WIDTH
        player_x = player_rect.right - 50

    screen.fill((135, 206, 235))

    for platform in platforms:
        pygame.draw.rect(
            screen,
            (100, 180, 100),
            platform
        )

    for platform, speed, right_lim, left_lim in sliding_hori:
        pygame.draw.rect(
            screen,
            (255, 215, 0),
            platform
        )

    for platform, speed, top_lim, bot_lim in sliding_vert:
        pygame.draw.rect(
            screen,
            (255, 215, 0),
            platform
        )

    screen.blit(player_image, (player_x, player_y))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
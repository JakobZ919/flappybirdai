import pygame
import sys

# Initialize Pygame
pygame.init()

# Set display dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class bird():
    bird_x = 100
    bird_y = HEIGHT // 2
    bird_radius = 20
    bird_velocity = 0

# Gravity
gravity = 0.5

# Bird jump strength
jump_strength = -5

# Pipe properties
pipe_width = 50
pipe_height = 300
pipe_x = WIDTH
pipe_y = HEIGHT // 2
score=0
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    # Update bird position
    bird_velocity += gravity #addieren weil oben Null ist
    bird_y += bird_velocity # bird geht nach oben

    # Update pipe position
    pipe_x -= 5#pipe wird nach links verschoben links ist null
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_y = HEIGHT // 2
        score+=1
        print(score)
    # Check for collisions
    if bird_y < 0 or bird_y > HEIGHT:
        bird_y = HEIGHT // 2
        score-=30
    if (bird_y<pipe_y or bird_y>pipe_y+100 )and (pipe_x<bird_x>pipe_x+pipe_width):
        score-=1
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (bird_x, int(bird_y)), bird_radius)
    pygame.draw.rect(screen, BLUE, (pipe_x, pipe_y - pipe_height, pipe_width, pipe_height))
    pygame.draw.rect(screen, BLUE, (pipe_x, pipe_y + 100, pipe_width, HEIGHT - pipe_y - 100))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

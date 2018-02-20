# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Edge Detection"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

    
# Make a block
block =  [375, 275, 50, 50]
vel = [0, 0]
speed = 5


# Select test case
'''
1 = stop on edge
2 = wrap around
'''
case = 2


# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    state = pygame.key.get_pressed()

    up = state[pygame.K_UP]
    down = state[pygame.K_DOWN]
    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]

    if left:
        vel[0] = -speed
    elif right:
        vel[0] = speed
    else:
        vel[0] = 0

    if up:
        vel[1] = -speed
    elif down:
        vel[1] = speed
    else:
        vel[1] = 0
        
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the block '''
    block[0] += vel[0]
    block[1] += vel[1]

    ''' get block edges (makes collision resolution easier to read) '''
    left = block[0]
    right = block[0] + block[2]
    top = block[1]
    bottom = block[1] +block[3]


    if case == 1:
        ''' if the block is moved out of the window, nudge it back on. '''
        if left < 0:
            block[0] = 0
        elif right > WIDTH:
            block[0] = WIDTH - block[2]

        if top < 0:
            block[1] = 0
        elif bottom > HEIGHT:
            block[1] = HEIGHT - block[3]

    
    elif case == 2:
        ''' if the block is moved completely off of the window, reposition it on the other side '''
        if left > WIDTH:
            block[0] = 0 - block[2]
        elif right < 0:
            block[0] = WIDTH
            
        if bottom < 0:
            block[1] = HEIGHT
        elif top > HEIGHT:
            block[1] = 0 - block[3]

    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, block)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()

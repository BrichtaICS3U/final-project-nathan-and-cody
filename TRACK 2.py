# ICS3U
# Assignment 2: Logo
# <your name>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (61, 237, 37)
RED = (255, 0, 0)
GREY =(86, 81, 74)
YELLOW = (250, 255, 0)
# Set the screen size (please don't change this)
SCREENWIDTH = 800
SCREENHEIGHT = 507

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(GREEN)

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, GREEN, [55, 300, 300, 70], 0)

    pygame.draw.ellipse(screen, BLACK, [130, 140, 300, 200], 0)  
    pygame.draw.ellipse(screen, BLACK, [390, 140, 300, 200], 0)
    pygame.draw.ellipse(screen, GREY, [195, 190, 170, 100], 0)
    pygame.draw.ellipse(screen, GREY, [460, 190, 170, 100], 0) 
    pygame.draw.ellipse(screen, WHITE, [170, 165, 220, 150], 1)
    pygame.draw.ellipse(screen, WHITE, [435, 165, 220, 150], 1)
   
     # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()


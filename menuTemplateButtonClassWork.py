
# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
from buttonClass import Button
from carClass import Player
pygame.init()
#pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
#pygame.mixer.music.load('SpongeBob.mp3')#https://www.youtube.com/watch?v=vE2ETqUGj6Q
#pygame.mixer.music.play()
#music_playing = True
#BackGround = pygame.image.load('KRUSTY_KRAB.jpg')#https://twitter.com/krustykrabtw

# Define some colours

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
BLUE = (0,0,200)
BRIGHT_BLUE=(0,0,255)


SCREENWIDTH = 1300
SCREENHEIGHT = 700
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)


        
sound = False
def my_shell_function():
    """A generic function that prints something in the shell"""
    print('Fire the nukes!')

def my_next_function():
    """A function that advances to the next level"""
    global level
    level +=1

def my_settings_function():
    """A function that advances to the next level"""
    global level
    level +=1

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    level -= 1

def my_soundsOn_function():
   # global music_playing
   # if music_playing == False:
   #     pygame.mixer.music.unpause()
  #      music_playing = True
    print('Sounds On')
    
def my_soundsOff_function():
   # global music_playing
   # if music_playing == True:
  #      pygame.mixer.music.pause()
 #       music_playing = False
    print('Sounds Off')
        
def my_hello_function():
    print('Spongebob says "KRABBY PATTIES NEED LOVE TOO!"')

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in level2_buttons:

            if button.rect.collidepoint(pos):
                button.call_back()

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects
button_01 = Button('PLay', (SCREENWIDTH/2, SCREENHEIGHT/4), BRIGHT_GREEN, my_hello_function, GREEN)
button_Settings = Button("Settings", (SCREENWIDTH/2, SCREENHEIGHT/2), BRIGHT_BLUE, my_settings_function, BLUE)
button_02 = Button("Back", (SCREENWIDTH/2, SCREENHEIGHT*2/3), BRIGHT_RED, my_previous_function, RED)
button_03 = Button("Quit", (SCREENWIDTH/2, SCREENHEIGHT*6/7), BRIGHT_RED, my_quit_function, RED)
button_SoundsOn = Button("On", (150, SCREENHEIGHT/2), BRIGHT_GREEN, my_soundsOn_function, GREEN)
button_SoundsOff = Button("Off", (250, SCREENHEIGHT/2), BRIGHT_RED, my_soundsOff_function, RED)


#arrange button groups depending on level
level1_buttons = [button_01, button_03, button_Settings]
level2_buttons = [button_02, button_SoundsOn, button_SoundsOff]

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)

    # --- Game logic goes here

    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Draw buttons
    if level == 1:
        for button in level1_buttons:
            button.draw()
        font = pygame.font.SysFont('centurygothic', 26)
        text = font.render("EXTREME KRABBY PATTY FLIP", 1, (BLACK))
        screen.blit(text, (35, 10))
    elif level == 2:
        #Settings Title
        font = pygame.font.SysFont('centurygothic', 36)
        text = font.render("Settings", 1, (BLACK))
        screen.blit(text, (150, 1))
        #Sound Subtitle
        font = pygame.font.SysFont('centurygothic', 24)
        text = font.render("Sound", 1, (BLACK))
        screen.blit(text, (170, 50))
        for button in level2_buttons:
            button.draw()

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()


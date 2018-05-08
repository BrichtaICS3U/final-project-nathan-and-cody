 # Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys, random
pygame.init()
from buttonClass import Button
#from trackClass import Track
from carClass import Player
BackGround = pygame.image.load('lamborgini-egoista-36475.jpg')


playlist = []
playlist.append ('Dragonball Super - Ultra Instinct Rush (HQ Recreation).mp3')
playlist.append ('Lil Uzi Vert, Quavo & Travis Scott - Go Off (from The Fate of the Furious_ The Album) MUSIC VID.mp3')
playlist.append ('PnB Rock, Kodak Black  A Boogie  Horses (from The Fate of the Furious The Album) [OFFICIAL AUDIO].mp3')
playlist.append ('Darude - Sandstorm.mp30')


Sound = pygame.mixer_music.load(playlist[random.randint(0,3)])



pygame.mixer.music.play()
music_playing = True

# Define some colours

WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
NEON = (70, 255, 191)
VIOLET = (127, 0, 255)
RED = (255, 0, 0)
BLOOD  = (200, 0, 0)
GREEN = (0, 200, 0)
B_GREEN = (0, 255, 0)
PINK = (255, 96, 210)
DGRAY = (45, 45, 45)
YELLOW = (250, 255, 0)
DGREY = (45, 45, 45)


SCREENWIDTH = 800
SCREENHEIGHT = 507

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

colourList = (RED, BLUE, NEON, VIOLET, BLOOD, PINK)

#all_sprites_list = pygame.sprite.Group()
 
#playerPlayer = Player(RED, 60, 80, 70)
#playerPlayer.rect.x = 160
#playerPlayer.rect.y = SCREENHEIGHT - 100

def my_shell_function():
    """A generic function that prints something in the shell"""
    print('Fire the nukes!')

def my_play_function():
   global level
   level +=2

def my_track_function():
    global level
    level -= 2

def my_sound_function():
    print('Sound')

def my_colour_change_function():
    print("Colour Changed")

def my_settings_function():
    """A function that advances to settings shell"""
    global level
    level += 1

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    if level ==2:
        level -= 1
    elif level == 3:
        level -=2

def my_on_function():
   global music_playing
   if music_playing == False:
        pygame.mixer.music.unpause()
        music_playing = True

def my_off_function():
    global music_playing
    if music_playing == True:
        pygame.mixer.music.pause()
        music_playing = False

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def my_change_song_function():
    global sound
    Sound = pygame.mixer_music.load(playlist[random.randint(0,3)])

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
    elif level == 3:
        for button in level3_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects
button_Play = Button("Race", (SCREENWIDTH/2, SCREENHEIGHT/4), GREY,my_play_function, DGREY)
button_Previous = Button("Previous", (SCREENWIDTH/2, SCREENHEIGHT*9/10), GREY, my_previous_function, DGREY)
button_Quit = Button("Quit", (SCREENWIDTH/2, SCREENHEIGHT*3/4), GREY, my_quit_function, DGREY)

button_Settings = Button("Settings", (SCREENWIDTH/2, SCREENHEIGHT/2), GREY, my_settings_function, DGREY)
button_On = Button("ON", (SCREENWIDTH/4, SCREENHEIGHT/6), B_GREEN, my_on_function, GREEN)
button_Off = Button("OFF", (SCREENWIDTH*3/4, SCREENHEIGHT/6), RED, my_off_function, BLOOD)
button_colourRED = Button("RED", (SCREENWIDTH*1/3, SCREENHEIGHT*2/3), GREY, my_colour_change_function, DGREY)
button_songchange = Button("Change Song", (SCREENWIDTH/2, SCREENHEIGHT*6/10), GREY, my_change_song_function, DGREY)

button_trackOne = Button("Track One", (SCREENWIDTH/3, SCREENHEIGHT/2), GREY, my_quit_function, DGREY)
button_trackTwo = Button("Track Two",  (SCREENWIDTH/2, SCREENHEIGHT/2), GREY, my_quit_function, DGREY)
button_trackThree = Button("Track Three",  (SCREENWIDTH*2/3, SCREENHEIGHT/2), GREY, my_quit_function, DGREY)

#arrange button groups depending on level
level1_buttons = [button_Settings, button_Play, button_Quit]
level2_buttons = [button_Previous,button_On, button_Off, button_colourRED, button_songchange]
level3_buttons = [button_trackOne, button_trackTwo, button_trackThree, button_Previous]

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
    screen.blit(BackGround,(0,0))
    # Draw buttons/
    if level == 1:
        for button in level1_buttons:
            button.draw()
        font = pygame.font.SysFont('magneto', 60)
        text = font.render("Top Speed", 1, (WHITE))
        screen.blit(text, (250, 1))
    elif level == 2:
        font = pygame.font.SysFont('magneto', 40)
        text = font.render("Sound", 1, (WHITE))
        screen.blit(text, (330, 1))
        for button in level2_buttons:
            button.draw()
    elif level == 3:
        for button in level3_buttons:
            button.draw()
        font = pygame.font.SysFont('magneto', 40)
        text = font.render("Pick a Track", 1, (WHITE))
        screen.blit(text, (300, 1))
            

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()




 # pygame.draw.rect(screen, GREEN, [55, 300, 300, 70], 0)

  #  pygame.draw.ellipse(screen, BLACK, [100, 110, 600, 300], 0)
   # pygame.draw.ellipse(screen, GREY,[180, 160, 450, 200], 0)

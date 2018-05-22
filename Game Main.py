 # Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys, random
pygame.init()
from buttonClass import Button
#from trackClass import Track
from carClass import Player
BackGround = pygame.image.load('Photos/lamborgini-egoista-36475.jpg')
Road_Atlanta = pygame.image.load('Photos/Road_Atlanta.png')
Oval_Track = pygame.image.load("Photos/Oval_Track.png")
Nurburgring = pygame.image.load('Photos/Nurburgring.png')

playlist = []
playlist.append ('Music/Dragonball Super - Ultra Instinct Rush (HQ Recreation).mp3')
playlist.append ('Music/Lil Uzi Vert Ft. Quavo & Travis Scott- Go Off (Clean) (1).mp3')
playlist.append ('Music/PnB Rock- Horses (Clean).mp3')
playlist.append ('Music/Rick Astley - Never Gonna Give You Up (Video).mp3')
playlist.append ('Music/Darude - Sandstorm.mp3')
playlist.append ('Music/Legend Has It Clean - Run The Jewels.mp3')

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
PINK = (237, 54, 176)
ORANGE = (255, 91, 15)


SCREENWIDTH = 800
SCREENHEIGHT = 507

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

colourList = (RED, BLUE, NEON, VIOLET, BLOOD, PINK, YELLOW)

all_sprites_list = pygame.sprite.Group()
 
player = Player(0)

all_sprites_list.add(player)

def my_play_function():
   global level
   level +=2

def my_track1_function():
    global level
    level += 1
    
def my_track2_function():
    global level
    level += 2

def my_track3_function():
    global level
    level += 3

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
button_songchange = Button("Change Song", (SCREENWIDTH/2, SCREENHEIGHT*2/10), GREY, my_change_song_function, DGREY)

button_colourchange = Button("Colour", (SCREENWIDTH/2, SCREENHEIGHT*5/10), GREY, my_change_song_function, DGREY)
button_colourRED = Button("RED", (SCREENWIDTH*1/6, SCREENHEIGHT*2/3), GREY, my_colour_change_function, DGREY)
button_colourBLUE = Button("BLUE", (SCREENWIDTH*2/6, SCREENHEIGHT*2/3), GREY, my_colour_change_function, DGREY)
button_colourORANGE = Button("ORANGE", (SCREENWIDTH*3/6, SCREENHEIGHT*2/3), GREY, my_colour_change_function, DGREY)
button_colourGREEN = Button("GREEN", (SCREENWIDTH*4/6, SCREENHEIGHT*2/3), GREY, my_colour_change_function, DGREY)
button_colourPINK = Button("PINK", (SCREENWIDTH*5/6, SCREENHEIGHT*2/3), PINK, my_colour_change_function, DGREY)

button_trackOne = Button("Track One", (SCREENWIDTH/3, SCREENHEIGHT/2), GREY, my_track1_function, DGREY)
button_trackTwo = Button("Track Two",  (SCREENWIDTH/2, SCREENHEIGHT/2), GREY, my_track2_function, DGREY)
button_trackThree = Button("Track Three",  (SCREENWIDTH*2/3, SCREENHEIGHT/2), GREY, my_track3_function, DGREY)

#arrange button groups depending on level
level1_buttons = [button_Settings, button_Play, button_Quit]
level2_buttons = [button_Previous,button_On, button_Off, button_colourRED, button_colourBLUE, button_colourORANGE, button_colourGREEN, button_colourPINK, button_songchange,button_colourchange]
level3_buttons = [button_trackOne, button_trackTwo, button_trackThree, button_Previous]

#Background Coordinates
global bx
global by
bx = 0
by = 0
#Lap Counter
lap = 1

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

    # Cl ear the screen to white
    screen.fill(WHITE)
    screen.blit(BackGround,(0,0))
    # Draw buttons/  
    if level == 1:
        for button in level1_buttons:
            button.draw()
        font = pygame.font.SysFont('magneto', 75)
        text = font.render("Top Speed", 1, (WHITE))
        screen.blit(text, (190, 1))
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
        screen.blit(text, (275, 1))

    elif level == 4:
       bx = -3977.1424852867044
       by = -3932.452859504728
       if player.rect.x > SCREENWIDTH/2 and player.rect.x < SCREENWIDTH/2+5 and player.rect.y < SCREENHEIGHT/2:
            lap += 1
        #MOVE THE TRACK, NOT THE SPRITE!!
       screen.fill(WHITE)
       screen.blit(Nurburgring,(bx, by))
       print(bx, by, speed)
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT] or keys[pygame.K_a]:
<<<<<<< HEAD
          player.rotLeft(2)          
       if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
          player.rotRight(2)
       if keys[pygame.K_UP] or keys[pygame.K_w]:
          bx, by = player.moveForward(bx, by)
       if keys[pygame.K_DOWN] or keys[pygame.K_s]:
          bx, by = player.moveForward(bx, by)
=======
           player.rotLeft(6)          
       if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
           player.rotRight(6)
       if keys[pygame.K_UP] or keys[pygame.K_w]:
          bx, by, speed = player.accelerate(bx, by, speed)
       if keys[pygame.K_DOWN] or keys[pygame.K_s]:
           bx, by, speed = player.moveBackward(bx, by, speed)
       else:
           bx, by, speed = player.deccelerate(bx, by, speed)

           4
>>>>>>> 3e1463175232530766f3f06ddbe900f070b2033e
       all_sprites_list.update()       
       all_sprites_list.draw(screen)
       font = pygame.font.SysFont('Segoe Print', 40)
       text = font.render("Lap"+str(lap), 1, (WHITE))
       screen.blit(text, (300, 1))
    elif level == 5:
        if bx < -3100 and bx > -3105 and by > -1900:
            lap += 1
        screen.fill(WHITE)
        screen.blit(Oval_Track,(bx, by))
        print(bx, by, speed)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.rotLeft(2)          
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.rotRight(2)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
<<<<<<< HEAD
           bx, by = player.moveForward(bx, by)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            bx, by = player.moveForward(bx, by)
=======
           bx, by, speed = player.accelerate(bx, by, speed)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            bx, by, speed = player.moveBackward(bx, by, speed)
        else:
            bx, by, speed = player.deccelerate(bx, by, speed)
            
>>>>>>> 3e1463175232530766f3f06ddbe900f070b2033e
        all_sprites_list.update()       
        all_sprites_list.draw(screen)
        font = pygame.font.SysFont('Segoe Print', 40)
        text = font.render("Lap"+str(lap), 1, (WHITE))
        screen.blit(text, (300, 1))
        
    elif level == 6:
        if bx < -1250 and bx > -1255 and by > -2250:
            lap += 1
<<<<<<< HEAD
        screen.fill(WHITE)
        screen.blit(Road_Atlanta,(bx, by))
        print(bx, by)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.rotLeft(2)          
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.rotRight(2)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
           bx, by = player.moveForward(bx, by)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            bx, by = player.moveForward(bx, by)
        all_sprites_list.update()       
        all_sprites_list.draw(screen)
        font = pygame.font.SysFont('magneto', 40)
        text = font.render("Lap"+str(lap), 1, (WHITE))
        screen.blit(text, (300, 1))
=======
       screen.fill(WHITE)
       screen.blit(Road_Atlanta,(bx, by))
       print(bx, by, speed)
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT] or keys[pygame.K_a]:
           player.rotLeft(6)          
       if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
           player.rotRight(6)
       if keys[pygame.K_UP] or keys[pygame.K_w]:
          bx, by, speed = player.accelerate(bx, by, speed)
       if keys[pygame.K_DOWN] or keys[pygame.K_s]:
           bx, by, speed = player.moveBackward(bx, by, speed)
       else:
           bx, by, speed = player.deccelerate(bx, by, speed)
             
       all_sprites_list.update()       
       all_sprites_list.draw(screen)
       font = pygame.font.SysFont('magneto', 40)
       text = font.render("Lap"+str(lap), 1, (WHITE))
       screen.blit(text, (300, 1))
>>>>>>> 3e1463175232530766f3f06ddbe900f070b2033e
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

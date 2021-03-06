# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys, random
pygame.init()
from buttonClass import Button
from carClass import Player, Car
#Maps
BackGround = pygame.image.load('Photos/lamborgini-egoista-36475.jpg')
Road_Atlanta = pygame.image.load('Photos/Road_Atlanta.png')
Road_Atlanta_Mini = pygame.image.load('Photos/Road_Atlanta_Mini.png')
Oval_Track = pygame.image.load("Photos/Oval_Track.png")
Oval_Track_Mini = pygame.image.load('Photos/Oval_Track_Mini.png')
Nurburgring = pygame.image.load('Photos/Nurburgring.png')
Nurburgring_Mini = pygame.image.load('Photos/Nurburgring_MiniMap.png')
#Cars
Blue_Car = pygame.image.load('Photos/Blue Car.png')
Green_Car = pygame.image.load('Photos/Green Car.png')
Smile_Car = pygame.image.load('Photos/Smile Car.png')
Orange_Car = pygame.image.load('Photos/Orange Car.png')
Pink_Car = pygame.image.load("Photos/Pink Car.png")
Red_Car = pygame.image.load("Photos/Red Car.png")

#music
playlist = []
playlist.append ('Music/Dragonball Super - Ultra Instinct Rush (HQ Recreation).mp3')
playlist.append ('Music/Lil Uzi Vert Ft. Quavo & Travis Scott- Go Off (Clean) (1).mp3')
playlist.append ('Music/PnB Rock- Horses (Clean).mp3')
playlist.append ('Music/Rick Astley - Never Gonna Give You Up (Video).mp3')
playlist.append ('Music/Darude - Sandstorm.mp3')
playlist.append ('Music/Legend Has It Clean - Run The Jewels.mp3')
playlist.append('Music/Classical Gas [Mason Williams] - Songs - Tommy Emmanuel.mp3')
playlist.append('Music/Tokyo Drift - Teriyaki Boyz [ MUSIC VIDEO ] HD.mp3')

Sound = pygame.mixer_music.load(playlist[random.randint(0,7)])
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

#Mini map sprite
Mini_Map_Sprite = pygame.sprite.Group()
miniCar = Car(RED, 5, 5)
Mini_Map_Sprite.add(miniCar)

#player sprite
all_sprites_list = pygame.sprite.Group()
image = Blue_Car
player = Player(0, 0,  image)
all_sprites_list.add(player)

def blue_car():
   player.image = Blue_Car
   player.original = Blue_car

def green_car():
   player.image = Green_Car
   player.original = Green_Car

def orange_car():
   player.image = Orange_Car
   player.original = Orange_Car

def red_car():
   player.image = Red_Car
   player.original = Red_Car

def pink_car():
   player.image = Pink_Car
   player.original = Pink_Car

def my_play_function():
   global level
   level = 7

def my_race_function():
   global level
   level = 3

def my_track1_function():
    global level, bx, by, miliSec, Sec, Min
    level += 1
    bx = -291.26694934954867
    by = -3349.390480728794
    player.rotLeft(90)
    miliSec = 0
    Sec = 0
    Min = 0
    
def my_track2_function():
    global level, bx, by, speed, miliSec
    level += 2
    bx = -1132.7936704725912
    by = -1983.3962939071591
    speed = 40
    miliSec = 0
    Sec = 0
    Min = 0

def my_track3_function():
    global level, bx, by, miliSec
    level += 3
    bx = -2040.9458062023593
    by = -2160.2446692390226
    miliSec = 0
    Sec = 0
    Min = 0
   
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
def Main_Menu():
   global level
   level = 1
   
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
    elif level == 7:
       for button in level7_buttons:
          if button.rect.collidepoint(pos):
             button.call_back()
             
    elif level == 8:
       for button in level8_buttons:
          if button.rect.collidepoint(pos):
             button.call_back()

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects
button_Play = Button("Race", (SCREENWIDTH/2, SCREENHEIGHT/4), GREY,my_play_function, DGREY)
button_Race = Button("Let's GO", (500, 306), B_GREEN, my_race_function, GREEN)
button_Previous = Button("Previous", (SCREENWIDTH/2, SCREENHEIGHT*9/10), GREY, my_previous_function, DGREY)
button_Quit = Button("Quit", (SCREENWIDTH/2, SCREENHEIGHT*3/4), GREY, my_quit_function, DGREY)
button_Main = Button("Main Menu", (SCREENWIDTH/2, SCREENHEIGHT*9/10), RED, Main_Menu, BLOOD)

button_Settings = Button("Settings", (SCREENWIDTH/2, SCREENHEIGHT/2), GREY, my_settings_function, DGREY)
button_On = Button("ON", (SCREENWIDTH/4, SCREENHEIGHT/6), B_GREEN, my_on_function, GREEN)
button_Off = Button("OFF", (SCREENWIDTH*3/4, SCREENHEIGHT/6), RED, my_off_function, BLOOD)
button_songchange = Button("Change Song", (SCREENWIDTH/2, SCREENHEIGHT*2/10), GREY, my_change_song_function, DGREY)

button_colourchange = Button("Colour", (SCREENWIDTH/2, SCREENHEIGHT*5/10), GREY, my_change_song_function, DGREY)
button_colourRED = Button("RED", (SCREENWIDTH*1/6, SCREENHEIGHT*2/3), GREY, red_car, DGREY)
button_colourBLUE = Button("BLUE", (SCREENWIDTH*2/6, SCREENHEIGHT*2/3), GREY, blue_car, DGREY)
button_colourORANGE = Button("ORANGE", (SCREENWIDTH*3/6, SCREENHEIGHT*2/3), GREY, orange_car, DGREY)
button_colourGREEN = Button("GREEN", (SCREENWIDTH*4/6, SCREENHEIGHT*2/3), GREY, green_car, DGREY)
button_colourSmile = Button("PINK", (SCREENWIDTH*5/6, SCREENHEIGHT*2/3), GREY, pink_car, DGREY)

button_trackOne = Button("Track One", (SCREENWIDTH/3, SCREENHEIGHT/2), GREY, my_track1_function, DGREY)
button_trackTwo = Button("Track Two",  (SCREENWIDTH/2, SCREENHEIGHT/2), GREY, my_track2_function, DGREY)
button_trackThree = Button("Track Three",  (SCREENWIDTH*2/3, SCREENHEIGHT/2), GREY, my_track3_function, DGREY)

#arrange button groups depending on level
level1_buttons = [button_Settings, button_Play, button_Quit]
level2_buttons = [button_Previous, button_On, button_Off, button_colourRED, button_colourBLUE, button_colourORANGE, button_colourGREEN, button_colourSmile, button_colourchange]
level3_buttons = [button_trackOne, button_trackTwo, button_trackThree, button_Previous]
level7_buttons = [button_Race]
level8_buttons = [button_Race, button_Main]

#Background Coordinates
bx = 0
by = 0

#Speed
global speed
speed = 0
#Lap Counter
lap = 0

#Timer
global miliSec, Sec, Min
miliSec = 0
Sec = 0
Min = 0

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
    # Draw buttons/  
    if level == 1:
        screen.blit(BackGround,(0,0))
        for button in level1_buttons:
            button.draw()
        font = pygame.font.SysFont('magneto', 75)
        text = font.render("Top Speed", 1, (WHITE))
        screen.blit(text, (190, 1))
    elif level == 2:
        screen.blit(BackGround,(0,0))
        font = pygame.font.SysFont('magneto', 40)
        text = font.render("Sound", 1, (WHITE))
        screen.blit(text, (330, 1))
        for button in level2_buttons:
            button.draw()
    elif level == 3:
        screen.blit(BackGround,(0,0))
        for button in level3_buttons:
            button.draw()
        font = pygame.font.SysFont('magneto', 40)
        text = font.render("Pick a Track", 1, (WHITE))
        screen.blit(text, (275, 1))

    elif level == 4:
       #Lap
       if bx < -128 and bx > -469 and by < -3110 and by > -3120:
            lap += 1
       screen.fill(WHITE)
       screen.blit(Nurburgring,(bx, by))
       screen.blit(Nurburgring_Mini,(0, 0))
       print(bx, by, speed)
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT] or keys[pygame.K_a]:
          player.rotLeft(9)
       if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
           player.rotRight(9)
       if keys[pygame.K_UP] or keys[pygame.K_w]:
          bx, by, speed = player.accelerate(bx, by, speed)
       if keys[pygame.K_DOWN] or keys[pygame.K_s]:
           bx, by, speed = player.moveBackward(bx, by, speed)
       if keys[pygame.K_ESCAPE]:
          level = 3
          miliSec = 0
          Sec = 0
          Min = 0
       else:
           bx, by, speed = player.deccelerate(bx, by, speed)
           
       if lap == 3:
          level = 8
#Timer
       miliSec += 1
       if miliSec == 16:
          Sec += 1
          miliSec = 0
       if Sec == 59:
          Min += 1
          Sec = 0
       print(str(Min) + ':' + str(Sec) + ':' + str(miliSec))
       Mini_Map_Sprite.update(bx, by, level)
       Mini_Map_Sprite.draw(screen)
       all_sprites_list.update()       
       all_sprites_list.draw(screen)
       #Lap Print
       font = pygame.font.SysFont('magneto', 40)
       text = font.render("Lap:"+str(lap)+"/2", 1, (WHITE))
       screen.blit(text, (300, 1))
       #Time Print
       font = pygame.font.SysFont('arabic transparent', 40)
       text = font.render(str(Min) + ':' + str(Sec) + ':' + str(miliSec), 1, (WHITE))
       screen.blit(text, (350, 45))
       
    elif level == 5:
       #Lap
        print(pygame.mouse.get_pos())
        if bx < -3200 and bx > -3250 and by > -1860 and by < -1090:
            lap += 1
        screen.fill(WHITE)
        screen.blit(Oval_Track,(bx, by))
        screen.blit(Oval_Track_Mini,(0, 0))
        print(bx, by, speed)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.rotLeft(3)          
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.rotRight(3)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
           bx, by, speed = player.accelerate(bx, by, speed)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            bx, by, speed = player.moveBackward(bx, by, speed)
        if keys[pygame.K_LSHIFT]:
           speed = 60
        if keys[pygame.K_ESCAPE]:
          level = 3
          miliSec = 0
          Sec = 0
          Min = 0
        else:
            bx, by, speed = player.deccelerate(bx, by, speed)
#timer 
        miliSec += 1
        if miliSec == 16:
           Sec += 1
           miliSec = 0
        if Sec == 59:
           Min += 1
           Sec = 0
        if lap == 11:
            level = 8
        Mini_Map_Sprite.update(bx, by, level)
        Mini_Map_Sprite.draw(screen) 
        all_sprites_list.update()       
        all_sprites_list.draw(screen)
        #Lap Print
        font = pygame.font.SysFont('magneto', 40)
        text = font.render("Lap:"+str(lap)+"/10", 1, (WHITE))
        screen.blit(text, (300, 1))
        #Timer Print
        font = pygame.font.SysFont('arabic transparent', 40)
        text = font.render(str(Min) + ':' + str(Sec) + ':' + str(miliSec), 1, (WHITE))
        screen.blit(text, (350, 45))       
            
    elif level == 6:
       #Lap
       print(pygame.mouse.get_pos())
       if bx < -2560 and bx > -2610 and by > -2305 and by < -2020:
          lap += 1
       screen.fill(WHITE)
       screen.blit(Road_Atlanta,(bx, by))
       screen.blit(Road_Atlanta_Mini,(0, 0))
       print(bx, by, speed)
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT] or keys[pygame.K_a]:
           player.rotLeft(7)          
       if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
           player.rotRight(7)
       if keys[pygame.K_UP] or keys[pygame.K_w]:
          bx, by, speed = player.accelerate(bx, by, speed)
       if keys[pygame.K_DOWN] or keys[pygame.K_s]:
           bx, by, speed = player.moveBackward(bx, by, speed)
       if keys[pygame.K_LSHIFT]:
           speed = 40
       if keys[pygame.K_ESCAPE]:
          level = 3
          miliSec = 0
          Sec = 0
          Min = 0
       else:
          bx, by, speed = player.deccelerate(bx, by, speed)

#Timer
       miliSec += 1
       if miliSec == 16:
          Sec += 1
          miliSec = 0
       if Sec == 59:
          Min += 1
          Sec = 0
       if lap == 4:
          level = 8
       Mini_Map_Sprite.update(bx, by, level)
       Mini_Map_Sprite.draw(screen)
       all_sprites_list.update()       
       all_sprites_list.draw(screen)
       #Lap Print
       font = pygame.font.SysFont('magneto', 40)
       text = font.render("Lap:"+str(lap)+"/3", 1, (WHITE))
       screen.blit(text, (300, 1))
       #Timer Print
       font = pygame.font.SysFont('arabic transparent', 40)
       text = font.render(str(Min) + ':' + str(Sec) + ':' + str(miliSec), 1, (WHITE))
       screen.blit(text, (350, 45))

    elif level == 7:
       #Instructions
       screen.blit(BackGround,(0,0))
       font = pygame.font.SysFont('magneto', 40)
       text = font.render("Instructions", 1, (WHITE))
       screen.blit(text, (300, 1))
       font = pygame.font.SysFont('arabic transparent', 24)
       text = font.render("The point of the game is to race around a few tracks, some real, and others not", 1, (WHITE))
       screen.blit(text, (100, 50))
       font = pygame.font.SysFont('arabic transparent', 24)
       text = font.render("and try to get the best times of 3 laps", 1, (WHITE))
       screen.blit(text, (100, 70))
       font = pygame.font.SysFont('arabic transparent', 24)
       text = font.render("To play you use WSAD or the Arrow Keys", 1, (WHITE))
       screen.blit(text, (100, 100))
       font = pygame.font.SysFont('arabic transparent', 24)
       text = font.render("W/ Up Arrow = Accelerate", 1, (WHITE))
       screen.blit(text, (100, 140))
       font = pygame.font.SysFont('arabic transparent', 24)
       text = font.render("S/ Down Arrow = Stop and move backward", 1, (WHITE))
       screen.blit(text, (100, 160))
       font = pygame.font.SysFont('arabic transparent', 24)
       text = font.render("A/ Left Arrow = Turn Left", 1, (WHITE))
       screen.blit(text, (100, 180))
       font = pygame.font.SysFont('arabic transparent', 24)
       text = font.render("D/ Right Arrow = Turn Right", 1, (WHITE))
       screen.blit(text, (100, 200))
       font = pygame.font.SysFont('arabic transparent', 24)
       text = font.render("Left Shift = Boost **Not on track 1**", 1, (WHITE))
       screen.blit(text, (100, 220))
       font = pygame.font.SysFont('arabic transparent', 24)
       text = font.render("ESCAPE is to go back to track select", 1, (WHITE))
       screen.blit(text, (100, 240))
       for button in level7_buttons:
            button.draw()


   elif level == 8:
      #Final Screen
       screen.blit(BackGround,(0,0))
       font = pygame.font.SysFont('magneto', 60)
       text = font.render("Your time was:"+str(Min) + ':' + str(Sec) + ':' + str(miliSec), 1, (WHITE))
       screen.blit(text, (50, 1))
       font = pygame.font.SysFont('arabic transparent', 40)
       text = font.render("Are you able to beat your time????", 1, (WHITE))
       screen.blit(text, (150, 70))
       for button in level8_buttons:
            button.draw()
      
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

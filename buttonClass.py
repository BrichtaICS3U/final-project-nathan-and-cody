import pygame
pygame.init()
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
NEON = (70, 255, 191)
VIOLET = (127, 0, 255)
BLOOD  = (255, 115, 60)
PINK = (255, 96, 210)
DGREY = (45, 45, 45)

SCREENWIDTH = 800
SCREENHEIGHT = 507

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)


class Button():
    """This is a class for a generic button.
    
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """
    def __init__(self, txt, location, ac, action, bg=WHITE, fg=WHITE, size=(110, 40), font_name="centurygothic", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.ac = ac #acive colour
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = self.ac  # mouseover color
        elif pos != self.rect.collidepoint(pos):
            self.bg = self.color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()

import pygame
pygame.init()
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):

    def __init__(self, colour, width, height, speedx, speedy):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width = width
        self.height = height
        self.colour = colour
        self.speedx = speedx
        self.speedy = speedy

        pygame.draw.rect(self.image, self.colour, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, pixels):
        self.rect.y -= pixels
 
    def moveBackward(self, pixels):
        self.rect.y += pixels
 
    def changeSpeed(self, speed):
        self.speed = speed
 
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

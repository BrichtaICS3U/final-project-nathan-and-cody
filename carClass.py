import pygame, math
pygame.init()
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
SCREENWIDTH = 800
SCREENHEIGHT = 507

class Player(pygame.sprite.Sprite):

    def __init__(self, startangle):

        super().__init__()

        self.image = pygame.image.load("Photos/car.png")
        self.original = self.image
        self.angle = startangle
        self.rect = self.image.get_rect()
        self.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)

    def rotRight(self, angle):
        self.angle -= angle
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.original, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter
 
    def rotLeft(self, angle):
        self.angle += angle
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.original, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter
 
    def moveForward(self, bx, by):
        bx -= math.cos(math.radians(self.angle))*20
        by += math.sin(math.radians(self.angle))*20
        return bx, by
        #self.rect.y -= math.cos(math.radians(self.angle))*10
        #self.rect.x -= math.sin(math.radians(self.angle))*10
 
    def moveBackward(self, bx, by):
        bx += math.cos(math.radians(self.angle))*10
        by -= math.sin(math.radians(self.angle))*10
        return bx, by
 
    def changeSpeed(self, speed):
        self.speed = speed
 
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        
    def draw(self, screen):
        self.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)
        screen.blit(self.image, self.rect)

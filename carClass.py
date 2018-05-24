import pygame, math
pygame.init()
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
SCREENWIDTH = 800
SCREENHEIGHT = 507

class Player(pygame.sprite.Sprite):

    def __init__(self, startangle, speed, image):

        super().__init__()

        self.image = image
        self.original = self.image
        self.angle = startangle
        self.rect = self.image.get_rect()
        self.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)
        self.speed = speed

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
 
    #def moveForward(self, bx, by):
        #bx -= math.cos(math.radians(self.angle))*20
       # by += math.sin(math.radians(self.angle))*20
        #return bx, by
 
    def moveBackward(self, bx, by, speed):
        if speed >= 1:
            speed -= 1
            bx += math.cos(math.radians(self.angle))*speed
            by -= math.sin(math.radians(self.angle))*speed
        elif speed >= 0:
            speed +=1
            bx += math.cos(math.radians(self.angle))*speed
            by -= math.sin(math.radians(self.angle))*speed
        return bx, by, speed
    
    def accelerate(self, bx, by, speed):
        speed +=1
        bx -= math.cos(math.radians(self.angle))*speed
        by += math.sin(math.radians(self.angle))*speed
        return bx, by, speed
    
    def deccelerate(self, bx, by, speed):
        if speed >= 1:
            speed *= 0.95
            bx -= math.cos(math.radians(self.angle))*speed
            by += math.sin(math.radians(self.angle))*speed
        elif speed >= 0:
            speed = 0
            bx -= math.cos(math.radians(self.angle))*speed
            by += math.sin(math.radians(self.angle))*speed
        return(bx, by, speed)
    
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        
    def draw(self, screen):
        self.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)
        screen.blit(self.image, self.rect)

import pygame, math
pygame.init()
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
SCREENWIDTH = 800
SCREENHEIGHT = 507

#Player Spite
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
        speed += 1
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

#Mini Map Sprite
class Car(pygame.sprite.Sprite): 
    def __init__(self, color, width, height):
        super().__init__() 

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width = width
        self.height = height
        self.color = color

        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self, bx, by, level):
        if level == 4:
            self.rect.x = -0.0271*bx+616
            self.rect.y = -0.0278*by+330
        elif level == 5:
            self.rect.x = -0.0275*bx+603
            self.rect.y = -0.0273*by+334
        elif level == 6:
            self.rect.x = -0.0337*bx+547
            self.rect.y = -0.0341*by+292

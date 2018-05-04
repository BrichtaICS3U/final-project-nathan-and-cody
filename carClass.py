BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
BLUE = (0,0,200)
BRIGHT_BLUE=(0,0,255)
class Player():

    def __init__(self, colour, width, height, speed):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colourkey(WHITE)

        self.width = width
        self.height = height
        self.colour = colour
        self.speed = speed

        pygame.draw.rect(self.image, self.colour, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
 
    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20
 
    def changeSpeed(self, speed):
        self.speed = speed
 
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

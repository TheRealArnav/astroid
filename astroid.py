import pygame
import random
import time
pygame.init()
pygame.font.init()
HEIGHT = 800
WIDTH = 800
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("ASTROID DESTROYER")


fps = 60
clock = pygame.time.Clock()


small_astroid = pygame.image.load("C:/Pygame2/images/astroid.png")
medium_astroid = pygame.image.load("C:/Pygame2/images/mediumastroid.png")
large_astroid = pygame.image.load("C:/Pygame2/images/bigastroid.png")
star = pygame.image.load("C:/Pygame2/images/star.png")
alien_ship = pygame.image.load("C:/Pygame2/images/alienship.png")

rocketship = pygame.image.load("C:/Pygame2/images/spaceship.png")
background = pygame.image.load("C:/Pygame2/images/spacebg3.png")

class Rocket(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.img = rocketship
        self.speed = 4
        self.angle = 0
        self.updaterotation()
    
    def updaterotation(self):
        self.rotated_image = pygame.transform.rotate(self.img,self.angle)
        self.rotated_rect = self.rotated_image.get_rect(center = (self.x,self.y))
    def draw(self):
        screen.blit(self.rotated_image,self.rotated_rect)
    def turnleft(self):
        self.angle = self.angle + 6

        self.updaterotation()
    def turnright(self):
        self.angle = self.angle - 6
    
        self.updaterotation()
    def forward(self):
        self.y = self.y - self.speed
    def backward(self):
        self.y = self.y + self.speed


class Astroid(pygame.sprite.Sprite):
    def __init__(self,dir,size):
        super().__init__()
        self.dir = dir
        self.size = size
        self.image = pygame.image.load("C:/Pygame2/images/astroid.png")
    def draw(self):

        if self.size == 1:
            self.image = small_astroid
        if self.size == 2:
            self.image = medium_astroid
        if self.size == 3:
            self.image = large_astroid

        
        if self.dir == "top":
            self.y = -15
            self.x = random.randint(0,WIDTH)
        if self.dir == "bottom":
            self.y = 815
            self.x = random.randint(0,WIDTH)
        if self.dir == "left":
            self.x = -15
            self.y = random.randint(0,HEIGHT)
        if self.dir == "right":
            self.x = 815 
            self.y = random.randint(0,HEIGHT)
        screen.blit(self.image,(self.x,self.y))
        




rocket = Rocket(400,400)


astroidgroup = pygame.sprite.Group()



run = True
while run:
    clock.tick(fps)
    for i in range(30):
        size = random.randint(1,3)
        direclist = ["top","bottom","right","left"]
        y = random.randint(0,3)
        direction = direclist[y]
        astroid = Astroid(direction,size)
        astroid.draw()
        astroidgroup.add(astroid)
        pygame.display.update()


    screen.blit(background,(0,0))
    rocket.draw()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rocket.turnleft()
    if keys[pygame.K_RIGHT]:
        rocket.turnright()
    if keys[pygame.K_UP]:
        rocket.forward()
    if keys[pygame.K_DOWN]:
        rocket.backward()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #if event.type == pygame.key.get_pressed():
        
            
            

    pygame.display.flip()
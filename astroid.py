import pygame
import random
import time
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("ASTROID DESTROYER")


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
        self.x = self.x - self.speed
        self.updaterotation()
    def turnright(self):
        self.angle = self.angle - 6
        self.x = self.x + self.speed
        self.updaterotation()
    def forward(self):
        self.y = self.y - self.speed
    def backward(self):
        self.y = self.y + self.speed






rocket = Rocket(400,400)






run = True
while run:
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
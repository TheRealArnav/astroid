import pygame
import random
import time
import math
pygame.init()
pygame.font.init()
HEIGHT = 800
WIDTH = 800
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("ASTROID DESTROYER")


fps = 60
clock = pygame.time.Clock()
count = 0
score = 0
lives = 3
gameover = False
small_astroid = pygame.image.load("C:/Pygame2/images/astroid.png")
medium_astroid = pygame.image.load("C:/Pygame2/images/mediumastroid.png")
large_astroid = pygame.image.load("C:/Pygame2/images/bigastroid.png")
star = pygame.image.load("C:/Pygame2/images/star.png")
alien_ship = pygame.image.load("C:/Pygame2/images/alienship.png")

rocketship = pygame.image.load("C:/Pygame2/images/spaceship.png")
background = pygame.image.load("C:/Pygame2/images/spacebg3.png")
txt = pygame.font.SysFont("Calibri",35,False)

class Bullet():
    def __init__(self,x,y,angle):
        self.x = x
        self.y = y
        angle = math.radians(angle)
        self.speed = 10
        self.dx = math.sin(angle)
        self.dy = math.cos(angle)
       
    def move(self): 
        self.y = self.y - (self.dy * self.speed)
        self.x = self.x - (self.dx * self.speed)
    def draw(self):
        pygame.draw.rect(screen,"yellow",(self.x,self.y,5,20))
            
        



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
        self.x = random.randint(0,800)
        self.y = random.randint(0,800)
        self.angle = 0
        
        self.image = pygame.image.load("C:/Pygame2/images/astroid.png")
        if self.size == 1:
            self.image = small_astroid
        if self.size == 2:
            self.image = medium_astroid
        if self.size == 3:
            self.image = large_astroid

        self.w = self.image.get_width()
        self.h = self.image.get_height()

        if self.dir == "top":
            self.y = -15
            self.x = random.randint(0,WIDTH)
        if self.dir == "bottom":
            self.y = 715
            self.x = random.randint(0,WIDTH)
        if self.dir == "left":
            self.x = -15
            self.y = random.randint(0,HEIGHT)
        if self.dir == "right":
            self.x = 715 
            self.y = random.randint(0,HEIGHT)

        self.rect = self.image.get_rect()
        
    def draw(self):      

        screen.blit(self.image,(self.x,self.y))
        
    def move(self):
        directionlist = [-1,1]
        if self.dir == "top":
            x = random.choice(directionlist)
            self.x = self.x - x
            self.y = self.y + 1
        if self.dir == "bottom":
            x = random.choice(directionlist)
            self.x = self.x - x
            self.y = self.y - 1
        if self.dir == "left":
            x = random.choice(directionlist)
            self.y = self.y - x
            self.x = self.x + 1
        if self.dir == "right":
            x = random.choice(directionlist)
            self.y = self.y - x
            self.x = self.x - 1 


        #self.angle = self.angle + 2
        #if self.angle == 360:
        #    self.angle = 0
        #self.image = pygame.transform.rotate(self.image,self.angle)
        #self.image.get_rect




rocket = Rocket(400,400)


astroidlist = []


        
bulletlist = []


 
run = True
while run:
    
    clock.tick(fps)
    count = count + 1
    if count%50 == 0 and gameover == False:
        size = random.randint(1,3)
        direclist = ["top","bottom","right","left"]
        y = random.choice(direclist)
        direction = y
        astroid = Astroid(direction,size)
        
        astroidlist.append(astroid)

    for astroid in astroidlist:
        astroid.move()
        astroid.draw()
        for bullet in bulletlist:
            if pygame.Rect(astroid.x,astroid.y,astroid.w,astroid.h).colliderect(pygame.Rect(bullet.x,bullet.y,5,20)):
                astroidlist.remove(astroid)
                bulletlist.remove(bullet)
                score = score + 1
                break
            
        pygame.display.update()
        
        if pygame.Rect(astroid.x,astroid.y,astroid.w,astroid.h).colliderect(rocket.rotated_rect):
            if lives > 0:
                lives = lives - 1
                astroidlist.remove(astroid)
            if lives == 0:
                gameover = True
                gameovertxt = txt.render("GAMEOVER",True,"White")
                screen.blit(gameovertxt,(HEIGHT//2,WIDTH//2))
                pygame.display.update()


    scoretxt = txt.render("Score:  "+str(score),True,"White")
    livestxt = txt.render("Lives:  "+str(lives),True,"white")

    

    screen.blit(background,(0,0))
    rocket.draw()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gameover == False:
        rocket.turnleft()
    if keys[pygame.K_RIGHT] and gameover == False:
        rocket.turnright()
    if keys[pygame.K_UP] and gameover == False:
        rocket.forward()
    if keys[pygame.K_DOWN] and gameover == False:
        rocket.backward()
    
    #pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gameover == False:
                bullet = Bullet(rocket.x, rocket.y - 0, rocket.angle)
                bulletlist.append(bullet)
                
        #if event.type == pygame.key.get_pressed():
        
            
            
    for bullet in bulletlist:
        bullet.draw()
        bullet.move()

    screen.blit(scoretxt,(0,0))
    screen.blit(livestxt,(0,40))
        
    pygame.display.update()
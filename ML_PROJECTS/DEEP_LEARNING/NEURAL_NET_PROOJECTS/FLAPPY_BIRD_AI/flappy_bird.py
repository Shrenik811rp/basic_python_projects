import pygame
import neat
import time
import os
import random


WIDTH = 600
HEIGHT = 800

'''
stores the bird images

transform.scale2x ->scales the image twice the original size

pygame.image.load -> loads the image
'''

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird3.png")))]

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")))

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")))

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))




'''
class for bird
'''

class Bird:
    IMGS = BIRD_IMGS
    '''When we tilt bird up and down we rotate bird by certain degrees'''
    MAX_ROTATION = 25

    '''how much we rotate the bird'''
    ROTAT_VELOCITY = 20

    '''we can change how fast the bird moves '''
    ANIMATION_TIME = 5


    def __init__(self,x,y):
        #get starting position of bird
        self.x = x
        self.y = y

        #how much bird tilts
        self.tilt = 0

        self.tick_count =0

        #initially not moving
        self.velocity = 0

        #tilting
        self.height = self.y

        #which image is displayed
        self.img_count = 0

        self.img = self.IMGS[0]
    
    def jump(self):
        #when we move up we have to subtract coordinates from origin
        self.velocity = -10.5

        #keep track of when we last jumped
        self.tick_count = 0

        #keep track of its previous height
        self.height = self.y


    #function to move bird
    def move(self):
        pass



while True:
    Bird.move()






















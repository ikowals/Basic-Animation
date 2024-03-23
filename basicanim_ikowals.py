# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:07:32 2024

@author: ikowa
"""

""" Charlie.py
    illustrates basic motion
    image loading
    move Charlie the Cardinal
"""


#Initialize
import pygame
import random

def main():
    pygame.init()

    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("UFO!")

    #Entities
    #yellow background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("blue")

    #load an image
    meteor = pygame.image.load("New Piskel.gif")
    sky = pygame.image.load("sky.png")
    ufo = pygame.image.load("ufoedit.png")
    meteor = meteor.convert_alpha()
    sky = sky.convert_alpha()
    ufo = ufo.convert_alpha()
    meteor = pygame.transform.scale(meteor, (100, 100))
    sky = pygame.transform.scale(sky, (700, 500))
    ufo = pygame.transform.scale(ufo, (200,200))
    

    # set up some cardinal variables
    meteor_x = 0
    meteor_y = 200
    ufo_x = 100
    ufo_y= 100

    #ACTION

        #Assign
    clock = pygame.time.Clock()
    keepGoing = True

        #Loop
   
    while keepGoing:

        #Time
        clock.tick(30)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #modify cardinal value
        meteor_x += random.randint(1,5)
        meteor_y += random.randint(1,10)
        ufo_x += random.randint(-5,5)
        ufo_y += random.randint(-10,10)
        meteor = pygame.transform.rotate(meteor,90) 
        #check boundaries
        if meteor_x > screen.get_width():
            meteor_x = 0
        if meteor_y > screen.get_width():
            meteor_y = 0
        if ufo_y > 400:
            #ufo_y = 0
            ufo_y += -10
        if ufo_x > 600:
            #ufo_x = 0
            ufo_x += -5
        if ufo_x < 0:
            #ufo_x = 0 
            ufo_x += 5
        if ufo_y < 0:
            #ufo_y = 0
            ufo_y += 10
         
        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(sky, (0, 0))
        screen.blit(ufo, (ufo_x,ufo_y))
        screen.blit(meteor, (meteor_x, meteor_y))
    
        
        pygame.display.flip()
     

    pygame.quit()

if __name__ == "__main__":
    main()
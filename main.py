import pygame
import random
pygame.init()
screen = pygame.display.set_mode((400,500))
display_surface = pygame.display.set_mode((20, 10))  

done = False  
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    pygame.display.flip()  

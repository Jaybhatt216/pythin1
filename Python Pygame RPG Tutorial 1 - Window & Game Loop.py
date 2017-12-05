import sys
import os
import pygame
import pygame_assets
import pygametemplate

pygame.init()

def create_window (): #create a window function creates a window
    global window,window_height, window_width, window_title #golbal variables
    window_width, window_height = 800,600 #the size of the window
    window_title = "RPG Tutorial"#this is the name of the title
    pygame.display.set_caption(window_title) #displays the title
    window = pygame.display.set_mode((window,window_height, window_width), pygame.HWSURFACE|pygame.DOUBLEBUF) # this is for memory management
    create_window()



isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False


window.fill((0,0,0)) # 000 is black basically first tuple is red then green then blue



pygame.quit()
sys.exit()

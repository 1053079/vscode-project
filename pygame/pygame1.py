import pygame
import os

# initialising pygame
pygame.init()

#defining size of game window
windowsSize = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hello World Printer")

#defining font attributes
myFont = pygame.font.Sysfont("Segoe UI",90)
HelloWorld = myFont.render("Hello World",1, (255, 0, 255), (255, 255, 255))

except
# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.

import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

# initialize pygame module
pygame.init()

# get surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

# background - sky
gameDisplay.fill(Color('lightblue'))

# house with a roof
draw.rect(gameDisplay, Color('brown'), Rect(100, 200, 300, 200))
draw.polygon(gameDisplay, Color('black'), [(100, 200), (400, 200), (250, 50)])

# green grass
draw.rect(gameDisplay, Color('green'), Rect(0, 400, 500, 100))

# sun
draw.circle(gameDisplay, Color('yellow'), (50, 50), 50)

# show the graphics on the screen
display.flip()

# Wait for user's input before closing the window
input("Press enter to exit")
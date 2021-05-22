# imports
import os
import pygame as pg

# folders

gameFolder = os.path.dirname(__file__)
imageFolder = os.path.join(gameFolder, "img")
arrowFolder = os.path.join(imageFolder, "arrows")
sndFolder = os.path.join(gameFolder, "sound")
bgFolder = os.path.join(imageFolder, "backgrounds")

# Game Values

HEIGHT = 500
WIDTH = 1000
FPS = 30
title = "Advanced Template"

#colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DARKISH_RED = (125, 0, 0)
DEEP_GREEN = (0, 40, 0)
DARK_BLUE = (0, 0, 80)
DEEP_BLUE = (0, 0, 40)

N_BLUE = (25, 0, 100)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
LIGHT_BLUE = (100, 150, 200)
MAGENTA = (255, 0, 255)

DARK_RED = (80, 0, 0)
DEEP_RED = (30, 0, 0)
PURPLE = (80, 0, 80)
PURPLE2 = (80, 0, 150)
DARK_PURPLE = (50, 0, 50)

LIGHT_COLOR = (167, 153, 234)
TAN = (200, 152, 89)

# LAYERS
ARROW_LYR = 2
OBJECT_LYR = 1
THING_LYR = 1



#####################################################################
#   File containing constants that you might need in your assignment.
#   Make sure to import the library in all your files using a statement
#   like:
#   from Constants import *
#####################################################################

# import libraries that you will need
import pygame
from random import randint, choice


# constants for screen size
WIDTH = 1200
HEIGHT = 750

# constants for colors
RED = [0xe3, 0x1b, 0x23]
BLUE = [0x00,0x2F,0x8B]
GREY = [0xA2, 0xAA, 0xAD]
WHITE = [0xFF, 0xFF, 0xFF]
BLACK = [0x00, 0x00, 0x00]

COLORS = [BLUE, RED, GREY, WHITE, BLACK]

# Image paths
WIZARD_IMAGE = '../assets/images/wizard.png'
SPIDER_IMAGE = '../assets/images/spider.png'

# Sound effect paths
SPIDER_SOUND = '../assets/sounds/death2-340040.mp3'
LIFE_LOST_SOUND = '../assets/sounds/retro-hurt-2-236675.mp3'
SPELL_SOUND = '../assets/sounds/fire-magic-6947.mp3'

# keys from pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
)

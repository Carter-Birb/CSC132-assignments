#####################################################################
# author: Carter Landry
# date:
# description:
#####################################################################
import pygame
from random import randint, choice
from Item import *
from Constants import *



class Person(pygame.sprite.Sprite, Item):
    
    DEBUG = False
    
    def __init__(self):
        # The reason I am initializing these two separately, is when I tried to use *groups, I was getting getter/setter errors within Item.py for self.size.
        pygame.sprite.Sprite.__init__(self)
        Item.__init__(self)
        self.color = []
        self.surf = pygame.Surface((self.size, self.size))
        
        @property
        def color(self):
            return self._color
        
        @color.setter
        def color(self, val):
            self._color = val
        
        @property
        def surf(self):
            return self._surf
        
        @surf.setter
        def surf(self, val):
            self._surf = val


    def setColor(self):
        '''
        Obtains a random color from Constants.py and sets self.color to said color
        '''
        random_color = choice(COLORS)
        self.color = random_color
        self.surf.fill(self.color)


    def setSize(self):
        '''
        sets a Person's size to a random value between 10 - 100
        '''
        self.size = randint(10, 100)
        self.surf = pygame.Surface((self.size, self.size))


    def update(self, event:dict):
        '''
        Updates the position and status of a Person depending on what keys have been pressed
        '''
        if event[pygame.K_UP]:
            self.goUp()
        
        if event[pygame.K_DOWN]:
            self.goDown()
        
        if event[pygame.K_LEFT]:
            self.goLeft()
        
        if event[pygame.K_RIGHT]:
            self.goRight()
        
        if event[pygame.K_SPACE]:
            self.setSize()
            self.setColor()


    def setRandomPosition(self):
        '''
        Sets a Person's x, y values to random integers between 0 and WIDTH/HEIGHT depending on which value is calculated
        '''
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT)


    def getPosition(self):
        '''
        Calculates the coordinates of the top left corner of a person
        '''
        x = self.x - (self.size / 2)
        y = self.y - (self.size / 2)
        return x, y


    def __str__(self):
        '''
        __str__ method for Person
        '''
        return f"Item: name = {self.name}\tsize = {self.size}\tx = {self.x}\ty = {self.y}\tcolor = {self.color}"
    




########################### main game ################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
######################################################################

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
p = Person()
RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop
                
while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(p)
            
    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()

    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()
#####################################################################
# author: Carter Landry
# date: 3/14/2025
# description: 
# This is a file containing the Person class.
# A person has a name, x-value, y-value, and a size. 
# A Person can goLeft, goRight, goUp, and goDown.
#####################################################################

# Imports the sqrt method from python's math lib to utilize in the euclidean distance formula
from math import sqrt

# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 800
MAX_Y = 600
# Added a DEFAULT_SIZE variable aswell as the DEFAULT_NAME variable to easily access these values in multiple cases,
# as well as have the ability to alter these values once and have the code work around them.
DEFAULT_SIZE = 1
DEFAULT_NAME = "Player 1"

# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left,
# go right, go up and go down. A person also has a string function
# that prints out their name location, and size. A person also has a
# function that calculates the euclidean distance from another person
# object.
class Person:
    
    
    ## CONSTRUCTOR
    
    def __init__(self, name:str=DEFAULT_NAME, x:int=0, y:int=0): # The default name for a person is set by DEFAULT_NAME, and the default x, y values are 0, 0 respectively.
        self.name = name
        self.x = x
        self.y = y
        self.size = DEFAULT_SIZE # The default size of a Person is set by DEFAULT_SIZE
    
    
    ## GETTERS / SETTERS
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value:str):
        if len(value) < 2:
            self._name = DEFAULT_NAME
        else:
            self._name = value
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value:int):
        if value < 0:
            self._x = 0
        elif value > MAX_X:
            self._x = MAX_X
        else:
            self._x = value
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value:int):
        if value < 0:
            self._y = 0
        elif value > MAX_Y:
            self._y = MAX_Y
        else:
            self._y = value
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value:float):
        if value < DEFAULT_SIZE:
            self._size = DEFAULT_SIZE
        else:
            self._size = value
    
    
    ## FUNCTIONS
    
    def goLeft(self, distance=1):
        '''
        Moves the Person left by the specified distance
        '''
        self.x = self.x - distance
    
    def goRight(self, distance=1):
        '''
        Moves the Person right by the specified distance
        '''
        self.x = self.x + distance
    
    def goUp(self, distance=1):
        '''
        Moves the Person up by the specified distance
        '''
        self.y = self.y - distance
    
    def goDown(self, distance=1):
        '''
        Moves the Person down by the specified distance
        '''
        self.y = self.y + distance
    
    def getDistance(self, other:'Person') -> float:
        '''
        Calculates the distance between two Person(s) using the
        euclidean distance formula
        '''
        return sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))
    
    def __str__(self):
        '''
        __str__ method for Person
        '''
        return f"Person: name = {self.name}\tsize = {self.size}\tx = {self.x}\ty = {self.y}"
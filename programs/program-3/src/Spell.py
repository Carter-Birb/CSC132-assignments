import pygame
import constants
from Element import Element

class Spell(Element):
    
    def __init__(self, position:tuple[int, int]):
        width = 5
        height = 10
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.fill(constants.BLUE)  # Just fill it with a blue color
        super().__init__(image, position)  # Pass to the parent class
    
    def update(self):
        self.move("up")
        if self.rect.top <= 0:
            self.kill()

